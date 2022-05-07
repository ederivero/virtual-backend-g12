import { Router } from "express";
import { agregarLibro } from "../controllers/libros.controllers.js";
import { validarToken } from "../utils/validador.js";

export const libroRouter = Router();

libroRouter.route("/libro").all(validarToken).post(validarToken, agregarLibro);
