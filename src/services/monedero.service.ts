import axios from 'axios'
import { ICreateMovimiento, IGetMovimiento, IParams, IResponse } from '../interfaces'

const request = axios.create({ baseURL: process.env.REACT_APP_BACKEND_URL })

export const getMovimientos = (token: string, params: IParams) => {
  return request.get<IResponse<IGetMovimiento>>('/movimientos', {
    headers: { Authorization: `Bearer ${token}` },
    params,
  })
}

export const crearMovimiento = (data: ICreateMovimiento, token: string) => {
  return request.post('/movimiento', data, { headers: { Authorization: `Bearer ${token}` } })
}
