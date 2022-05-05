import { Router } from "express";
import {
  crearPreferencia,
  MercadoPagoWebhooks,
} from "../controllers/pagos.controller.js";

export const pagosRouter = Router();

pagosRouter.post("/generar-pago", crearPreferencia);
pagosRouter.post("/mp-webhooks", MercadoPagoWebhooks);
