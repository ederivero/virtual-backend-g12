import express from "express";
import morgan from "morgan";

const app = express();
// https://www.npmjs.com/package/morgan
const logger = morgan("dev");
// morgan es un middleware que me ayuda a poder hacer seguimiento a las peticiones a mi API
app.use(logger);

const PORT = process.env.PORT ?? 3000;

app.listen(PORT, () => {
  console.log(`Servidor corriendo exitosamente en el puerto ${PORT}`);
});
