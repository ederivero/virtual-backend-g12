notas = [10, 20, 16, 8, 6, 1]

# for(let i=0; i<10; i++){...}
# en cada iteracion de la lista notas tendremos su valor y lo almacenaremos en una variable llamda nota
# el mismo funcionamiento se da para cualquier coleccion de datos (lista, tupla, diccionario, conjunto)
for nota in notas:
    print(nota)

# crearemos un bucle manual para una iteracion hasta el limite definido en el range
# https://docs.python.org/3/library/stdtypes.html?highlight=range#range
for numero in range(10):
    print(numero)

# si colocamos dos parametros el primero significara el numero inicial y el segundo el tope
for numero in range(5,10):
    print(numero)

# si colocamos dos parametros el primero significara el numero inicial, el segundo el tope y el tercero sera de cuanto en cuanto hara la incrementacion o decrementacion
# empezara en 5, hasta <10 y en cada ciclo incrementara en 2 unidades
for numero in range(5,10,2):
    print(numero)


# imprimir los 3 valores iniciales de notas
notas = [10, 20, 16, 8, 6, 1]
# AYUDITA: utilizar range(...)
# AYUDITA: notas[..:..]
for nota in notas[:3]:
    print(nota)

for posicion in range(3):
    print(notas[posicion])
