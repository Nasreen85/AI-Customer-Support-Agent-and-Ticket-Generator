import re

class Planner:
    """
    Planner Agent:
    - Interprets user input
    - Detects intent
    - Generates a step-by-step plan for Worker
    """

    def __init__(self):
        pass

    def detect_intent(self, user_message: str) -> str:
        """Very simple rule-based intent detection."""
        text = user_message.lower()

        # Close ticket
        close_keywords = [
            "issue resolved", "problem resolved", "fixed now",
            "no longer", "it's working now", "close the ticket",
            "you can close", "resolved now"
        ]
        if any(k in text for k in close_keywords):
            return "close_ticket"

        # Escalation / still not working
        escalate_keywords = [
            "still not", "not working", "no help", "didn't help",
            "escalate", "talk to a human", "speak to someone"
        ]
        if any(k in text for k in escalate_keywords):
            return "escalate"

        # Check status / follow-up style
        status_keywords = ["status", "update", "any update", "ticket"]
        if any(k in text for k in status_keywords):
            return "check_status"

        # Greeting
        greet_keywords = ["hi", "hello", "hey"]
        if any(text.strip().startswith(k) for k in greet_keywords):
            # If it clearly mentions an issue, treat as new_issue
            issue_keywords = ["issue", "problem", "error", "crash", "fail", "cannot", "can't"]
            if any(k in text for k in issue_keywords):
                return "new_issue"
            return "greet"

        # Default: assume new issue
        return "new_issue"

    def create_plan(self, user_message, session):
        """Return a simple plan dict with an intent and ordered steps."""
        intent = self.detect_intent(user_message)

        if intent == "greet":
            steps = ["respond_greeting"]
        elif intent == "check_status":
            steps = ["check_ticket_status"]
        elif intent == "close_ticket":
            steps = ["close_ticket"]
        elif intent == "escalate":
            steps = ["escalate_ticket"]
        else:  # new_issue
            steps = [
                "collect_missing_fields",
                "create_ticket",
                "search_solution",
                "evaluate_and_finalize",
            ]

        plan = {
            "intent": intent,
            "steps": steps,
            "raw_user_message": user_message,
        }
        return plan
