import React, { useState } from 'react';

function Login() {
  const [message, setMessage] = useState('');

  async function handleCheckUsername() {
    const username = document.getElementById("usernameInput").value;
    
    if (!username) {
      setMessage('Please enter a username');
      return;
    }

    try {
      const response = await fetch(`http://127.0.0.1:8000/search/check/?username=${username}`);
      const data = await response.json();
      setMessage(data.taken ? 'Username is taken' : 'Username is available');
    } catch {
      setMessage("Error checking username");
    }
  }

  return (
    <div>
      <input id="usernameInput" placeholder="Enter Username" />
      <p>{message}</p>
      <button onClick={handleCheckUsername}>Check Username</button>
    </div>
  );
}

export default Login;
