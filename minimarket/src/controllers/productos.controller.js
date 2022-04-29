import { Prisma } from "../prisma.js";

export const crearProducto = async (req, res) => {
  console.log("Yo me ejecuto primero");
  // Con el await le estamos diciendo que a la promesa la vamos a esperar y tiene que ser exitoso
  try {
    const resultado = await Prisma.producto.create({ data: req.body });

    console.log(resultado);

    console.log("Yo me ejecuto al ultimo");

    return res.json({
      message: "Producto Agregado exitosamente",
    });
  } catch (e) {
    console.log(e);
    return res.json({
      message: "Error al crear el producto",
    });
  }
};
