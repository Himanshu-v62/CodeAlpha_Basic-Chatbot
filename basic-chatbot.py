# chatbot.py
"""
Simple Rule-Based Chatbot
Responds to basic greetings and questions using if-elif logic.
"""
def get_bot_response(message):
    """
    Returns a response based on user input.
    """
    message = message.lower().strip()

    if message == "hello":
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm ChatBot 1.0!"
    elif message == "help":
        return "You can say hello, ask how I am, or say bye to exit."
    elif message == "bye":
        return "Goodbye!"

    # 🔹 New Responses Added Below
    elif message == "what can you do":
        return "I can chat with you using simple rules. Try saying 'hello' or 'help'!"
    elif message == "who created you":
        return "I was created by a Python developer for an internship project!"
    elif message == "thank you":
        return "You're welcome!"

    else:
        return "I'm not sure how to respond to that."


def start_chatbot():
    """
    Starts the chatbot interaction loop.
    """
    print("🤖 Chatbot: Hello! Type something to chat. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").strip()
        response = get_bot_response(user_input)
        print("🤖 Chatbot:", response)

        if user_input.lower() == "bye":
            break


# Run chatbot
if __name__ == "__main__":
    start_chatbot()
