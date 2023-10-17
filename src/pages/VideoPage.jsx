// src/pages/VideoPage.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TextField from '../components/TextField';
import VideoPlayer from '../components/VideoPlayer';

const VideoPage = () => {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const videoSource = '/music.mp4';

  const handleTextChange = (e) => {
    setText(e.target.value);
  };

  const handleSubmit = () => {
    setLoading(true);

    // Simulate an asynchronous operation (e.g., API call)
    setTimeout(() => {
      setLoading(false);
      // Navigate to the video page
    }, 2000);
  };

  return (
    <div style={pageStyles}>
      <TextField onChange={handleTextChange} />
      <button style={buttonStyles} onClick={handleSubmit}>
        Submit
      </button>
      {loading && <div style={loadingStyles}>Loading...</div>}
      <VideoPlayer videoSource={videoSource} />
      <Link to="/">
        <button style={buttonStyles}>Generate Again</button>
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
};

const buttonStyles = {
  backgroundColor: '#4CAF50',
  color: 'white',
  padding: '10px 20px',
  fontSize: '16px',
  cursor: 'pointer',
  margin: '10px',
};

const loadingStyles = {
  fontSize: '20px',
  marginTop: '20px',
};

export default VideoPage;
