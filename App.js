import React, { useState, useEffect } from 'react';
import axios from 'axios';
import LoginComponent from './LoginComponent';
import DashboardComponent from './DashboardComponent';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    // Check if user is logged in
    // If logged in, fetch user data
    // If not, redirect to login page
  }, []);

  const handleLogin = (userData) => {
    // Handle user login
  };

  const handleLogout = () => {
    // Handle user logout
  };

  return (
    <div className="App">
      {user ? (
        <DashboardComponent user={user} onLogout={handleLogout} />
      ) : (
        <LoginComponent onLogin={handleLogin} />
      )}
    </div>
  );
}

export default App;
        
