import React, { useState } from 'react';
import axios from 'axios';  // Import axios for API calls
import './chatbot.css';

const App = () => {
    const [messages, setMessages] = useState([]);
    const [userInput, setUserInput] = useState('');
    const [loading, setLoading] = useState(false); // Manage loading state

    const handleSend = async () => {
        if (userInput.trim() === '') return; // Do nothing if the input is empty

        const userMessage = { text: userInput, sender: 'user' };
        setMessages([...messages, userMessage]);
        setUserInput('');
        setLoading(true); // Start loading state

        try {
            // Make sure the payload matches the backend's expected format
            const response = await axios.post('http://127.0.0.1:8000/chat', { input_text: userInput });
            const botMessage = { text: response.data.response, sender: 'bot' }; // Use 'response' here to match the backend response
            setMessages((prevMessages) => [...prevMessages, botMessage]);
        } catch (error) {
            console.error("Error connecting to backend:", error);
            const errorMessage = { text: "Error: Unable to reach the server.", sender: 'bot' };
            setMessages((prevMessages) => [...prevMessages, errorMessage]);
        }
        setLoading(false); // End loading state
    };

    return (
        <div className="container">
            <header>
                <div className="logo">
                    <img src="logo.png" alt="William Paterson IT Help Desk Logo" />
                    <p className="question-message">Have a question? Ask us here!</p>
                </div>
            </header>

            <main>
                <section className="chatbox">
                    <div className="chatbox-header">
                        <h2>IT Help Chat</h2>
                    </div>
                    <div className="chatbox-messages">
                        {messages.map((msg, index) => (
                            <div key={index} className={msg.sender === 'user' ? 'user-message' : 'bot-message'}>
                                {msg.text}
                            </div>
                        ))}
                    </div>
                    <div className="chatbox-input">
                        <input 
                            type="text" 
                            value={userInput} 
                            onChange={(e) => setUserInput(e.target.value)} 
                            placeholder="Type your message..."
                        />
                        <button onClick={handleSend} disabled={loading}>
                            {loading ? 'Sending...' : 'Send'}
                        </button>
                    </div>
                </section>
            </main>

            <footer>
                <p>Contact us at <strong>973-720-4357</strong> or <strong>help.wpunj.edu</strong></p>
            </footer>
        </div>
    );
};

export default App;
