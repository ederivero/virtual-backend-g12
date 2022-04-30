import jsonwebtoken from "jsonwebtoken";
import { Prisma } from "../prisma.js";

export async function verificarToken(req, res, next) {
  // middleware
  // es un intermediario que sirve para hacer una validacion previa antes del controlador final
  if (!req.headers.authorization) {
    return res.status(401).json({
      message: "Se necesita una token para realizar esta peticion",
    });
  }
  try {
    // recibire en el authorizacion lo siguiente: "Bearer asdasda.sdfasdfasdfa.asdfasdfasdf"
    const token = req.headers.authorization.split(" ")[1];
    // si la pwd es incorrecta, la token caduco o la token esta mal formateada emitira un error
    const payload = jsonwebtoken.verify(token, process.env.JWT_SECRET);

    // si la token fue verificada correctamente nos devolvera el payload en el cual hemos guardado el id del usuario, ahora buscaremos ese usuario en la bd
    const usuarioEncontrado = await Prisma.usuario.findUnique({
      where: { id: payload.id },
      rejectOnNotFound: true,
    });

    // ahora agregar al json del Request el usuario para que pueda ser utilizado en los demas controladores
    req.user = usuarioEncontrado;

    // ahora le digo que pase al siguiente controlador
    next();
  } catch (error) {
    return res.status(400).json({
      message: "Token invalida",
      content: error.message,
    });
  }
}
