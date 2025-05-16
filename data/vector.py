from langchain.vectorstores import FAISS
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document

# Prepare your helpdesk data
texts = [
    Document(page_content=open("duomfacleaned.txt", "r").read()),
    Document(page_content=open("passwordscleaned.txt", "r").read()),
    Document(page_content=open("spsscleaned.txt", "r").read())
]

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(texts)

# Embed and save vector DB
embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.from_documents(docs, embedding)
db.save_local("helpdesk_index")
