from google import genai
client = genai.Client()
with open('document2.txt','r') as file:
    file_contant = file.read()
chat = client.chats.create(model='gemini-2.5-flash',config={'system_instruction': 'Act as a asistant and use the information ropvite in the document to answer the questons'})
chat.send_message(f"here is the document you need to use \n {file_contant}")
while True:
    user_input=input("You : ")
    if user_input.lower() == 'quit':
        break
    response = chat.send_message(user_input)
    print(f'Gemini: {response.text}')