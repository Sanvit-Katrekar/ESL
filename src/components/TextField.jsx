// src/components/TextField.jsx
import React from 'react';

const TextField = ({ onChange }) => {
  return (
    <input
      type="text"
      placeholder="Enter text here..."
      onChange={onChange}
    />
  );
};

export default TextField;
