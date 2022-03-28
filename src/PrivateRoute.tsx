import React, { useContext } from 'react'
import { Navigate } from 'react-router-dom'
import { userContext } from './context/userContext'

export default function PrivateRoute({ children }: { children: React.ReactElement }) {
  const { data } = useContext(userContext)

  return data ? children : <Navigate to={'/'} />
}
