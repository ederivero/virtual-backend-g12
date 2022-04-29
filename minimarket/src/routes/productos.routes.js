import { Router } from "express";
import { crearProducto } from "../controllers/productos.controller.js";

export const productosRouter = Router();
productosRouter.post("/productos", crearProducto);
