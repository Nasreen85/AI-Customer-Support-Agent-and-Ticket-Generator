from project.main_agent import run_agent

def chat(message: str) -> str:
    return run_agent(message)

if __name__ == "__main__":
    print(chat("Hello from app!"))

