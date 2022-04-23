const URL_BACKEND = "http://127.0.0.1:8000";

// Peticion normal
async function pedirPlatos() {
  const respuesta = await fetch(URL_BACKEND + `/platos/`, { method: "GET" });
  const data = await respuesta.json();
  console.log(data);
}

async function login() {
  const respuesta = await fetch(URL_BACKEND + "/auth/inicio-sesion/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      correo: "mozo@outlook.com",
      password: "Welcome123!",
    }),
  });
  const data = await respuesta.json();
  listarStock(data.access);
  console.log(data);
}

// Usando Bearer Token
async function listarStock(token) {
  const respuesta = await fetch(URL_BACKEND + "/platos/stock/", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  const data = await respuesta.json();
  console.log(data);
}

pedirPlatos();
login();
