class FinalOperators:
    """Operators for Final Round sequential optimization."""
    
    @staticmethod
    def apply(current_combination: dict, target_strategy: str, client, 
              baseline_combination: dict, baseline_cost: float, player: str,
              opponent_best_code: str = None, opponent_best_improvement: float = 0.0,
              successful_summaries: list = None):
        """Apply optimization to target strategy with full system context."""
        system_prompt = FinalOperators._get_system_prompt(
            baseline_combination, baseline_cost, target_strategy
        )
        
        context = FinalOperators._build_context(
            current_combination, baseline_combination, target_strategy, baseline_cost, player,
            opponent_best_code, opponent_best_improvement, successful_summaries
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": context}
        ]
        
        _, code, summary = client.get_code(messages, function_id=f"FINAL_{target_strategy}")
        return code, summary
    
    @staticmethod
    def _get_system_prompt(baseline_combination: dict, baseline_cost: float, target_strategy: str):
        return (
            "You are an expert in the domain of optimization heuristics. "
            "Your task is to design heuristics that can effectively solve optimization problems."
        )

    @staticmethod
    def _build_baseline_section(baseline_combination: dict, baseline_cost: float, target_strategy: str):
        baseline_text = ""
        for strategy_id, code in baseline_combination.items():
            baseline_text += f"{strategy_id}:\n```python\n{code}\n```\n\n"
        
        return f"""FINAL ROUND:
- Target strategy: {target_strategy}
- Baseline cost: {baseline_cost:.6f}
- Improve the target while keeping the full system coherent.

BASELINE SYSTEM:
{baseline_text}

RULES:
- Keep the exact function signature.
- Beat the fixed baseline and the opponent if possible.
- Consider interactions with the other strategies.
- Keep reasoning concise (50 words max).
---"""

    @staticmethod
    def _build_context(current_combination: dict, baseline_combination: dict, target_strategy: str,
                       baseline_cost: float, player: str, opponent_best_code: str, opponent_best_improvement: float,
                       successful_summaries: list):
        # Current system state
        baseline_section = FinalOperators._build_baseline_section(
            baseline_combination, baseline_cost, target_strategy
        )

        system_parts = []
        for strategy_id, code in current_combination.items():
            system_parts.append(f"{strategy_id}:\n```python\n{code}\n```")
        system_text = "\n\n".join(system_parts)
        
        system_section = f"""CURRENT SYSTEM:
{system_text}
"""
        
        # Target strategy
        current_impl = current_combination[target_strategy]
        target_section = f"""TARGET STRATEGY:
{target_strategy}

CURRENT IMPLEMENTATION:
```python
{current_impl}
```"""
        
        # Opponent info
        if opponent_best_code:
            opponent_section = f"""OPPONENT BEST FOR {target_strategy}:
- Improvement over baseline: {opponent_best_improvement:.2f}%

```python
{opponent_best_code}
```"""
        else:
            opponent_section = f"""OPPONENT BEST FOR {target_strategy}:
- No opponent result yet."""
        
        # History of successful moves
        if successful_summaries:
            history_text = "\n".join(f"- {s}" for s in successful_summaries[-3:])
        else:
            history_text = "- No successful moves yet"
        
        history_section = f"""RECENT SUCCESSFUL MOVES FOR {target_strategy}:
{history_text}
"""
        
        # Instructions
        instructions = f"""---
INSTRUCTION:
You are {player}. Optimize {target_strategy} to beat baseline cost {baseline_cost:.6f} and the opponent.

FOCUS:
- Hyperparameter tuning
- Formula variants
- System-level synergies with other strategies

Return an improved implementation only for {target_strategy}."""
        
        return f"{baseline_section}\n\n{system_section}\n\n{target_section}\n\n{opponent_section}\n\n{history_section}\n\n{instructions}"
