DecodeLabs – Rule-Based AI Chatbot

**Project 1 | Artificial Intelligence Internship | DecodeLabs**

Project Overview

This project implements a simple Rule-Based AI Chatbot using Python. It simulates basic human interaction by identifying predefined keywords and generating appropriate responses using conditional logic and a dictionary-based knowledge base.

The chatbot continuously accepts user input, processes messages, identifies matching intents, and responds accordingly.

Objectives

- Understand fundamental AI chatbot architecture.
- Implement decision-making using Python `if-else` logic.
- Build a dictionary-based knowledge base.
- Handle user input through a continuous loop.
- Implement input sanitization and fallback responses.

Technologies Used

- **Programming Language:** Python 3
- **Code Editor:** Visual Studio Code
- **Core Concepts:** Dictionaries, Loops, Conditional Statements, String Operations and Functions.

Features

1. **Greeting Detection:** Responds to Hello, Hi, Hey and other greetings.
2. **Identity Recognition:** Answers questions about the chatbot's identity.
3. **Wellbeing Responses:** Responds to questions such as "How are you?"
4. **Thank You Recognition:** Handles appreciation messages.
5. **Help Support:** Explains the chatbot's basic capabilities.
6. **Farewell Detection:** Recognizes goodbye messages.
7. **Input Sanitization:** Converts input to lowercase and removes unnecessary whitespace.
8. **Fallback Mechanism:** Provides a default response when no matching rule is found.
9. **Exit Functionality:** Terminates the conversation using exit, quit or stop commands.

Project Structure

```text
DecodeLabs-Rule-Based-Chatbot/
│
├── chatbot.py
├── README.md
└── screenshots/
```

Installation and Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Directory

```bash
cd DecodeLabs-Rule-Based-Chatbot
```

### Step 3: Run the Chatbot

```bash
python chatbot.py
```

**Note:** Python 3 must be installed on your system.

Sample Interaction

```text
WELCOME TO DECODELABS AI CHATBOT

Chatbot: Hello! I am your virtual assistant.
Chatbot: Type 'help' to know what I can do.

You: Hello
Chatbot: Hello! Welcome to DecodeLabs Chatbot.

You: How are you?
Chatbot: I'm doing great! Thanks for asking.

You: Thank you
Chatbot: You're welcome! Happy to help you.

You: Exit
Chatbot: Goodbye! Have a nice day.
```

Core Implementation

| Concept | Implementation |
|---|---|
| Knowledge Base | Python Dictionary |
| Input Handling | `input()` |
| Sanitization | `lower()` and `strip()` |
| Continuous Execution | `while True` |
| Decision Making | `if-else` |
| Rule Matching | Keyword Matching |
| Fallback | Default Response |
| Termination | `break` |

Project Screenshots

Screenshots of the chatbot execution and sample conversations are available in the `screenshots/` directory.

Future Improvements

- Add more intents and conversational patterns.
- Integrate Natural Language Processing (NLP).
- Introduce an optional Large Language Model (LLM) fallback.
- Develop a graphical user interface.
- Improve keyword matching and context handling.

Author

Aryan Chouhan

Artificial Intelligence Intern – DecodeLabs

B.Tech, Electronics and Telecommunication Engineering

MITS-DU, Gwalior

---

**Project 1 – Rule-Based AI Chatbot | DecodeLabs Internship 2026**