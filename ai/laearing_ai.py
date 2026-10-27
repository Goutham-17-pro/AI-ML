import ollama
model_name="llama3.2:3b"

response=ollama.generate(model=model_name,prompt="explain ai in one line")
print(response.response)