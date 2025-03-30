from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gpt4all import GPT4All
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for all origins (adjust in production for security)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, OPTIONS, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Define model path
model_path = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"

# Initialize the GPT4All model at startup
@app.on_event("startup")
async def load_model():
    global gpt4all_model
    try:
        gpt4all_model = GPT4All(model_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load GPT4All model on startup: {e}")

# Define the input model
class Query(BaseModel):
    input_text: str

# Define the response model
class ChatResponse(BaseModel):
    response: str

# Define the chat endpoint
@app.post("/chat")
async def chat(query: Query):
    try:
        response = gpt4all_model.generate(query.input_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
