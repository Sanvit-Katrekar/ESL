// src/components/TextField.jsx
import React from 'react';

const TextField = ({ onChange }) => {
  return (
    <div style={textFieldContainerStyles}>
      <input
        type="text"
        placeholder="Enter text here..."
        onChange={onChange}
        style={textFieldStyles}
      />
    </div>
  );
};

const textFieldContainerStyles = {
  display: 'flex',
  alignItems: 'center',
};

const textFieldStyles = {
  padding: '10px',
  fontSize: '16px',
  border: '2px solid #ddd', // Light Gray border
  borderRadius: '15px', // Rounded corners
  margin: '10px 0',
  width: 'calc(100% + 400px)', // Adjusted width to accommodate the button
  boxSizing: 'border-box', // Include padding and border in the width
};

const audioButtonStyles = {
  background: '#4CAF50', // Green color
  color: 'white',
  border: 'none',
  borderRadius: '50%', // Round button
  marginLeft: '3px', // Leave a 3px gap between the button and the text field
  marginRight: '10px', // Added gap between the button and text field
  cursor: 'pointer',
  padding: '10px',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
};

const audioIconStyles = {
  fontSize: '20px',
};

export default TextField;
