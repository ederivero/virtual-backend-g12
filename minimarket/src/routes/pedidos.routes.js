import { Router } from "express";
import { crearPedido } from "../controllers/pedidos.controller.js";
import { validarCliente, verificarToken } from "../utils/validador.js";

export const pedidosRouter = Router();

pedidosRouter
  .route("/pedidos")
  .all(verificarToken, validarCliente)
  .post(crearPedido);
