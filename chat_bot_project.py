import ollama 

message = [{"role": "system", "content": "you are a frindly assistant ."}]
model_name="llama3.2:3b"

while True:
    user_prompt=input("You: ") 
    user_role={"role":"user", "content": user_prompt}
    if user_prompt == "bye":
        break
    
               
    message.append(user_role)

    response =ollama.chat(model=model_name,messages=message)
    response =response.message.content
    print("Assistant:",response)

    assistant_role={"role":"assistant", "content": response}
