class Tools:
    """
    Tool collection:
    - Simple internal knowledge base
    - Fake web search
    - Placeholder for Google Sheets
    """

    def __init__(self):
        # Tiny FAQ-style knowledge base
        self.knowledge_base = [
            {
                "pattern": "login",
                "solution": (
                    "Try clearing your browser cache/cookies and make sure you are "
                    "using the latest version of the app. If the issue continues, "
                    "try resetting your password once."
                ),
            },
            {
                "pattern": "payment",
                "solution": (
                    "If payment failed but money was deducted, please wait 24 hours. "
                    "Most banks automatically reverse the transaction. If it does not "
                    "return, contact support with your transaction ID."
                ),
            },
            {
                "pattern": "crash",
                "solution": (
                    "Please reinstall the app and ensure your OS is up to date. "
                    "Crashes are often caused by outdated versions or corrupted installs."
                ),
            },
            {
                "pattern": "password",
                "solution": (
                    "Use the 'Forgot Password' option on the login page. "
                    "Check your spam folder if you don't receive the reset email."
                ),
            },
        ]

    # -------- Domain tools (placeholders / simple logic) --------

    def google_sheets_create_ticket(self, data):
        """Fake placeholder for Sheets ticket creation."""
        return True

    def search_internal_docs(self, query):
        """
        Very simple internal docs search:
        - If a pattern is found in query, return that solution.
        - Otherwise return None.
        """
        text = query.lower()
        for item in self.knowledge_base:
            if item["pattern"] in text:
                return item["solution"]
        return None

    def web_search(self, query):
        """
        Fake web search.
        In a real system, this would call an external search API.
        """
        return (
            "I checked external resources and found general guidance, "
            "but for security reasons I'm logging this for a human agent to review."
        )

    def find_best_solution(self, issue_text: str):
        """
        Combines internal docs and (fake) web search.
        - Try internal docs first
        - If nothing found, fallback to a generic web-style answer
        """
        internal = self.search_internal_docs(issue_text)
        if internal:
            return internal
        return self.web_search(issue_text)


