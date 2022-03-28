import React, { createContext, Dispatch, SetStateAction, useState } from 'react'

export const userContext = createContext<{ data?: string; setData?: Dispatch<SetStateAction<string>> }>({})

export const UserContextProvider = ({ children }: any) => {
  const [data, setData] = useState(localStorage.getItem('token') ?? '')

  return <userContext.Provider value={{ data, setData }} children={children} />
}
