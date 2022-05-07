import express from "express";
import morgan from "morgan";
import mongoose from "mongoose";
import { usuariosRouter } from "./routes/usuarios.routes.js";
import { libroRouter } from "./routes/libros.routes.js";

const app = express();
// https://www.npmjs.com/package/morgan
const logger = morgan("dev");
// morgan es un middleware que me ayuda a poder hacer seguimiento a las peticiones a mi API
app.use(logger);

// sirve para indicar la data que va a poder aceptar y entender nuestra API
app.use(express.json());

app.use(usuariosRouter);
app.use(libroRouter);

const PORT = process.env.PORT ?? 3000;

mongoose
  .connect(process.env.MONGO_URL, { dbName: process.env.DBNAME })
  .then((valor) => {
    console.log("Conectado a la base de datos 🔌");
  })
  .catch((error) => {
    console.log(error);
    console.log("Error al conectarse a la base de datos 💀");
  });

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
