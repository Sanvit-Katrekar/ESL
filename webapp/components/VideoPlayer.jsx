// src/components/VideoPlayer.jsx
import React from 'react';

const VideoPlayer = ({ videoSource }) => {
  return (
    <div>
      <video width="640" height="360" controls>
        <source src={videoSource} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default VideoPlayer;
