import { Usuario } from "../models/usuarios.models.js";

export const registrarUsuario = async (req, res) => {
  // creare mi DTO de registro
  const data = req.body;
  try {
    const nuevoUsuario = await Usuario.create(data);

    return res.status(201).json({
      message: "Usuario creado exitosamente",
      content: nuevoUsuario,
    });
  } catch (e) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: e.message,
    });
  }
};
