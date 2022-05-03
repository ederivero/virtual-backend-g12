import { Prisma } from "../prisma.js";

export const crearDetallePedido = async (req, res) => {
  try {
    const data = crearDetallePedidoRequestDTO(req.body);

    return res.status(201).json({
      message: "Detalle creado exitosamente",
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el detalle del pedido",
      content: error.message,
    });
  }
};
