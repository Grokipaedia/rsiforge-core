# core/adaptive_runtime_loop.py

import time
from evaluation.metric import TruthMetric
from mutation.mutation import MutationEngine
from governance.iba import IBA
from memory.store import MemoryStore


class AdaptiveRuntimeLoop:
    """
    Minimal bounded self-improving runtime loop.

    Responsibilities:
    - execute tasks
    - evaluate outcomes
    - propose mutations
    - validate intent through IBA
    - persist memory
    """

    def __init__(self):
        self.metric = TruthMetric()
        self.mutation_engine = MutationEngine()
        self.iba = IBA()
        self.memory = MemoryStore()

        self.runtime_state = {
            "iteration": 0,
            "strategy": "baseline"
        }

    # -------------------------
    # Step 1: Execute task
    # -------------------------
    def execute_task(self, input_data):
        """
        Executes current runtime strategy.
        """

        strategy = self.runtime_state["strategy"]

        if strategy == "baseline":
            output = input_data.upper()

        elif strategy == "reverse":
            output = input_data[::-1]

        else:
            output = input_data

        return output

    # -------------------------
    # Step 2: Evaluate output
    # -------------------------
    def evaluate(self, input_data, output):
        """
        Scores runtime behavior.
        """

        return self.metric.score(input_data, output)

    # -------------------------
    # Step 3: Generate mutation proposal
    # -------------------------
    def propose_mutation(self, score):
        """
        Generates bounded runtime mutation proposal.
        """

        return self.mutation_engine.propose(
            current_score=score,
            current_strategy=self.runtime_state["strategy"]
        )

    # -------------------------
    # Step 4: Apply validated mutation
    # -------------------------
    def apply_mutation(self, proposal):
        """
        Applies mutation after IBA validation.
        """

        if not self.iba.validate_intent(proposal):
            return {
                "status": "blocked_by_iba"
            }

        new_strategy = proposal.get("strategy")

        if new_strategy:
            self.runtime_state["strategy"] = new_strategy

        return {
            "status": "mutation_applied",
            "strategy": new_strategy
        }

    # -------------------------
    # Step 5: Persist execution memory
    # -------------------------
    def persist_memory(self, input_data, output, score):
        """
        Stores execution history.
        """

        self.memory.store({
            "iteration": self.runtime_state["iteration"],
            "input": input_data,
            "output": output,
            "score": score,
            "strategy": self.runtime_state["strategy"],
            "timestamp": time.time()
        })

    # -------------------------
    # Main runtime cycle
    # -------------------------
    def run_cycle(self, input_data):
        """
        Full bounded self-improving execution loop.
        """

        self.runtime_state["iteration"] += 1

        output = self.execute_task(input_data)

        score = self.evaluate(input_data, output)

        proposal = self.propose_mutation(score)

        mutation_result = self.apply_mutation(proposal)

        self.persist_memory(input_data, output, score)

        return {
            "iteration": self.runtime_state["iteration"],
            "input": input_data,
            "output": output,
            "score": score,
            "proposal": proposal,
            "mutation_result": mutation_result,
            "strategy": self.runtime_state["strategy"]
        }
