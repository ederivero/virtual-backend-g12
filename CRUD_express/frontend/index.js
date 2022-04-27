const BASE_URL = "http://localhost:3000";

async function pedirProductos() {
  const respuesta = await fetch(`${BASE_URL}/productos`, { method: "GET" });
  const data = await respuesta.json();
  console.log(data);
}

pedirProductos();
