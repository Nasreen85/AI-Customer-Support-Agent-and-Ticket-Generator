from project.agents.planner import Planner
from project.agents.worker import Worker
from project.agents.evaluator import Evaluator
from project.tools.tools import Tools
from project.memory.session_memory import SessionMemory
from project.core.observability import Logger

class MainAgent:
    """Main orchestrator for the multi-agent support system."""

    def __init__(self):
        self.planner = Planner()
        self.tools = Tools()
        self.worker = Worker(self.tools)
        self.evaluator = Evaluator()
        self.memory = SessionMemory()

    def handle_message(self, user_input: str):
        session = self.memory.get_session()
        self.memory.add_message(session, "user", user_input)
        Logger.log("Received user message.")

        plan = self.planner.create_plan(user_input, session)
        Logger.log(f"Plan created with intent: {plan.get('intent')}")

        worker_result = self.worker.execute_plan(plan, session)
        Logger.log("Worker executed plan.")

        evaluation = self.evaluator.evaluate(worker_result)
        Logger.log(f"Evaluator validated results. Approved: {evaluation.get('approved')}")

        response = worker_result["solution"]
        self.memory.add_message(session, "agent", response)

        return {
            "response": response,
            "ticket_id": worker_result["ticket_id"],
            "evaluation": evaluation,
        }

def run_agent(user_input: str):
    """Convenience function for one-off calls."""
    agent = MainAgent()
    result = agent.handle_message(user_input)
    return result["response"]

