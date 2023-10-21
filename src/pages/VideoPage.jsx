// src/pages/VideoPage.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import TextField from '../components/TextField';
import VideoPlayer from '../components/VideoPlayer';
import { makeGet, makePost } from '../server_functions/request';
import VideoInput from '../components/Dropzone';
const VideoPage = () => {
  const [text, setText] = useState('');
  const [loading, setLoading] = useState(false);
  const [videoSource, setVideoSource] = useState('/bruhh.mp4');

  const handleTextChange = (e) => {
    setText(e.target.value);
    console.log(text);
  };

async function handleSubmit() {
    setLoading(true);
    makePost(text).then((data)=>{
     
      //console.log("images: " + data)
      setVideoSource(data);
      setLoading(false);
    })
    
  };

  return (
    <div style={pageStyles}>
      <div style={leftContainerStyles}>
        <div style={innerContainerStyles}>
          <h2 style={titleStyles}>Sign Language Chat Assistant</h2>
        
          <h5 style={descriptionStyles}>Get Started with: </h5>
          <h7 style={descriptionStyles}>Looking for images , Getting new Ideas , or Planning your Day </h7>
        
          <div style={textInputContainerStyles}>
            <TextField onChange={handleTextChange} />
            
            {/*<MyUploader/>*/}
            <button style={submitButtonStyles} onClick={handleSubmit}>
              ASK
            </button>
          </div>
          {loading && <div style={loadingStyles}>Loading...</div>}
          
        </div>
      </div>
      <div style={rightContainerStyles}>
        {/*<VideoPlayer videoSource={videoSource} />*/}
        <VideoInput width={400} height={300}/>
      </div>
    </div>
  );
};

const pageStyles = {
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'space-around',
  textAlign: 'center',
  padding: '20px',
  backgroundColor: '#add8e6', // Light Blue
  height: '100vh',
};

const leftContainerStyles = {
  flex: 1,
  background: '#fff8dc',
  borderRadius: '20px', // Rounded corners
  padding: '20px',
  height: '500px',
};

const innerContainerStyles = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
};

const rightContainerStyles = {
  flex: 1,
};

const titleStyles = {
  color: '#333',
  fontSize: '36px', // Increased font size
  fontFamily: 'Verdana, sans-serif', // Custom font
  marginBottom: '10px',
  fontWeight: 'bold', // Added bold style
};

const descriptionStyles = {
  color: '#555',
  fontSize: '18px', // Increased font size
  fontFamily: 'Arial, sans-serif', // Custom font
  marginBottom: '5px',
};

const textInputContainerStyles = {
  display: 'flex',
  alignItems: 'center',
};

const submitButtonStyles = {
  backgroundColor: '#4CAF50',
  color: 'white',
  marginLeft: '10px', // Added margin between text input and submit button
  padding: '10px 20px',
  fontSize: '16px',
  cursor: 'pointer',
  borderRadius: '15px', // Rounded corners
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
