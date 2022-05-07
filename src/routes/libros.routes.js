import { Router } from "express";
import {
  agregarLibro,
  devolverLibro,
  listarLibros,
} from "../controllers/libros.controllers.js";
import { validarToken } from "../utils/validador.js";

export const libroRouter = Router();

libroRouter
  .route("/libro")
  .all(validarToken)
  .post(agregarLibro)
  .get(listarLibros);

libroRouter.route("/libro/:_id").all(validarToken).get(devolverLibro);
