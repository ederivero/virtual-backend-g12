import React, { useCallback, useContext, useState } from 'react'
import { userContext } from '../context/userContext'
import { IGetMovimiento } from '../interfaces'
import { getMovimientos } from '../services/monedero.service'

export const Monedero = () => {
  const { data: token } = useContext(userContext)
  const [movimientos, setMovimientos] = useState<Array<IGetMovimiento>>([])

  const getData = useCallback(async () => {
    console.log('entro')

    if (token) {
      const { data } = await getMovimientos(token, {})
      setMovimientos(data.content)
    }
  }, [token])

  useCallback(() => {
    getData()
  }, [getData])

  return (
    <div>
      <h1>Monedero</h1>
      {movimientos.map((movimiento) => (
        <div key={movimiento.id}>MOVIMIENTO</div>
      ))}
    </div>
  )
}
