// src/App.tsx
import React, { useEffect, useState } from 'react';
import './App.css';
import { DefaultService } from './api/services/DefaultService';
import type { DTO_CreateBurger } from './api/models/DTO_CreateBurger';
import { OpenAPI } from './api/core/OpenAPI';

OpenAPI.BASE = 'http://127.0.0.1:8000'; // your backend API

function App() {
  const [burgers, setBurgers] = useState<DTO_CreateBurger[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function fetchBurgers() {
      setLoading(true);
      setError(null);
      try {
        const response = await DefaultService.getAllBurgersBurgersGet(0, 10);
        // Assuming response is an array of burgers
        setBurgers(response);
      } catch (err: any) {
        console.error('Failed to fetch burgers:', err);
        setError('Failed to fetch burgers. Check your backend or CORS.');
      } finally {
        setLoading(false);
      }
    }

    fetchBurgers();
  }, []);

  if (loading) return <p>Loading burgers...</p>;
  if (error) return <p style={{ color: 'red' }}>{error}</p>;

  return (
    <div className="App">
      <header className="App-header">
        <h1>Burger List</h1>
        <ul>
          {burgers.map((burger, index) => (
            <li key={index}>
              <strong>{burger.name}</strong>
              <br />
              Description: {burger.description}
            </li>
          ))}
        </ul>
      </header>
    </div>
  );
}

export default App;