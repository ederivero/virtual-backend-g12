import mongoose from "mongoose";

// Toda la configuracion que estamos haciendo es solamente a nivel de mongoose, osea si agregamos un usuario de frente a la bd no hara caso a ninguna de estas caracterisiticas

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
    set: (valorActual) => {
      console.log(valorActual);
      return "hola";
    }, // sera una funcion que antes de guardarse en la base de datos se modificara su valor
  },
});

// aca indicamos que crearemos una coleccion en la bd
export const Usuario = mongoose.model("usuarios", usuarioSchema);
