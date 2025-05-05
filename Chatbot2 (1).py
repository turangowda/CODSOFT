def Chatbot():
    print("Hello! I am a simple Chatbot.Type'quit' to exit.")

    while True:
        user_input = input("you:").lower()

        if user_input == 'quit':
            print("Goodbye! Have a great day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello Boss! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I am just a bot, I dont have any feelings! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I am a bot I dont have any name. Perhaps you can call me accoding to your wish!.")
        elif "Help" in user_input:
            print("Chatbot: Sure! I can help you with basic queries. Ask me something like 'How are you?' or 'What's your name?'")
        elif "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! See you later!.")
        elif "are you ok with the name" in user_input:
            print("Chatbot: Wow! that's a good name. I am ok with it.")  
        else:
            print("Chatbot: Sorry, I dont understand that. Can you ask me something else?")


#Start the chatbot
Chatbot()            


            
