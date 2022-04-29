// nullish coalesing operator
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Nullish_coalescing_operator
// si el primer valor no es nulo o undefined entonces sera ese valor, caso contrario tomara el segundo valor
const PORT = process.env.PORT ?? 3000;
// sirve para hacer una comprobacion previa
// Operador AND
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_AND
const persona = {
  nombre: "eduardo",
  apellido: "de rivero",
  /*
    actividades : ['Nadar', 'Montar caballo']
     */
};
// Nadar | undefined
let actividades = persona.actividades && persona.actividades[0];
actividades = false;
actividades = 10.2;
actividades = new Date();
actividades = undefined;

// Operador OR ||
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Logical_OR
// en JS el 0 significa False y el 1 y los demas numeros significan True
const numero1 = false;
// si la primera condicion es verdadera entonces devuelvo esa sino devolvere la segunda
const resultado = numero1 || 10;
// si el primero resultado no es null o undefined lo devolvere caso contrario devolver el segundo valor
const resultado2 = numero1 ?? 10;
console.log(resultado);
console.log(resultado2);
