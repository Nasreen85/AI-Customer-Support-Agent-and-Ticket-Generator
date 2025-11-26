import datetime

class Logger:
    """Simple logger + tiny in-memory metrics."""

    total_messages = 0
    total_tickets_created = 0

    @staticmethod
    def log(message: str) -> None:
        now = datetime.datetime.now().isoformat(timespec="seconds")
        Logger.total_messages += 1
        print(f"[LOG {now}] {message}")

    @staticmethod
    def ticket_created():
        Logger.total_tickets_created += 1
        Logger.log(f"Ticket created. Total tickets so far: {Logger.total_tickets_created}")

