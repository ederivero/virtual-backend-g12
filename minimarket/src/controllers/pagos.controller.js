import mercadopago from "mercadopago";
import { Prisma } from "../prisma.js";

export const crearPreferencia = async (req, res) => {
  try {
    //
    const { pedidoId } = req.body;

    const pedidoEncontrado = await Prisma.pedido.findUnique({
      where: { id: pedidoId },
      rejectOnNotFound: true,
    });

    // https://www.mercadopago.com.pe/developers/es/reference/preferences/_checkout_preferences/post
    mercadopago.preferences.create({
      auto_return: "approved",
      back_urls: {
        failure: "http://localhost:3000/pago-fallido",
        pending: "http://localhost:3000/pago-pendiente",
        success: "http://localhost:3000/pago-exitoso",
      },
      metadata: {
        nombre: "Prueba",
      },
      payer: {
        name: "Eduardo",
        surname: "De Rivero",
        address: {
          zip_code: "04002",
          street_name: "Calle Los Girasoles",
          street_number: "105",
        },
        email: "test_user_46542185@testuser.com",
      },
      items: [
        {
          id: "1234",
          category_id: "456",
          currency_id: "PEN",
          description: "Zapatillas de Outdoor",
          picture_url: "https://imagenes.com",
          quantity: 1,
          title: "Zapatillas edicion Otoño",
          unit_price: 75.2,
        },
      ],
    });
  } catch (error) {
    return res.json({
      message: "Error al crear la preferencia",
      content: error.message,
    });
  }
};
