import random

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm a bot, so I don't have feelings, but thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_response(user_input):
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return "Sorry, I didn't get that. Please try again."

print("Welcome to Chatbot! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower():
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print(f"Chatbot: {response}")