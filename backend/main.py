from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gpt4all import GPT4All
from fastapi.middleware.cors import CORSMiddleware

from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings

app = FastAPI()

# Enable CORS (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define paths
model_path = "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf"
db_folder = "helpdesk_index"  # Path to your FAISS .db folder

# Input and output schemas
class Query(BaseModel):
    input_text: str

class ChatResponse(BaseModel):
    response: str

# Global model and retriever
gpt4all_model = None
retriever = None

@app.on_event("startup")
async def load_resources():
    global gpt4all_model, retriever
    try:
        print("Loading GPT4All model...")
        gpt4all_model = GPT4All(model_path)

        print("Loading FAISS vector database...")
        embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        db = FAISS.load_local(db_folder, embedding_model, allow_dangerous_deserialization=True)
        retriever = db.as_retriever()

        print("Resources loaded successfully.")
    except Exception as e:
        raise RuntimeError(f"Startup failed: {e}")

@app.post("/chat", response_model=ChatResponse)
async def chat(query: Query):
    try:
        user_input = query.input_text

        # Step 1: Retrieve context from FAISS DB
        results = retriever.get_relevant_documents(user_input)
        context = "\n\n".join([doc.page_content for doc in results])

        # Step 2: Create full prompt
        prompt = f"""You are a helpful IT helpdesk assistant. Use the following helpdesk knowledge to answer the question.

Helpdesk Knowledge:
{context}

User Question: {user_input}
Answer:"""

        # Step 3: Generate response from GPT4All
        response = gpt4all_model.generate(prompt)
        return {"response": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
