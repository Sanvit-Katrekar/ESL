"use client"
import React from 'react'
import Link from 'next/link'
export default function Home() {
  return (
    <><div style={{
      textAlign: 'center',
      padding: '20px',
      backgroundColor: '#add8e6', // Light Blue
      height: '100vh',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
    }}>
    <h1 style={{ color: '#333'}}>Marhaba</h1>
    <Link href={"/components/dashboard/"}>
                  <button style={{
                  backgroundColor: '#4CAF50',
                  color: 'white',
                  padding: '10px 20px',
                  fontSize: '16px',
                  cursor: 'pointer',
                }}>Click Here</button>
      </Link>
  </div></>
  )
}



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