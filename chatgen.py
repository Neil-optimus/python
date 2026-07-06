from google import genai
client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash',config={'system_instruction':'You are a friendly and helpful coding tutor.Explain concepts clearly and simply, and provide small code examples.'})
print("Start Chating! Type quit to end chat")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")