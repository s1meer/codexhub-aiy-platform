import React, { useState } from "react";
import Editor from "@monaco-editor/react";
import axios from "axios";
import "./App.css";

function App() {
  const [code, setCode] = useState("// Start building your next-gen app here...");
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const askGemini = async () => {
    try {
      const res = await axios.post("http://127.0.0.1:5000/api/gemini", { prompt });
      setResponse(res.data.response || "No response received.");
    } catch (err) {
      setResponse("Error: " + err.message);
    }
  };

  return (
    <div className="container">
      <header>
        <h1>🧠 CodexHub AI IDE</h1>
        <p className="subtitle">Your personal AI-powered development workspace</p>
      </header>

      <main className="main-section">
        <div className="editor-box">
          <Editor
            height="400px"
            language="javascript"
            value={code}
            onChange={setCode}
            theme="vs-dark"
          />
        </div>

        <div className="ai-box">
          <textarea
            rows={4}
            placeholder="💡 Ask Gemini something..."
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
          />
          <button onClick={askGemini}>Ask Gemini 🤖</button>
          <pre className="response-box">{response}</pre>
        </div>
      </main>
    </div>
  );
}

export default App;
