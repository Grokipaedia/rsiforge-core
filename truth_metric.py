# evaluation/truth_metric.py

class TruthMetric:
    """
    Minimal runtime evaluation system for RSIForge Core.

    Purpose:
    - measure execution quality
    - produce comparable scores
    - guide bounded mutation decisions

    This is NOT "truth" in a philosophical sense.

    It is simply:
    a measurable runtime scoring mechanism.
    """

    def __init__(self):
        self.metric_name = "runtime_efficiency"

    # -------------------------
    # Primary scoring function
    # -------------------------
    def score(self, input_data, output):
        """
        Scores execution result.

        Current scoring logic:
        - output length similarity
        - execution consistency
        - deterministic structure

        Returns:
            float between 0.0 and 1.0
        """

        if not input_data:
            return 0.0

        input_len = len(str(input_data))
        output_len = len(str(output))

        length_similarity = 1.0 - abs(input_len - output_len) / max(input_len, 1)

        if output == input_data:
            consistency_bonus = 0.2
        else:
            consistency_bonus = 0.0

        raw_score = length_similarity + consistency_bonus

        return min(max(raw_score, 0.0), 1.0)

    # -------------------------
    # Compare scores
    # -------------------------
    def improved(self, old_score, new_score):
        """
        Determines whether runtime behavior improved.
        """

        return new_score > old_score

    # -------------------------
    # Normalize score
    # -------------------------
    def normalize(self, score):
        """
        Ensures score stays within valid bounds.
        """

        return min(max(score, 0.0), 1.0)

    # -------------------------
    # Human-readable explanation
    # -------------------------
    def explain(self, score):
        """
        Converts score into simple runtime interpretation.
        """

        if score >= 0.9:
            return "high_runtime_alignment"

        elif score >= 0.6:
            return "moderate_runtime_alignment"

        elif score >= 0.3:
            return "weak_runtime_alignment"

        return "poor_runtime_alignment"
