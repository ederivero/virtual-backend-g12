import jwt from "jsonwebtoken";
import { Usuario } from "../models/usuarios.models.js";

export const validarToken = async (req, res, next) => {
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "Se necesita una token para realizar esta peticion",
    });
  }
  // Bearer 123123.123123.123123123
  const token = req.headers.authorization.split(" ")[1];

  if (!token) {
    return res.status(401).json({
      message: "Formato de token no valido",
    });
  }

  try {
    const { _id } = jwt.verify(token, process.env.JWT_SECRET);

    const usuarioEncontrado = await Usuario.findById(_id);

    if (!usuarioEncontrado) {
      throw Error("Usuario no existe");
    }

    req.user = usuarioEncontrado;

    next();
  } catch (error) {
    return res.status(401).json({
      message: "Error en la token",
      content: error.message,
    });
  }
};
