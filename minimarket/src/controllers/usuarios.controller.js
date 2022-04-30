import { Prisma } from "../prisma.js";
import { usuarioRequestDTO, loginRequestDTO } from "../dtos/usuarios.dto.js";
import { hashSync, compareSync } from "bcrypt";
import jsonwebtoken from "jsonwebtoken";

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
      const token = jsonwebtoken.sign(
        {
          id: usuarioEncontrado.id,
          mensaje: "API de Minimarket",
        },
        "asdfasdflkñjasdfjlkñasdfñjkl",
        { expiresIn: "1h" }
      );
      // el expiresIn recibe un numero (sera expresado en segundo) y si le pasamos un string:
      // '10' > 10 milisegundos
      // '1 days' > 1 dia
      // '1y' > 1 año
      // '7d' > 7 dias

      return res.json({
        message: "Bienvenido",
        content: token,
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
