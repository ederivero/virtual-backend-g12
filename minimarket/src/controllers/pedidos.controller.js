import { Prisma } from "../prisma.js";
import { crearPedidoRequestDTO } from "../dtos/pedidos.dto.js";

export const crearPedido = async (req, res) => {
  try {
    const { clienteId } = crearPedidoRequestDTO({ clienteId: req.user.id });

    // agregar el pedido a la base de datos
    const pedidoCreado = await Prisma.pedido.create({
      data: {
        estado: "CREADO",
        fecha: new Date(),
        total: 0.0,
        clienteId,
      },
      select: {
        id: true,
      },
    });

    return res.status(201).json({
      message: "Pedido creado exitosamente",
      content: pedidoCreado,
    });
  } catch (error) {
    return res.status(400).json({
      message: "Error al crear el pedido",
      content: error.message,
    });
  }
};
