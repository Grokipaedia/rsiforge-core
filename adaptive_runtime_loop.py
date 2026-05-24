# adaptive_runtime_loop.py
import time
import json
from datetime import datetime

class AdaptiveRuntimeLoop:
    def __init__(self):
        self.memory = []
        self.iteration = 0
        self.best_score = -float('inf')
    
    def execute(self, task):
        """Execute a task and return result"""
        print(f"[{self.iteration}] Executing task...")
        # Example: Simple external compute task
        result = self._run_compute_task(task)
        self.memory.append({"iteration": self.iteration, "task": task, "result": result})
        return result

    def evaluate(self, result):
        """Simple evaluation score"""
        score = len(str(result)) * 0.1 + (1 if "optimal" in str(result).lower() else 0)
        print(f"  Evaluation score: {score:.3f}")
        return score

    def mutate(self, task):
        """Propose mutation"""
        print(f"  Proposing mutation...")
        mutated = task + " (optimized version)"
        return mutated

    def validate(self, mutation, score):
        """Intent-Bound validation"""
        return score > self.best_score * 0.9

    def persist(self, result, score):
        """Persist to memory"""
        if score > self.best_score:
            self.best_score = score
            print(f"  New best score: {score:.3f} ★")

    def _run_compute_task(self, task):
        """Live external hook - replace with real API/compute"""
        time.sleep(0.3)  # simulate work
        return f"Computed result for: {task} → optimized_value=42.7"

    def run_cycle(self, initial_task):
        """One full adaptive cycle"""
        self.iteration += 1
        print(f"\n=== Cycle {self.iteration} ===")
        
        result = self.execute(initial_task)
        score = self.evaluate(result)
        
        mutation = self.mutate(initial_task)
        if self.validate(mutation, score):
            print("  Mutation validated ✓")
            self.persist(result, score)
        
        return {"iteration": self.iteration, "score": score, "best": self.best_score}

# Run live cycles
if __name__ == "__main__":
    loop = AdaptiveRuntimeLoop()
    task = "Optimize a simple sorting function for speed and clarity"
    
    for i in range(5):
        loop.run_cycle(task)
        task = loop.memory[-1]["result"]  # evolve the task
        time.sleep(0.5)
