import axios from 'axios'
import { ILogin, IRegister } from '../interfaces'

const request = axios.create({ baseURL: process.env.REACT_APP_BACKEND_URL })

export const login = (data: ILogin) => {
  return request.post('/login', data)
}

export const register = (data: IRegister) => {
  return request.post('/register', data)
}
