class Evaluator:
    """Evaluator Agent: validates solution quality (skeleton)."""

    def __init__(self):
        pass

    def evaluate(self, worker_output):
        """Always approves in this skeleton version."""
        return {
            "approved": True,
            "feedback": "Looks good.",
        }
