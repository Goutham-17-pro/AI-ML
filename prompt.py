import ollama

#1 role 
system_role_content = "you are a wildlife travel writer for south India travel blog ."

#2 Task
user_role_content = "write an instuction to karnataka's wildlife for first-time visiter."


#3 constraints

#4 format

#5 examples

messeges = [
    {
        "role": "system",
        "content":system_role_content
    },

    {
        "role": "user",
        "content":user_role_content
    }            
]

model_name = "llama3.2:3b"

response=ollama.chat(model=model_name,messeges=messeges)

print(response.messege)

