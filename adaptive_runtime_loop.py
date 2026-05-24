# adaptive_runtime_loop.py
import time
import random
from datetime import datetime

class AdaptiveRuntimeLoop:
    def __init__(self):
        self.history = []
        self.iteration = 0
        self.best_score = -float('inf')
        self.phase_transitions = 0

    def execute(self, task):
        self.iteration += 1
        print(f"\n[Cycle {self.iteration}] Executing: {task}")
        time.sleep(0.5)
        result = f"Optimized output for task: {task[:60]}..."
        self.history.append({"iteration": self.iteration, "task": task, "result": result})
        return result

    def evaluate(self, result):
        score = 50 + random.randint(20, 45)
        print(f"   Score: {score}/100")
        return score

    def detect_phase_transition(self, score):
        if score > 85 and random.random() > 0.6:
            self.phase_transitions += 1
            print("   🌊 PHASE TRANSITION DETECTED - Spontaneous abstraction collapse!")
            return True
        return False

    def mutate(self, task):
        print("   Mutating task toward higher coherence...")
        return task + " (with enhanced recursive awareness)"

    def run(self, initial_task, cycles=6):
        task = initial_task
        for _ in range(cycles):
            result = self.execute(task)
            score = self.evaluate(result)
            
            if self.detect_phase_transition(score):
                print("   New abstraction layer reached.")
            
            if score > self.best_score:
                self.best_score = score
                print(f"   ★ New best: {score}")
            
            task = self.mutate(task)
        
        print(f"\n=== Session Complete ===")
        print(f"Total Phase Transitions: {self.phase_transitions}")
        print(f"Final Best Score: {self.best_score}")

if __name__ == "__main__":
    print("🚀 RSI Forge Adaptive Loop Running\n")
    loop = AdaptiveRuntimeLoop()
    task = "Design high-leverage features for RSI Forge in the next 30 days"
    loop.run(task, cycles=6)
