import random
responses = {
    "hi": ["Hello!", "Hi there!", "Greetings!"],
    "do you know programming": ["I'm a bot","i don't know programming"],
    "what is your name": ["I am a simple chatbot created by you.", "You can call me Chatbot."],
    "bye": ["Goodbye!", "See you later!", "Have a nice day!"]
}

# Function to get a response based on user input
def get_response(user_input):
    # Convert the input to lowercase to make the bot case insensitive
    user_input = user_input.lower()
    
    # Find a response from the predefined responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    # Default response if no keyword is found
    return "I didn't understand that. Can you please rephrase?"

# Main function to run the chatbot
def chatbot():
    print("Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        
        response = get_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()