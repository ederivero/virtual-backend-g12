import React, { useState } from "react";
import registerImage from "../register.svg";
import { register } from "../services/auth.service";
import axios from "axios";

export const Register = () => {
  const [form, setForm] = useState<{
    nombre: string;
    apellido: string;
    email: string;
    password: string;
    repeatPassword: string;
  }>({
    nombre: "",
    apellido: "",
    email: "",
    password: "",
    repeatPassword: "",
  });

  const registrarUsuario = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (form.password !== form.repeatPassword) {
      alert("Las contraseñas no coinciden!");
    } else {
      try {
        const { data } = await register({
          apellido: form.apellido,
          correo: form.email,
          nombre: form.nombre,
          password: form.password,
        });
        console.log(data);
      } catch (e) {
        if (axios.isAxiosError(e)) {
          console.log(e.response?.data);
          console.log(e.response);
        }
      }
    }
  };

  return (
    <div className="login">
      <div className="div-login">
        <form
          action="POST"
          className="form-register"
          onSubmit={registrarUsuario}
        >
          <label htmlFor="nombre">Nombre</label>
          <input
            type="text"
            name=""
            id="nombre"
            value={form.nombre}
            onChange={(e) =>
              setForm((preValue) => ({ ...preValue, nombre: e.target.value }))
            }
          />

          <label htmlFor="apellido">Apellido</label>
          <input
            type="text"
            name=""
            id="apellido"
            value={form.apellido}
            onChange={(e) =>
              setForm((preValue) => ({ ...preValue, apellido: e.target.value }))
            }
          />

          <label htmlFor="email">Email</label>
          <input
            type="email"
            name=""
            id="email"
            value={form.email}
            onChange={(e) =>
              setForm((preValue) => ({ ...preValue, email: e.target.value }))
            }
          />

          <label htmlFor="password">Password</label>
          <input
            type="password"
            name=""
            id="password"
            value={form.password}
            onChange={(e) =>
              setForm((preValue) => ({ ...preValue, password: e.target.value }))
            }
          />

          <label htmlFor="password2">Repita su password</label>
          <input
            type="password"
            name=""
            id="password2"
            value={form.repeatPassword}
            onChange={(e) =>
              setForm((preValue) => ({
                ...preValue,
                repeatPassword: e.target.value,
              }))
            }
          />
          <button>Registrarse</button>
        </form>
      </div>
      <div style={{ display: "flex" }}>
        <img src={registerImage} alt="" width="90%" />
      </div>
    </div>
  );
};
