import express, { json } from "express";
import { detallePedidoRouter } from "./routes/detallePedido.routes.js";
import { pedidosRouter } from "./routes/pedidos.routes.js";
import { productosRouter } from "./routes/productos.routes.js";
import { usuarioRouter } from "./routes/usuarios.routes.js";

const app = express();

app.use(json());

const PORT = process.env.PORT ?? 3000;

app.get("/", (req, res) => {
  res.json({
    message: "Bienvenido a mi API del minimarket",
  });
});

// agregar un bloque de rutas definidas en otro archivo
app.use(productosRouter);
app.use(usuarioRouter);
app.use(pedidosRouter);
app.use(detallePedidoRouter);

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
