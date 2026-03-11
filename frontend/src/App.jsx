import { useState } from 'react';
import LoginScreen from './components/LoginScreen';
import Dashboard from './components/Dashboard';

export default function App() {
  const [session, setSession] = useState(null); // Stores { code, userProfile }

  const handleLogin = (code, profile) => {
    setSession({ code, profile });
  };

  return (
    <div className="min-h-screen bg-cyber-black text-white font-sans selection:bg-neon-blue selection:text-black">
      {!session ? (
        <LoginScreen onLogin={handleLogin} />
      ) : (
        <Dashboard userProfile={session.profile} />
      )}
    </div>
  );
}