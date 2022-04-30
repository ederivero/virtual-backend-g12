import { Prisma } from "../prisma.js";
import { usuarioRequestDTO, loginRequestDTO } from "../dtos/usuarios.dto.js";
import { hashSync, compareSync } from "bcrypt";

export const crearUsuario = async (req, res) => {
  try {
    const data = usuarioRequestDTO(req.body);
    const password = hashSync(data.password, 10);

    const nuevoUsuario = await Prisma.usuario.create({
      data: { ...data, password },
      select: {
        id: true,
        nombre: true,
        email: true,
        rol: true,
        validado: true,
      },
    });

    return res.status(201).json(nuevoUsuario);
  } catch (error) {
    // La clase error tiene el atributo message
    // Yo valido si una instancia es de una clase o no
    if (error instanceof Error) {
      return res.status(400).json({
        message: "Error al crear el usuario",
        content: error.message,
      });
    }
    // typeof error Instance
  }
};

export const login = async (req, res) => {
  try {
    const data = loginRequestDTO(req.body);
    // buscar el usuario en la bd que tenga ese correo
    const usuarioEncontrado = await Prisma.usuario.findUnique({
      where: { email: data.email },
      rejectOnNotFound: true,
    });

    // validar su password
    //              Welcome123!    askldjasdf0as9iudf09sdvcasiojhdvoasijfoais
    if (compareSync(data.password, usuarioEncontrado.password)) {
      return res.json({
        message: "Bienvenido",
      });
    } else {
      // si no es la password emitire un error
      // raise new Exception('credenciales incorrectas')
      throw Error("Credenciales incorrectas");
    }
  } catch (error) {
    if (error instanceof Error) {
      return res.status(400).json({
        message: "Error la hacer el inicio de sesion",
        content: error.message,
      });
    }
  }
};
