import { Router } from "express";
import { registrarUsuario } from "../controllers/usuarios.controllers.js";

export const usuariosRouter = Router();

usuariosRouter.post("/registro", registrarUsuario);
