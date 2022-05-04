import { crearDetallePedidoRequestDTO } from "../dtos/detallePedido.dto.js";
import { Prisma } from "../prisma.js";

export const crearDetallePedido = async (req, res) => {
  try {
    const data = crearDetallePedidoRequestDTO(req.body);
    // LUEGO DE CREAR EL DETALLE PEDIDO ACTUALIZAR EL PEDIDO PARA MODIFICAR EL TOTAL DEL PEDIDO
    // LO HAREMOS MEDIANTE TRANSACCIONES
    await Prisma.$transaction(async () => {
      // https://www.prisma.io/docs/concepts/components/prisma-client/transactions#interactive-transactions-in-preview
      // ahora puedo usar dentro de la transaccion una secuencia de codigo
      // hago la busqueda de ese producto
      const { precio } = await Prisma.producto.findUnique({
        where: { id: data.productoId },
        rejectOnNotFound: true,
        select: { precio: true },
      });

      // hago la busqueda el pedido
      const { id, total } = await Prisma.pedido.findUnique({
        where: { id: data.pedidoId },
        select: { id: true, total: true },
        rejectOnNotFound: true,
      });

      // creo el detalle de ese pedido con la modificacion del subtotal
      const { subTotal } = await Prisma.detallePedido.create({
        data: { ...data, subTotal: precio * data.cantidad },
        select: { subTotal: true },
      });

      // ahora actualizo el total del pedido
      await Prisma.pedido.update({
        data: { total: total + subTotal },
        where: { id },
      });
    });

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
