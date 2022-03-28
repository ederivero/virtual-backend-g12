import React from 'react'
import register from '../register.svg'
export const Register = () => {
  return (
    <div className="login">
      <div className="div-login">
        <form action="POST" className="form-register">
          <label htmlFor="nombre">Nombre</label>
          <input type="text" name="" id="nombre" />

          <label htmlFor="apellido">Apellido</label>
          <input type="text" name="" id="apellido" />

          <label htmlFor="email">Email</label>
          <input type="email" name="" id="email" />

          <label htmlFor="password">Password</label>
          <input type="password" name="" id="password" />

          <label htmlFor="password2">Repita su password</label>
          <input type="password" name="" id="password2" />
          <button>Registrarse</button>
        </form>
      </div>
      <div style={{ display: 'flex' }}>
        <img src={register} alt="" width="90%" />
      </div>
    </div>
  )
}
