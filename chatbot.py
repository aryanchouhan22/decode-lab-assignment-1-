
# ==========================================
# DecodeLabs - Rule-Based AI Chatbot
# Project 1: Artificial Intelligence
# ==========================================

# 1. Knowledge Base (Dictionary with 6 Intents)

knowledge_base = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! Welcome to DecodeLabs Chatbot. How can I help you?"
    },

    "identity": {
        "keywords": ["your name", "who are you", "what are you"],
        "response": "I am DecodeLabs Assistant, a simple rule-based AI chatbot."
    },

    "wellbeing": {
        "keywords": ["how are you", "how are you doing"],
        "response": "I'm doing great! Thanks for asking. How can I help you?"
    },

    "thanks": {
        "keywords": ["thank you", "thanks", "thank"],
        "response": "You're welcome! Happy to help you."
    },

    "help": {
        "keywords": ["help", "what can you do", "your features"],
        "response": "I can respond to greetings, answer basic questions, and have simple conversations."
    },

    "farewell": {
        "keywords": ["bye", "goodbye", "see you"],
        "response": "Goodbye! Thank you for chatting. Have a great day!"
    }
}


# 2. Exit Commands

exit_commands = ["exit", "quit", "stop"]


# 3. Chatbot Introduction

print("=" * 50)
print("       WELCOME TO DECODELABS AI CHATBOT")
print("=" * 50)
print("Chatbot: Hello! I am your virtual assistant.")
print("Chatbot: Type 'help' to know what I can do.")
print("Chatbot: Type 'exit' to end the conversation.")
print("-" * 50)


# 4. Continuous Input Loop

while True:

    # Take input from the user
    user_input = input("You: ")

    # 5. Input Sanitization
    # Convert to lowercase and remove extra spaces
    user_input = user_input.lower().strip()

    # Handle empty input
    if not user_input:
        print("Chatbot: Please enter something.")
        continue

    # 6. Exit Strategy
    if user_input in exit_commands:
        print("Chatbot: Goodbye! Have a nice day.")
        break

    # 7. Rule Matching
    response_found = False

    for intent, details in knowledge_base.items():

        for keyword in details["keywords"]:

            # Match complete words or phrases
            if keyword in user_input.split() or keyword in user_input:
                
                # Avoid matching short words inside longer words
                if len(keyword.split()) == 1 and keyword not in user_input.split():
                    continue

                print("Chatbot:", details["response"])
                response_found = True
                break

        if response_found:
            break

    # 8. Fallback Response
    if not response_found:
        print("Chatbot: Sorry, I don't understand that.")
        print("Chatbot: Please try asking something else.")

