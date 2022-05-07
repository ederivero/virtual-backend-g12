import validador from "validator";

export const libroRequestDTO = ({ nombre, avance, numPagina }) => {
  const errores = [];
  if (validador.isEmpty(nombre)) {
    errores.push("Nombre no puede estar vacio");
  }

  if (avance !== "COMPLETO" && avance !== "INCOMPLETO") {
    errores.push("avance debe ser COMPLETO o INCOMPLETO");
  }

  if (avance === "INCOMPLETO") {
    if (validador.isEmpty(numPagina.toString()) || !numPagina) {
      errores.push("numPagina no puede ser vacio si el avance es INCOMPLETO");
    }
  }

  if (errores.length !== 0) {
    throw Error(errores);
  } else {
    return { nombre, avance, numPagina };
  }
};
