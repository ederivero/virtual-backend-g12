import { libroRequestDTO } from "../dtos/libro.request.dto.js";
import { Usuario } from "../models/usuarios.models.js";

export const agregarLibro = async (req, res) => {
  // dto en el cual valido que me envie los campos para agregar un libro
  try {
    const data = libroRequestDTO(req.body);
    console.log(req.user);
    const usuarioActual = req.user;
    usuarioActual.libros.push(data);
    // internamente cuando hacemos una busque a un registro de mongoose se jala algunos datos para poder sobreescribir o modificar este registro a nivel de base de datos y esto se logra con el metodo save() (es un proceso asincrono)
    // https://mongoosejs.com/docs/documents.html#updating-using-save
    await usuarioActual.save();

    return res.json({
      message: "ok",
      content: usuarioActual.libros,
    });
  } catch (e) {
    return res.status(400).json({
      message: "Errro al agregar el libro",
      content: e.message,
    });
  }
};

export const listarLibros = (req, res) => {
  // req.user > toda la data de nuestro usuario
  return res.json({
    message: "los libros son:",
    content: req.user.libros,
  });
};

// http://localhost:3000/libro/:_id
export const devolverLibro = async (req, res) => {
  const { _id: id_del_libro } = req.params;
  // no puedo usar clausulas de condicion
  // https://www.mongodb.com/docs/manual/reference/operator/projection/positional/#proj._S_
  // usando las propiedades de la base de datos
  const libroEncontrado = await Usuario.findOne(
    {
      _id: req.user._id, // id del usuario
      "libros._id": id_del_libro, // id del libro
    },
    // con la proyeccion se le indica a mongodb que esta busqueda se tiene que realizar en un nivel mas 'adentro' porque libros es un arreglo y lo tendra q iterara y hacer la busqueda de ese libro, seria algo muuuy similar con depth en django
    {
      "libros.$": 1,
    }
  );

  // forma tradicional en la cual se realiza en el lado del backend
  const libro = req.user.libros.filter(
    (libro) => libro._id.toString() === id_del_libro
  );
  return res.json({
    message: "El libro es:",
    content: libro,
    content2: libroEncontrado,
  });
};
