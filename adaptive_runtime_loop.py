# adaptive_runtime_loop.py
import time
import json
from datetime import datetime

class AdaptiveRuntimeLoop:
    def __init__(self):
        self.memory = []
        self.iteration = 0
        self.best_score = -float('inf')
        self.best_solution = None

    def execute(self, task):
        """Execute a real compute task"""
        print(f"\n[{self.iteration}] Executing: {task}")
        result = self._run_code_optimization_task(task)
        self.memory.append({
            "iteration": self.iteration,
            "task": task,
            "result": result,
            "timestamp": datetime.now().isoformat()
        })
        return result

    def evaluate(self, result):
        """Score based on quality, efficiency, and clarity"""
        score = 0
        if "optimized" in result.lower(): score += 40
        if "O(n)" in result or "efficient" in result.lower(): score += 30
        score += len(result) * 0.05  # reward clarity
        print(f"  Score: {score:.1f}/100")
        return score

    def mutate(self, task):
        """Propose improved version"""
        print("  Mutating task...")
        return task + " (with better time/space complexity and readability)"

    def validate(self, score):
        """Keep only improvements"""
        return score > self.best_score * 0.85

    def persist(self, result, score):
        if score > self.best_score:
            self.best_score = score
            self.best_solution = result
            print(f"  ★ New best solution (score: {score:.1f})")

    def _run_code_optimization_task(self, task):
        """Live external compute hook"""
        time.sleep(0.4)  # simulate real work
        
        # Example responses for demo
        if "sort" in task.lower():
            return "def optimized_sort(arr): return sorted(arr)  # O(n log n) with built-in optimization"
        elif "fib" in task.lower():
            return "def fib(n, memo={}): if n in memo: return memo[n]\n    if n <= 1: return n\n    memo[n] = fib(n-1) + fib(n-2)\n    return memo[n]"
        else:
            return f"Optimized solution for '{task}': Clean, efficient implementation with memoization and early termination."

    def run_cycle(self, initial_task):
        self.iteration += 1
        print(f"\n{'='*60}")
        print(f"ADAPTIVE CYCLE {self.iteration}")
        print(f"{'='*60}")

        result = self.execute(initial_task)
        score = self.evaluate(result)

        if self.validate(score):
            self.persist(result, score)
            mutated_task = self.mutate(initial_task)
            print(f"  Next cycle task: {mutated_task[:80]}...")
            return mutated_task
        else:
            print("  Mutation rejected — sticking with current best.")
            return initial_task


# === LIVE RUN ===
if __name__ == "__main__":
    print("🚀 Starting Adaptive Runtime Loop (Combo Mode)\n")
    
    loop = AdaptiveRuntimeLoop()
    task = "Optimize a Fibonacci function for both speed and clarity"
    
    for i in range(6):
        task = loop.run_cycle(task)
        time.sleep(0.6)
    
    print("\n" + "="*60)
    print("FINAL BEST SOLUTION:")
    print(loop.best_solution)
    print("="*60)
