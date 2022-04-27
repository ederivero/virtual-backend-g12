// usando ECMAScript
import express from "express"
// usando CommonJs
// const express = require('express') 

const servidor = express()
// middleware: intermediario que permite visualizar informacion adicional
// ahora podremos recibir y entender a un formato JSON
servidor.use(express.json())
// recibir y entender los bodys que sean puro texto
servidor.use(express.raw()) 
servidor.use(express.urlencoded({extended: true})) 

const productos = [
  {
    nombre:'platano',
    precio: 1.80,
    disponible: true
  }
]
// cuando se ingrese a la ruta URL/ en metodo GET
servidor.get('/',(req, res)=>{
  return res.status(200).json({
    message: 'Bievenido a mi API de productos'
  })
})

servidor.post('/crear-producto', (req,res)=>{
  // mostrara todo el body enviado por el cliente 
  console.log(req.body);

  return res.status(201).json({
    message:'Producto agregado exitosamente'
  })
})

servidor.listen(3000, () => {
  console.log("Servidor corriendo exitosamente en el puerto 3000")
})
