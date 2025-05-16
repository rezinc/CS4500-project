# 💬 Helpdesk Chatbot with GPT4All

This project is a chatbot application that leverages local semantic search with FAISS and GPT4All to answer helpdesk-related queries based on internal documentation. The app features a React frontend and a FastAPI backend.

---

## 🚀 How to Execute the Project

### 1. 🔄 Clone the Repository

Start by cloning the repository and navigating into the project directory:

```bash
git clone https://github.com/rezinc/CS4500-project.git
cd CS4500-project
```

2. 🛠️ Environment Setup
Ensure you have Python 3.9+ installed.

Create and activate a virtual environment:

```bash
Copy code
python -m venv venv
# For Windows:
venv\Scripts\activate
# For Mac/Linux:
source venv/bin/activate
```
Install the required Python packages:

```bash
pip install -r requirements.txt
```
3. 🧠 Prepare the Vector Database
Make sure the following `.txt` files are in the root directory:

`duomfacleaned.txt`
`passwordscleaned.txt`
`spsscleaned.txt`

Then run the vector generation script:

```bash
python vector.py
```
This will create a `helpdesk_index/` directory containing the FAISS semantic vector index.

4. 🚦 Start the Backend Server
Ensure `main.py` and the GPT4All model file are in the same directory. Then run the FastAPI backend:

```bash
uvicorn main:app --reload
```
Your API will be live at:

👉 `http://127.0.0.1:8000`

5. 🌐 (Optional) Use Ngrok for Public Testing
If you need to access the backend remotely (e.g. from a different device or for a demo), use Ngrok:

```bash
ngrok http 8000
```
Copy the HTTPS URL provided by Ngrok, and update the Axios POST URL in `frontend/src/App.js` to match it, like:

```bash
https://your-ngrok-url.ngrok.io/chat
```
⚠️ Ngrok is optional. For local development, `http://127.0.0.1:8000` works fine.

6. 🎨 Run the Frontend (React)
Navigate into the `frontend` directory:

```bash
cd frontend
```

Install dependencies and start the React development server:

```bash
npm install
npm start
```
Make sure the Axios POST URL in `App.js` is set to your backend:

Local: `http://127.0.0.1:8000/chat`
Remote: Your Ngrok HTTPS URL
The chatbot will now be live at:

👉 `http://localhost:3000`

7. 🤖 Using the Chatbot
Open the chatbot interface in your browser and ask a question like:

“How do I install SPSS?”
“What if I forget my Duo app?”
“How can I reset my password?”

The chatbot will search your helpdesk documentation and provide relevant responses using GPT4All. 🧠💬
