import re

class Worker:
    """Worker Agent: executes plan steps using tools."""

    def __init__(self, tools):
        self.tools = tools

    def _extract_name(self, text: str):
        """Naive name extraction: looks for 'my name is ...'."""
        m = re.search(r"my name is ([A-Za-z ]+)", text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
        return None

    def _extract_phone(self, text: str):
        """Naive phone extraction: 7-15 digit number (optionally with +)."""
        m = re.search(r"(\+?\d{7,15})", text)
        if m:
            return m.group(1)
        return None

    def execute_plan(self, plan, session):
        """Execute based on intent."""
        intent = plan.get("intent", "new_issue")

        if intent == "greet":
            return self._handle_greet(plan, session)

        if intent == "check_status":
            return self._handle_check_status(plan, session)

        if intent == "close_ticket":
            return self._handle_close_ticket(plan, session)

        if intent == "escalate":
            return self._handle_escalate_ticket(plan, session)

        # Default: new issue flow
        return self._handle_new_issue(plan, session)

    # ---- intent handlers ----

    def _handle_greet(self, plan, session):
        """Simple greeting response, no ticket."""
        response = "Hello! How can I help you with your issue today?"
        return {
            "ticket_id": None,
            "solution": response,
        }

    def _handle_check_status(self, plan, session):
        """Return status of latest ticket if available."""
        current_ticket = session.get("current_ticket")
        if current_ticket is None:
            response = (
                "I couldn't find any existing tickets in this session. "
                "Please describe your issue and I'll create a new ticket for you."
            )
            return {
                "ticket_id": None,
                "solution": response,
            }

        ticket_id = current_ticket.get("ticket_id")
        status = current_ticket.get("status", "Open")
        issue = current_ticket.get("issue_description", "your last reported issue")

        response = (
            f"Your latest ticket {ticket_id} about '{issue}' is currently marked as '{status}'."
        )
        return {
            "ticket_id": ticket_id,
            "solution": response,
        }

    def _handle_close_ticket(self, plan, session):
        """Mark current ticket as closed."""
        current_ticket = session.get("current_ticket")
        if current_ticket is None:
            response = (
                "I couldn't find any active ticket to close in this session. "
                "If your issue is resolved, thank you for letting us know!"
            )
            return {
                "ticket_id": None,
                "solution": response,
            }

        current_ticket["status"] = "Closed"
        ticket_id = current_ticket["ticket_id"]
        response = (
            f"Thank you for the update. I have marked ticket {ticket_id} as 'Closed'. "
            "We're glad your issue is resolved."
        )
        return {
            "ticket_id": ticket_id,
            "solution": response,
        }

    def _handle_escalate_ticket(self, plan, session):
        """Mark current ticket as escalated."""
        current_ticket = session.get("current_ticket")
        if current_ticket is None:
            response = (
                "I couldn't find any existing ticket to escalate. "
                "Please describe your issue again, and I'll create a ticket and escalate it."
            )
            return {
                "ticket_id": None,
                "solution": response,
            }

        current_ticket["status"] = "Escalated"
        ticket_id = current_ticket["ticket_id"]
        issue = current_ticket.get("issue_description", "your issue")

        response = (
            f"I'm sorry this is still causing trouble. I have escalated ticket {ticket_id} "
            f"about '{issue}' to our senior support team. They will review it with priority."
        )
        return {
            "ticket_id": ticket_id,
            "solution": response,
        }

    def _handle_new_issue(self, plan, session):
        """Create a new ticket, call solution finder, and respond."""
        user_text = plan.get("raw_user_message", "")

        # Extract basic info if available
        name = self._extract_name(user_text)
        phone = self._extract_phone(user_text)

        # Update customer profile
        profile = session.get("customer_profile", {})
        if name:
            profile["name"] = name
        if phone:
            profile["phone"] = phone
        session["customer_profile"] = profile

        # Increment ticket counter
        session["ticket_counter"] = session.get("ticket_counter", 0) + 1
        counter = session["ticket_counter"]
        ticket_id = f"TCKT-{counter:05d}"

        ticket = {
            "ticket_id": ticket_id,
            "issue_description": user_text,
            "status": "Open",
        }

        # Save as current + append to tickets list
        session["current_ticket"] = ticket
        tickets = session.get("tickets", [])
        tickets.append(ticket)
        session["tickets"] = tickets

        # Call tools to find a possible solution (internal KB + fake web)
        solution_hint = self.tools.find_best_solution(user_text)

        display_name = profile.get("name", "customer")
        base_msg = (
            f"Thank you, {display_name}. Your ticket {ticket_id} has been created "
            f"with status 'Open'. Our support team will assist you shortly."
        )

        if solution_hint:
            full_msg = (
                base_msg
                + " In the meantime, here is a possible solution you can try:\n"
                + solution_hint
            )
        else:
            full_msg = base_msg

        return {
            "ticket_id": ticket_id,
            "solution": full_msg,
        }

