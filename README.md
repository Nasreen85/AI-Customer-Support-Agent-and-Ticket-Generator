🌟 AI Customer Support Agent & Ticket Generator

A fully automated AI Customer Support Agent built using Google ADK with a clean multi-agent architecture.
This system understands customer issues, generates support tickets, provides solutions, and evaluates responses — all autonomously.

🚀 Features
🧠 Multi-Agent Architecture

Planner Agent – Interprets user input and creates a plan

Worker Agents – Execute support tasks

Safety Worker

Helpline Worker

Evaluator Agent – Checks quality of final output

Main Agent – Orchestrates everything using ADK

🎫 Intelligent Ticket Handling

Automatically generates unique ticket IDs

Extracts and stores user details

Maintains ticket status (Open / In Progress / Closed)

💾 Session Memory

Preserves conversation history

Remembers user details and issue context across messages

🔧 Modular ADK Design

Organized folder structure

Easy to extend with new agents or tools

Clean separation of logic

🧪 Demo Script Included

Test the agent quickly using:

python run_demo.py

📁 Project Structure
project/
│
├── agents/
│   ├── planner.py
│   ├── worker.py
│   └── evaluator.py
│
├── core/
│   ├── routing.py
│   └── observability.py
│
├── memory/
│   └── session_memory.py
│
├── tools/
│   └── tools.py
│
├── app.py
├── main_agent.py
├── requirements.txt
└── run_demo.py

🧩 Architecture Diagram (Mermaid)
flowchart TD
    U[User] -->|Message| M[Main Agent]

    M --> P[Planner Agent]
    P --> W1[Safety Worker]
    P --> W2[Helpline Worker]

    W1 --> E[Evaluator Agent]
    W2 --> E

    M --> MEM[Session Memory]
    MEM --> M

    E --> M
    M -->|Final Response + Ticket ID| U

⚙️ Installation & Running
1️⃣ Clone the repository
git clone https://github.com/<your-username>/AI-Customer-Support-Agent-and-Ticket-Generator.git
cd AI-Customer-Support-Agent-and-Ticket-Generator/project

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your Google API Key

Windows:

set GOOGLE_API_KEY=your_api_key_here


macOS / Linux:

export GOOGLE_API_KEY=your_api_key_here

4️⃣ Run the demo
python run_demo.py

💬 Example Usage

User Message:

My name is Raj. My number is +971501234567. My app keeps crashing when I login.

AI Agent Output:

Extracts user name

Creates ticket: TCKT-00001

Suggests troubleshooting steps

Stores context in session

Final Response Example:

Thank you Raj. Your ticket TCKT-00001 has been created with status 'Open'.
Try clearing your cache or updating the app to the latest version.

🤝 Contributing

Pull Requests and contributions are welcome!
Please refer to CONTRIBUTING.md before submitting.

📄 License

This project is licensed under the MIT License.
See LICENSE.txt for full details.
