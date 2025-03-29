from fastapi import FastAPI
from gpt4all import GPT4All

app = FastAPI()

# Load GPT4ALL model
model = GPT4All("C:/Users/Jack/gpt4all/Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf")

@app.get("/")
def home():
    return {"message": "Chatbot API is running"}

@app.post("/chat")
async def chat(input_text: str):
    response = model.generate(input_text)
    return {"response": response}