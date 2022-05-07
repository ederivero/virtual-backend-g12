import mongoose from "mongoose";
import bcryptjs from "bcryptjs";
// Toda la configuracion que estamos haciendo es solamente a nivel de mongoose, osea si agregamos un usuario de frente a la bd no hara caso a ninguna de estas caracterisiticas

const libroSchema = new mongoose.Schema(
  {
    nombre: {
      type: mongoose.Schema.Types.String,
      required: true,
    },
    avance: {
      type: mongoose.Schema.Types.String,
      enum: ["COMPLETO", "INCOMPLETO"],
      required: true,
    }, // completo o incompleto
    numPagina: {
      type: mongoose.Schema.Types.Number,
      min: 1,
      name: "num_pagina", // en la bd la columna se llame de esa manera mientras que en mongoose se llame como el nombre de la llave
    },
  },
  {
    // https://mongoosejs.com/docs/guide.html#options
    // no podemos evitar usar el _id o un id personalizable en un schema principal (que no sea un subschema)
    _id: false, // sirve para indicar que en este schema no se creara automaticamente el _id (primary key)
    timestamps: {
      updatedAt: "fecha_actualizacion", // true > solo creara el updatedAt | string > creara esa columna pero con ese nombre
    }, // creara las columnas de auditoria (created_at y el updated_at)
  }
);

const usuarioSchema = new mongoose.Schema({
  correo: {
    type: mongoose.Schema.Types.String,
    required: true, // para que si o si me pase el valor de esta columna
    unique: true, // el correo no se va a poder repetir en la coleccion (tabla)
    // ademas de las configuraciones generales tenemos algunas configuraciones dependiendo del tipo de dato
    // https://mongoosejs.com/docs/schematypes.html
    lowercase: true,
    maxlength: 100,
  },
  nombre: mongoose.Schema.Types.String, // aca no le podremos agregar configuracion adicional
  telefono: {
    type: mongoose.Schema.Types.Number,
    required: false,
  },
  password: {
    type: mongoose.Schema.Types.String,
    set: (valorActual) => bcryptjs.hashSync(valorActual, 10), // sera una funcion que antes de guardarse en la base de datos se modificara su valor
    // get: (valorActual) => "",
  },
  // asi seria una relacion de 1:1 en la cual un usuario solo puede tener un libro y un libro le perteneceria a un usuario
  // libro: libroSchema
  // asi seria una relacion de 1:n un usuario puede tener varios libros pero ese libro solo le pertenecera a un usuario
  libros: {
    // [libroSchema]
    type: [libroSchema],
  },
});

// aca indicamos que crearemos una coleccion en la bd
export const Usuario = mongoose.model("usuarios", usuarioSchema);
