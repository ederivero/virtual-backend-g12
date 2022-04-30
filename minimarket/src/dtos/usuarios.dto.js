import prisma from "@prisma/client";
import validator from "validator";

export function usuarioRequestDTO({ nombre, email, password, rol }) {
  //  xxxxx@xxxxxxx.xxx
  const errores = [];
  if (!validator.isEmail(email)) {
    errores.push("El email no es un correo valido");
  }

  if (validator.isEmpty(password)) {
    errores.push("El password no puede estar vacio");
  }

  if (validator.isEmpty(nombre)) {
    errores.push("El nombre no puede estar vacio");
  }

  if (
    rol !== prisma.USUARIO_ROL.ADMINISTRADOR &&
    rol !== prisma.USUARIO_ROL.CLIENTE
  ) {
    errores.push(
      `El rol puede ser ${prisma.USUARIO_ROL.ADMINISTRADOR} o ${prisma.USUARIO_ROL.CLIENTE}`
    );
  }

  if (errores.length != 0) {
    throw Error(errores);
  } else {
    return {
      nombre,
      email,
      password,
      rol,
    };
  }
}
// alt + 96 > `
// alt + 124 > |

export function loginRequestDTO({ email, password }) {
  // Validar que el email sea un email y que la password no sea nula
  const errores = [];

  if (!validator.isEmail(email)) {
    errores.push("El email no es un correo valido");
  }
  if (validator.isEmpty(password)) {
    errores.push("El password no puede estar vacio");
  }

  if (errores.length != 0) {
    throw Error(errores);
  } else {
    return {
      email,
      password,
    };
  }
}
