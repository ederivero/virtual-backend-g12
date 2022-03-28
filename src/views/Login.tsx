import React, { useContext, useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { Button } from '../components/Button/Button'
import { userContext } from '../context/userContext'
import { login } from '../services/auth.service'
import axios from 'axios'
import logo from '../login.svg'

export const Login = () => {
  const { data, setData } = useContext(userContext)
  const navigate = useNavigate()
  const [form, setForm] = useState<{ correo: string; password: string }>({ correo: '', password: '' })
  useEffect(() => {
    if (data) {
      navigate('/monedero')
    }
  }, [data, navigate])

  const makeRequest = async (e: React.MouseEvent<HTMLFormElement, MouseEvent>) => {
    e.preventDefault()
    try {
      const {
        data: { token },
      } = await login(form)
      if (token) {
        localStorage.setItem('token', token)
        setData && setData(token)
        navigate('/monedero')
      }
      console.log(data)
    } catch (error) {
      if (axios.isAxiosError(error)) {
        console.log(error.response?.status)
      }
    }
  }

  return (
    <div className="login">
      <div className="div-login">
        <form action="POST" className="form-login" onClick={makeRequest}>
          <label htmlFor="email">Email</label>
          <input
            type="email"
            name=""
            id="email"
            onChange={(e) => setForm((preVal) => ({ ...preVal, correo: e.target.value }))}
          />

          <label htmlFor="password">Password</label>
          <input
            type="password"
            name=""
            id="password"
            onChange={(e) => setForm((preVal) => ({ ...preVal, password: e.target.value }))}
          />

          <Button text="Iniciar sesion" backgroundColor="#2d91ca" />
          <p>
            No tienes cuenta? Crea una <Link to={'/register'}>aqui</Link>
          </p>
        </form>
      </div>
      <div style={{ display: 'flex' }}>
        <img src={logo} alt="" width="100%" />
      </div>
    </div>
  )
}
