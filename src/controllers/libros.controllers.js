import { libroRequestDTO } from "../dtos/libro.request.dto.js";
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
