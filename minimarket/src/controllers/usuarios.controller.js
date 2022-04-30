import { Prisma } from "../prisma.js";
import { usuarioRequestDTO, loginRequestDTO } from "../dtos/usuarios.dto.js";
import { hashSync, compareSync } from "bcrypt";
import jsonwebtoken from "jsonwebtoken";
import { enviarCorreoValidacion } from "../utils/sendMail.js";
import cryptojs from "crypto-js";

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

    // Crear un texto encriptado
    const hash = cryptojs.AES.encrypt(
      JSON.stringify({
        nombre: nuevoUsuario.nombre,
        email: nuevoUsuario.email,
      }),
      process.env.LLAVE_ENCRIPTACION
    ).toString();

    await enviarCorreoValidacion({
      destinatario: nuevoUsuario.email,
      hash,
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
        process.env.JWT_SECRET,
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

export const confirmarCuenta = async (req, res) => {
  // TODO crear el DTO de la confirmacion de la cuenta
  // const data = confirmarCuentaRequestDTO(req.body)
  try {
    const data = req.body;
    // aca desencripto el hash con la misma contraseña que use para encriptar
    const informacion = JSON.parse(
      cryptojs.AES.decrypt(data.hash, process.env.LLAVE_ENCRIPTACION).toString(
        cryptojs.enc.Utf8
      )
    );

    console.log(informacion);

    // De acuerdo a esa informacion :
    // 1. buscar el usuario en la bd con su correo y que su "validado" sea false, si es true indicar que el usuario ya valido su cuenta (400)

    // SELECT id FROM usuarios WHERE email = '...' and validado=false;
    // findUnique > para hacer busquedas con columnas que son unique | indices de la tabla
    // findFirst > me devolver la primera coincidencia con condicionales a cualquier columna sin que sea unique's
    const usuarioEncontrado = await Prisma.usuario.findFirst({
      where: {
        email: informacion.email,
        validado: false,
      },
      select: {
        id: true,
      },
    });

    if (!usuarioEncontrado) {
      throw new Error("El usuario ya fue validado");
    }

    // 2. actualizar el estado validado a true
    // UPDATE usuarios SET validado=true WHERE id= '...';
    await Prisma.usuario.update({
      where: { id: usuarioEncontrado.id },
      data: { validado: true },
    });

    return res.json({
      message: "Cuenta validada correctamente",
    });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(400).json({
        message: "Error al validar la cuenta",
        content: error.message,
      });
    }
  }
};

// controlador protegido (recibira una JWT)
export const perfil = async (req, res) => {
  console.log(req.user);

  return res.json({
    message: "Bienvenido",
    content: req.user,
  });
};
