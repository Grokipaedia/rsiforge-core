# memory/memory_store.py

import json
import os
import time


class MemoryStore:
    """
    Minimal persistent runtime memory system.

    Responsibilities:
    - store execution history
    - persist runtime observations
    - provide bounded memory recall

    This is NOT:
    - semantic memory
    - vector memory
    - long-term cognition

    It is simply:
    structured runtime persistence.
    """

    def __init__(self, memory_file="runtime_memory.json"):

        self.memory_file = memory_file

        # Ensure memory file exists
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    # -------------------------
    # Store runtime event
    # -------------------------
    def store(self, event):
        """
        Stores execution event in persistent memory.
        """

        memory = self.load_all()

        event["stored_at"] = time.time()

        memory.append(event)

        with open(self.memory_file, "w") as f:
            json.dump(memory, f, indent=2)

    # -------------------------
    # Load all memory
    # -------------------------
    def load_all(self):
        """
        Loads complete runtime memory.
        """

        try:
            with open(self.memory_file, "r") as f:
                return json.load(f)

        except Exception:
            return []

    # -------------------------
    # Recall recent events
    # -------------------------
    def recent(self, limit=5):
        """
        Returns recent runtime events.
        """

        memory = self.load_all()

        return memory[-limit:]

    # -------------------------
    # Memory statistics
    # -------------------------
    def stats(self):
        """
        Returns memory system statistics.
        """

        memory = self.load_all()

        return {
            "total_events": len(memory),
            "memory_file": self.memory_file
        }

    # -------------------------
    # Clear memory
    # -------------------------
    def clear(self):
        """
        Clears runtime memory.
        """

        with open(self.memory_file, "w") as f:
            json.dump([], f)

    # -------------------------
    # Search memory
    # -------------------------
    def search(self, key, value):
        """
        Searches memory by key/value pair.
        """

        memory = self.load_all()

        results = []

        for event in memory:
            if event.get(key) == value:
                results.append(event)

        return results
