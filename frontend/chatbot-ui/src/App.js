import React, { useState } from "react";
import axios from "axios";

function App() {
    const [query, setQuery] = useState(""); // To store user input
    const [response, setResponse] = useState(""); // To store chatbot response
    const [loading, setLoading] = useState(false); // To manage loading state

    // Function to handle the API call when user submits a query
    const sendQuery = async () => {
        setLoading(true); // Start loading
        try {
            // Send input to FastAPI backend and get response
            const res = await axios.post("http://127.0.0.1:8000/chat", { input_text: query });
            setResponse(res.data.response); // Update state with the response
        } catch (error) {
            console.error("Error in sending query:", error);
            setResponse("Error: Could not fetch response."); // Error message if the request fails
        }
        setLoading(false); // End loading
    };

    return (
        <div style={styles.container}>
            <h1 style={styles.header}>Helpdesk Chatbot</h1>
            <input 
                style={styles.input} 
                type="text" 
                value={query} 
                onChange={(e) => setQuery(e.target.value)} 
                placeholder="Ask me a question!" 
            />
            <button 
                style={styles.button} 
                onClick={sendQuery}
                disabled={loading} // Disable button while loading
            >
                {loading ? "Loading..." : "Ask"}
            </button>
            {response && <p style={styles.response}>{response}</p>}
        </div>
    );
}

// Simple styles for the chatbot interface
const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        marginTop: "50px",
        fontFamily: "Arial, sans-serif",
    },
    header: {
        fontSize: "2rem",
        marginBottom: "20px",
    },
    input: {
        padding: "10px",
        fontSize: "1rem",
        width: "300px",
        marginBottom: "20px",
        borderRadius: "5px",
        border: "1px solid #ccc",
    },
    button: {
        padding: "10px 20px",
        fontSize: "1rem",
        backgroundColor: "#4CAF50",
        color: "white",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
    },
    response: {
        marginTop: "20px",
        fontSize: "1.2rem",
        color: "#333",
        fontStyle: "italic",
    }
};

export default App;
