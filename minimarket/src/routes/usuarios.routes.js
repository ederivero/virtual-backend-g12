import { Router } from "express";
import {
  confirmarCuenta,
  crearUsuario,
  login,
  perfil,
} from "../controllers/usuarios.controller.js";
import { verificarToken } from "../utils/validador.js";

export const usuarioRouter = Router();

usuarioRouter.post("/registro", crearUsuario);
usuarioRouter.post("/login", login);
usuarioRouter.post("/confirmar-cuenta", confirmarCuenta);
usuarioRouter.get("/perfil", verificarToken, perfil);
