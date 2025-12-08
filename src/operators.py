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
        
        system_prompt = prompts.get(strategy_id, "")
        baseline_impl = mcts.controller.get_current_best_implementation(strategy_id)
        
        context = Operators._build_context(
            node, mcts, baseline_cost, current_impl, operator, baseline_impl, active_player
        )
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": context}
        ]
        
        _, code, summary = client.get_code(messages, function_id=strategy_id)
        return code, summary
    
    @staticmethod
    def _build_context(node, mcts, baseline_cost, current_impl, operator_type, baseline_impl, active_player):
        baseline_section = f"""<baseline>
{baseline_impl}
</baseline>"""
        
        current_cost = node.get_cost(active_player)
        current_improvement = node.get_improvement(active_player)
        
        if current_cost == float('inf') or current_cost is None:
            status_info = "FAILED - Implementation has errors"
            improvement_info = f"Improvement: {current_improvement:.2f}% (failed)"
        else:
            status_info = f"Cost: {current_cost:.6f}"
            improvement_info = f"Improvement: {current_improvement:.2f}%"
        
        current_section = f"""<current_solution>
Status: {status_info}
{improvement_info}

Implementation:
{current_impl}
</current_solution>"""
        
        # Get opponent's best (using active_player to determine opponent)
        opponent_best_code = mcts.get_opponent_best_code(active_player)
        opponent_best_improvement = mcts.get_opponent_best_improvement(active_player)
        
        opponent_section = f"""<opponent>
Latest best implementation (improvement: {opponent_best_improvement:.2f}% over baseline):
{opponent_best_code}
</opponent>"""
        
        path_summaries = node.get_path_summaries(max_depth=3)
        history_text = "\n".join(f"- {s}" for s in path_summaries) if path_summaries else "- No moves yet"
        
        history_section = f"""<history>
{history_text}
</history>"""
        
        instructions = Operators._get_operator_instructions(operator_type)
        
        instructions_section = f"""<instructions>
{instructions}

Your goal: Create implementation that outperforms both baseline and opponent.
Think step-by-step to achieve the best result.
</instructions>"""
        
        return f"{baseline_section}\n\n{current_section}\n\n{opponent_section}\n\n{history_section}\n\n{instructions_section}"
    
    @staticmethod
    def _get_operator_instructions(operator_type):
        if operator_type == "counter":
            return """COUNTER STRATEGY:
Analyze opponent's implementation and identify weaknesses or inefficiencies.
Create an implementation that specifically exploits these weaknesses.
Focus on areas where opponent's approach is suboptimal."""
        
        elif operator_type == "learning":
            return """LEARNING STRATEGY:
Study opponent's successful techniques and innovations.
Combine their best ideas with your own approach to create superior implementation.
Learn from their strengths while maintaining your unique advantages."""
        
        elif operator_type == "innovation":
            return """INNOVATION STRATEGY:
Create completely novel approach that differs from both baseline and opponent.
Think outside the box and introduce breakthrough techniques.
Pioneer new algorithmic paradigms."""
        
        return "Optimize the implementation to outperform opponent."
