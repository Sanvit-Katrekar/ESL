// src/pages/HomePage.js
import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div style={pageStyles}>
      <h1 style={titleStyles}>Marhaba</h1>
      <Link to="/text">
        <button style={buttonStyles}>Click Here</button>
      </Link>
    </div>
  );
};

const pageStyles = {
  textAlign: 'center',
  padding: '20px',
  backgroundColor: '#add8e6', // Light Blue
  height: '100vh',
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
};

const titleStyles = {
  color: '#333',
};

const buttonStyles = {
  backgroundColor: '#4CAF50',
  color: 'white',
  padding: '10px 20px',
  fontSize: '16px',
  cursor: 'pointer',
};

export default HomePage;
