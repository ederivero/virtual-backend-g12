import React from 'react'

export const Button = ({ text, backgroundColor }: { text: string; backgroundColor?: string }) => {
  return <button style={{ backgroundColor, borderRadius: '10px', padding: '10px', border: '0' }}>{text}</button>
}
