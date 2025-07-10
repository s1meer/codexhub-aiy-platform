import { useState } from 'react'
import './App.css'

function App() {
  const [inputValue, setInputValue] = useState('')
  const [result, setResult] = useState('')

  const handleSubmit = async () => {
    const fileContent = inputValue.trim()
    const response = await fetch(`${import.meta.env.VITE_API_URL}/api/files/create`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: 'index.js', content: fileContent })
    })

    const data = await response.json()
    setResult(data.message || 'Saved')
  }

  return (
    <div style={{ padding: '2rem', color: 'white' }}>
      <h1>CodexHub AI IDE</h1>
      <textarea
        style={{ width: '400px', height: '200px', background: '#1e1e1e', color: 'lime', padding: '10px' }}
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        placeholder='// Start coding...'
      />
      <br /><br />
      <button onClick={handleSubmit}>Ask Gemini</button>
      <div style={{ marginTop: '1rem' }}>{result}</div>
    </div>
  )
}

export default App
