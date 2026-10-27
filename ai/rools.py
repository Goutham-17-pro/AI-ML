import ollama

messages=[
    {
        "role":"system",
        "content":"you are ansser like a  strict college professor , explain in bulet points ai in one line",
    },
    
     {
        "role":"user",
        "content":"what is ai?"
      }
]

model_name="llama3.2:3b"

response=ollama.chat(model=model_name,messages=messages)
print(response.message.content)