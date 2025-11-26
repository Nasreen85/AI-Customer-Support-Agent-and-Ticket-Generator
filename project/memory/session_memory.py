class SessionMemory:
    """Stores simple in-memory session data (single-process demo only)."""

    def __init__(self):
        self.sessions = {}

    def get_session(self, session_id: str = "default"):
        if session_id not in self.sessions:
            self.sessions[session_id] = {
                "customer_profile": {},   # name, phone, email
                "current_ticket": None,   # latest ticket dict
                "tickets": [],            # list of all tickets
                "conversation_history": [],
                "ticket_counter": 0,
            }
        return self.sessions[session_id]

    def add_message(self, session: dict, role: str, content: str) -> None:
        """Append a message to conversation history."""
        session.setdefault("conversation_history", []).append(
            {"role": role, "content": content}
        )

