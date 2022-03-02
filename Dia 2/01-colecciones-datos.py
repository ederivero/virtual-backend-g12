# coleccion de datos es una variable que puede almacenar varios valores

# Listas (List)
# ordernadas y que puede ser modificadas
            #0      1        2        3         4       5
nombre= ['Pedro', 'Luis', 'Danny', 'Cesar', 'Magaly', 'Anahi']

combinada = ['Eduardo', 80, False, 15.8, [1,2,3]]

# las listas siempre empiezan en la posicion 0 
print(nombre[0])

# cuando hacemos el uso de valores negativos en una lista internamente python le dara vuelta
print(nombre[-1])

print(nombre)
# si queremos ingresar a una posicion inexistente nos lanzara un error de 'indice fuera de rango'
# print(nombre[10])

# pop() > remueve el ultimo elemento de la lista y se puede almacenar en otra variable
resultado = nombre.pop()
print(resultado)
print(nombre)

# append() > ingresa un nuevo elemento a la ultima posicion de la lista
nombre.append('Juana')

# elimina el contenido de una posicion de la lista pero no lo podemos almacenar en otra variable
del nombre[0]

print(nombre)

# clear() > limpia toda la lista y la deja como nueva
nombre.clear() # > []
print(nombre)
                # =1 <3
x = combinada[:] # .copy()
y = combinada

# indicar una sub seleccion de la lista 
print(combinada[1:4])

# indicando el contenido de la lista y esto es muy util para hacer una copia de la lista sin usar su misma posicion de memoria
print(combinada[:])

print(id(x))
print(id(combinada))
print(id(y))

# desde el inicio hasta <2
print(combinada[:2])
# desde la posicion 2 hasta el final
print(combinada[2:])

meses_dscto = ['Enero', 'Marzo', 'Julio']
mes= 'Septiembre'
mes2= 'Enero'
# indicara si el valor no se encuentra dentro de la lista

print(mes not in meses_dscto)
# indicar si el valor se encuentra en la lista
print(mes2 in meses_dscto)

seccion_a=['Roxana', 'Juan']
seccion_b=['Julieta', 'Martin']
# si hacemos una sumatoria en las listas estas se combinaran en la cual la segunda lista ira despues de la primera
print(seccion_a + seccion_b)

# sirve para esperar un dato ingresado por el usuario
# dato = input('Ingresa tu nombre:')
# print(dato)

# Tuplas
# muy similar a la lista a excepcion que no se puede modificar
cursos = ('backend', 'frontend', 1 , True)

print(cursos)
print(cursos[0])
print(cursos[0:1])
cursos.append('otra cosa')
# cursos[0] = 'mobile design'