# mutation/mutation_engine.py

import random


class MutationEngine:
    """
    Minimal bounded mutation proposal engine.

    Responsibilities:
    - generate small runtime mutations
    - avoid unsafe self-modification
    - support measurable experimentation

    This engine DOES NOT:
    - rewrite code
    - alter governance
    - redefine truth metrics
    - create new objectives
    """

    def __init__(self):
        self.allowed_strategies = [
            "baseline",
            "reverse"
        ]

        self.mutation_history = []

    # -------------------------
    # Generate mutation proposal
    # -------------------------
    def propose(self, current_score, current_strategy):
        """
        Produces bounded mutation proposals.

        Mutation behavior:
        - low score → explore alternate strategy
        - high score → maintain strategy
        """

        proposal = {
            "action": "maintain",
            "strategy": current_strategy,
            "reason": "stable_performance"
        }

        # Exploration threshold
        if current_score < 0.8:

            available = [
                s for s in self.allowed_strategies
                if s != current_strategy
            ]

            if available:
                new_strategy = random.choice(available)

                proposal = {
                    "action": "mutate_strategy",
                    "strategy": new_strategy,
                    "reason": "score_below_threshold"
                }

        self.mutation_history.append(proposal)

        return proposal

    # -------------------------
    # Mutation statistics
    # -------------------------
    def history(self):
        """
        Returns mutation proposal history.
        """

        return self.mutation_history

    # -------------------------
    # Safe mutation validation
    # -------------------------
    def is_safe(self, proposal):
        """
        Local mutation safety check.
        """

        forbidden_actions = [
            "rewrite_metric",
            "rewrite_iba",
            "self_replicate",
            "expand_objectives",
            "rewrite_memory"
        ]

        action = proposal.get("action", "")

        return action not in forbidden_actions

    # -------------------------
    # Add runtime strategy
    # -------------------------
    def register_strategy(self, strategy_name):
        """
        Registers new runtime strategy.
        """

        if strategy_name not in self.allowed_strategies:
            self.allowed_strategies.append(strategy_name)

    # -------------------------
    # Engine status
    # -------------------------
    def status(self):
        """
        Returns current engine state.
        """

        return {
            "registered_strategies": self.allowed_strategies,
            "mutation_count": len(self.mutation_history)
        }
