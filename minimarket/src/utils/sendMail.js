import nodemailer from "nodemailer";
//                   SERVIDOR      | PUERTO
// outlook > outlook.office365.com | 587
// hotmail > smtp.live.com         | 587
// gmail >   smtp.gmail.com        | 587
// icloud >  smtp.mail.me.com      | 587
// yahoo >   smtp.mail.yahoo.com   | 587

const trasporter = nodemailer.createTransport({
  host: "smtp.gmail.com",
  port: 587,
  auth: {
    user: process.env.EMAIL_ACCOUNT,
    pass: process.env.EMAIL_PASSWORD,
  },
});

export const enviarCorreoValidacion = async ({ destinatario, hash }) => {
  // Pagina para generar plantillas html > https://beefree.io/
  const html = `
    <p>
        Hola para comenzar a disfrutar de todas las ofertas en nuestro Minimarket, por favor haz click en el siguiente enlace   
            <a href="${process.env.FRONTEND_URL}?hash=${hash}">
                Valida mi cuenta.
            </a>
    </p>`;

  try {
    await trasporter.sendMail({
      from: "ederiveroman@gmail.com",
      to: destinatario,
      subject: "Validacion de Correo de Minimarket APP",
      html,
    });
    console.log("Correo enviado exitosamente");
  } catch (error) {
    console.log(error);
    return error;
  }
};
