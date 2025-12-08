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
            current_combination, target_strategy, baseline_cost, player,
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
        baseline_text = ""
        for strategy_id, code in baseline_combination.items():
            baseline_text += f"<{strategy_id.lower()}>\n{code}\n</{strategy_id.lower()}>\n\n"
        
        return f"""You are in the FINAL ROUND of competitive optimization.

GOAL: Beat both baseline cost ({baseline_cost:.6f}) AND your opponent.

BASELINE SYSTEM:
{baseline_text}

TARGET: Optimize {target_strategy}

COMPETITION RULES:
- Baseline is FIXED during this strategy optimization
- Beat baseline AND opponent for maximum reward
- Consider system-level synergies between strategies
- Maintain code correctness and efficiency

SUCCESS CRITERIA:
- Cost < {baseline_cost:.6f} (beat baseline)
- Cost < opponent's best (beat opponent)"""

    @staticmethod
    def _build_context(current_combination: dict, target_strategy: str, baseline_cost: float,
                       player: str, opponent_best_code: str, opponent_best_improvement: float,
                       successful_summaries: list):
        # Current system state
        system_parts = []
        for strategy_id, code in current_combination.items():
            system_parts.append(f"<{strategy_id.lower()}>\n{code}\n</{strategy_id.lower()}>")
        system_text = "\n\n".join(system_parts)
        
        system_section = f"""<current_system>
{system_text}
</current_system>"""
        
        # Target strategy
        current_impl = current_combination[target_strategy]
        target_section = f"""<target_strategy>
Optimize: {target_strategy}

Current implementation:
{current_impl}
</target_strategy>"""
        
        # Opponent info
        if opponent_best_code:
            opponent_section = f"""<opponent>
Opponent's best implementation for {target_strategy} (improvement: {opponent_best_improvement:.2f}%):
{opponent_best_code}
</opponent>"""
        else:
            opponent_section = f"""<opponent>
No opponent results yet for {target_strategy}.
</opponent>"""
        
        # History of successful moves
        if successful_summaries:
            history_text = "\n".join(f"- {s}" for s in successful_summaries[-3:])
        else:
            history_text = "- No successful moves yet"
        
        history_section = f"""<history>
Successful moves for {target_strategy}:
{history_text}
</history>"""
        
        # Instructions
        instructions = f"""<instructions>
TASK: Optimize {target_strategy} to beat BOTH baseline ({baseline_cost:.6f}) AND opponent.

You are {player}.

Focus on:
- Hyperparameter tuning
- Algorithm variants
- System-level synergies with other strategies

Provide an improved implementation that achieves lower cost.
</instructions>"""
        
        return f"{system_section}\n\n{target_section}\n\n{opponent_section}\n\n{history_section}\n\n{instructions}"
