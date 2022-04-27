// usando ECMAScript
import express from "express";
import cors from "cors";
// usando CommonJs
// const express = require('express')

const servidor = express();
// middleware: intermediario que permite visualizar informacion adicional
// ahora podremos recibir y entender a un formato JSON
servidor.use(express.json());
// recibir y entender los bodys que sean puro texto
servidor.use(express.raw());
servidor.use(express.urlencoded({ extended: true }));
// el metodo GET SIEMPRE va a poder ser accedido a pesar que solamente en el methods le indiquemos otro
servidor.use(
  cors({
    origin: ["http://127.0.0.1"], // '*'
    methods: ["POST", "PUT", "DELETE"], // '*'
    allowedHeaders: ["Content-Type", "Authorization"], // '*'
  })
);

const productos = [
  {
    nombre: "platano",
    precio: 1.8,
    disponible: true,
  },
];
// cuando se ingrese a la ruta URL/ en metodo GET
servidor.get("/", (req, res) => {
  return res.status(200).json({
    message: "Bievenido a mi API de productos",
  });
});

servidor.post("/productos", (req, res) => {
  // mostrara todo el body enviado por el cliente
  console.log(req.body);
  const data = req.body;

  productos.push(data);

  return res.status(201).json({
    message: "Producto agregado exitosamente",
  });
});

servidor.get("/productos", (req, res) => {
  const data = productos;
  return res.json({
    data, // que la llave sera el mismo nombre que la variable y su valor sera el contenido de esa variable
  });
});

servidor
  .route("/producto/:id")
  .get((req, res) => {
    console.log(req.params);
    const { id } = req.params;

    if (productos.length < id) {
      // 400 > Bad Request (Mala Solicitud)
      return res.status(400).json({
        message: "El producto no existe",
      });
    } else {
      const data = productos[id - 1];

      return res.json({
        data,
      });
    }
  })
  .put((req, res) => {
    // extraer el id
    const { id } = req.params;
    // validar si existe esa posicion en el arreglo
    if (productos.length < id) {
      // si no existe, emitir un 400 indicando que el producto a actualizar no existe
      return res.status(400).json({
        message: "El producto a actualizar no existe",
      });
    } else {
      // si existe, modificar con el body
      productos[id - 1] = req.body;

      return res.json({
        message: "Producto actualizado exitosamente",
        content: productos[id - 1],
      });
    }
  })
  .delete((req, res) => {
    const { id } = req.params;
    if (productos.length < id) {
      return res.json({
        message: "Producto a eliminar no existe",
      });
    } else {
      // Metodo de los arreglos para eliminar uno o mas elementos del arreglo iniciando desde una posicion e indicando la cantidad de elementos a eliminar
      productos.splice(id - 1, 1);
      return res.json({
        message: "Producto eliminado exitosamente",
      });
    }
  });

servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente en el puerto 3000");
});
