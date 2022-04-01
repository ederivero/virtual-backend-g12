import React, { useCallback, useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import {
  validarTokenPasswordReset,
  chagePassword,
} from "../services/auth.service";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export const ResetPassword = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const token = searchParams.get("token");
  const [valido, setValido] = useState(true);
  const [correo, setCorreo] = useState("");
  const [passwords, setPasswords] = useState({
    password: "",
    validatePassword: "",
  });

  const validezToken = useCallback(async () => {
    if (token) {
      try {
        const { data } = await validarTokenPasswordReset({
          token,
        });
        setCorreo(data.content.correo);
        setValido(true);

        console.log(data);
      } catch (error) {
        if (axios.isAxiosError(error)) {
          console.log(error.response?.data);
          setValido(false);
        }
      }
    }
  }, [token]);

  useEffect(() => {
    validezToken();
  }, [validezToken]);

  const cambiarPwd = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (passwords.password === passwords.validatePassword && token) {
      try {
        const { data } = await chagePassword({
          password: passwords.password,
          token,
        });
        navigate("/login");
        if (data) {
        }
      } catch (error) {
        if (axios.isAxiosError(error)) {
          console.log(error.toJSON());
        }
      }
    }
  };

  return token && valido ? (
    <div>
      <p>
        Hola <span style={{ color: "#893abd" }}>{correo}</span> ingresa tu nueva
        contraseña:
      </p>
      <form action="POST" onSubmit={cambiarPwd}>
        <label htmlFor=""></label>
        <input
          type="password"
          value={passwords.password}
          onChange={(e) =>
            setPasswords((preVal) => ({ ...preVal, password: e.target.value }))
          }
        />
        <label htmlFor=""></label>
        <input
          type="password"
          value={passwords.validatePassword}
          onChange={(e) =>
            setPasswords((preVal) => ({
              ...preVal,
              validatePassword: e.target.value,
            }))
          }
        />
        <button>Cambiar password</button>
      </form>
    </div>
  ) : (
    <div>Token incorrecta</div>
  );
};
