class Operators:
    """Three competitive operators for 2-player MCTS: counter, learning, innovation."""
    
    AVAILABLE = ["counter", "learning", "innovation"]
    
    @staticmethod
    def apply(operator: str, node, mcts, client, prompts, strategy_id, baseline_cost):
        """
        Apply operator to generate new code for node.active_player.
        Uses node.active_player (NOT a global current_player).
        """
        active_player = node.active_player
        current_impl = node.get_code(active_player)
        
        system_prompt = prompts.get(
            "SYSTEM_PROMPT",
            (
                "You are an expert in the domain of optimization heuristics. "
                "Your task is to design heuristics that can effectively solve optimization problems."
            )
        )
        task_prompt = prompts.get(strategy_id, "")
        baseline_impl = mcts.controller.get_current_best_implementation(strategy_id)
        
        context = Operators._build_context(
            node, mcts, baseline_cost, current_impl, operator, baseline_impl,
            active_player, task_prompt
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": context}
        ]
        
        _, code, summary = client.get_code(messages, function_id=strategy_id)
        return code, summary
    
    @staticmethod
    def _build_context(node, mcts, baseline_cost, current_impl, operator_type, baseline_impl, active_player, task_prompt):
        task_section = task_prompt

        baseline_section = f"""BASELINE IMPLEMENTATION:
```python
{baseline_impl}
```"""
        
        current_cost = node.get_cost(active_player)
        current_improvement = node.get_improvement(active_player)
        
        if current_cost == float('inf') or current_cost is None:
            status_info = "FAILED - Implementation has errors"
            improvement_info = f"Improvement: {current_improvement:.2f}% (failed)"
        else:
            status_info = f"Cost: {current_cost:.6f}"
            improvement_info = f"Improvement: {current_improvement:.2f}%"
        
        current_section = f"""CURRENT SOLUTION ({active_player}):
- Status: {status_info}
- {improvement_info}

IMPLEMENTATION:
```python
{current_impl}
```"""
        
        # Get opponent's best (using active_player to determine opponent)
        opponent_best_code = mcts.get_opponent_best_code(active_player)
        opponent_best_improvement = mcts.get_opponent_best_improvement(active_player)
        
        opponent_section = f"""OPPONENT BEST:
- Improvement over baseline: {opponent_best_improvement:.2f}%

```python
{opponent_best_code}
```"""
        
        path_summaries = node.get_path_summaries(max_depth=3)
        history_text = "\n".join(f"- {s}" for s in path_summaries) if path_summaries else "- No moves yet"
        
        history_section = f"""RECENT SUCCESSFUL CHANGES:
{history_text}
"""
        
        instructions = Operators._get_operator_instructions(operator_type)
        
        instructions_section = f"""---
INSTRUCTION:
{instructions}

GOAL:
Create an implementation that beats both baseline cost ({baseline_cost:.6f}) and the opponent.
Keep reasoning concise (50 words max)."""
        
        return f"{task_section}\n\n{baseline_section}\n\n{current_section}\n\n{opponent_section}\n\n{history_section}\n\n{instructions_section}"
    
    @staticmethod
    def _get_operator_instructions(operator_type):
        if operator_type == "counter":
            return "Counter: identify a weakness in the opponent implementation and improve on it."
        
        elif operator_type == "learning":
            return "Learning: reuse the opponent's best useful idea and combine it with a stronger variant."
        
        elif operator_type == "innovation":
            return "Innovation: try a different heuristic idea from both baseline and opponent."
        
        return "Optimize the implementation to outperform opponent."
