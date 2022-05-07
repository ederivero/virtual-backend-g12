import bcryptjs from "bcryptjs";
import { Usuario } from "../models/usuarios.models.js";
import jwt from "jsonwebtoken";

export const registrarUsuario = async (req, res) => {
  // creare mi DTO de registro
  const data = req.body;
  try {
    // cuando usamos una sentencia de busqueda, creacion o actualizacion o eliminacion esta retornara una serie de informacion que 'visiblemente' solo se vera el '_doc' que sera la informacion que se mostrara tanto en consola como en el postman, entonces
    const nuevoUsuario = await Usuario.create(data);

    // el metodo toJSON() solamente devolvera la informacion que retorna de la bd (sin las otras llaves que usa mongoose para trabajo interno)
    console.log(nuevoUsuario.toJSON());
    console.log(Object.keys(nuevoUsuario));

    // Forma 1 de eliminar un atributo del JSON
    const result = nuevoUsuario.toJSON();

    delete result["password"];

    // Forma 2 de eliminar un atributo del JSON
    delete nuevoUsuario["_doc"]["password"];

    return res.status(201).json({
      message: "Usuario creado exitosamente",
      content: result, // nuevoUsuario
    });
  } catch (e) {
    return res.status(400).json({
      message: "Error al crear el usuario",
      content: e.message,
    });
  }
};

export const login = async (req, res) => {
  // validar que se envie la pwd y el correo
  const data = req.body;
  // primero busco el usuario en la bd
  const usuarioEncontrado = await Usuario.findOne({ correo: data.correo });

  if (!usuarioEncontrado) {
    return res.status(400).json({
      message: "Credenciales incorrectas",
    });
  }
  // valido su pwd
  if (bcryptjs.compareSync(data.password, usuarioEncontrado.password)) {
    const token = jwt.sign(
      { _id: usuarioEncontrado._id },
      process.env.JWT_SECRET,
      {
        expiresIn: "1h",
      }
    );

    return res.json({
      message: "Bienvenido",
      content: token,
    });
  } else {
    return res.status(400).json({
      message: "Credenciales incorrectas",
    });
  }
};
