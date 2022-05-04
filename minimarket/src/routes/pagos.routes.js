import { Router } from "express";
import { crearPreferencia } from "../controllers/pagos.controller.js";

export const pagosRouter = Router();

pagosRouter.post("/generar-pago", crearPreferencia);
