import validator from "validator";

export const crearPedidoRequestDTO = ({ clienteId }) => {
  const errores = [];

  if (validator.isEmpty(clienteId.toString())) {
    errores.push("El clienteId no puede estar vacio");
  }

  if (errores.length !== 0) {
    throw Error(errores);
  } else {
    return {
      clienteId,
    };
  }
};
