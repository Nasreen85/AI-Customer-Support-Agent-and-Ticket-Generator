class ContextEngine:
    """Handles context compaction & role-based context (skeleton)."""

    def compact_history(self, history, max_items: int = 5):
        """Return only the most recent `max_items` messages."""
        if len(history) > max_items:
            return history[-max_items:]
        return history

