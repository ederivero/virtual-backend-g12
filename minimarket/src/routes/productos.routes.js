import { Router } from "express";
import {
  actualizarProducto,
  crearProducto,
  eliminarProducto,
  listarProductos,
} from "../controllers/productos.controller.js";
import { validarAdmin, verificarToken } from "../utils/validador.js";

export const productosRouter = Router();

productosRouter
  .route("/productos")
  .post(verificarToken, validarAdmin, crearProducto)
  .get(listarProductos);

productosRouter
  .route("/producto/:id")
  // el .all sirve para indicar todos los middlewares que se tienen que llamar antes de llamarse al controlador final (actualizarProducto en caso de PUT y a eliminarProducto en caso de DELETE)
  .all(verificarToken, validarAdmin)
  .put(actualizarProducto)
  .delete(eliminarProducto);
