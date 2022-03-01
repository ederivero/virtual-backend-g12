# Operadores de Comparacion
numero1, numero2 = 10, 20
# NOTA: en python no tenemos el triple igual 
# ===
# Igual que
print(numero1 == numero2)
# Mayor que | Mayor igual que
print( numero1 > numero2)
print( numero1 >= numero2)
# Menor que | Menor igual que
print( numero1 < numero2)
print( numero1 <= numero2)
# Diferente de
print( numero1 != numero2)

# Operadores Logicos
# sirve para compara varias comparaciones
# en JS se utiliza && en python se utiliza la palabra and
# en JS se utiliza || en python se utiliza la palabra or
# en el and todo tiene que ser verdadero para que el resultado final sea verdadero
print((10>5) and (10< 20))
# en el or al menos una condicion tiene que ser verdadera para que el resultado final sea verdadero
print((10>5) or (30< 20))

# Operadores de Identidad
# is
# is not
# sirve para ver si estan apuntando a la misma direccion de memoria
verduras= ['apio', 'lechuga', 'zapallo']
verduras2 = verduras
verduras3 = ['apio', 'lechuga', 'zapallo'] # [ 'brocoli', 'espinaca', 'succhini']
# NOTA: las colecciones de datos son variables mutables ( que cuando cambio su contenido este se vera reflejado en todas las copias de dicha variable)
verduras2[0] = 'peregil'
verduras[1] = 'manzana'
# el metodo copy() lo que hace es copia todo el contenido de la variable pero se guardara en una nueva posicion de memoria
verduras4 = verduras.copy()
verduras4[0] = 'huatacay'
print(verduras2 is verduras)
print(verduras)
print(verduras2)
print(verduras3 is verduras)

print('la posicion de la variable verduras es:',id(verduras))
print('la posicion de la variable verduras2 es:',id(verduras2))
print('la posicion de la variable verduras4 es:',id(verduras4))

# Si hablamos de variables primitivas (str, int, float, boolean, date) entonces al hacer la copia compartira su mismo espacio de memoria PERO al hacer alguna modificacion a cualquiera de las dos o mas variables que esten usando el mismo espacio de memoria automaticamente python le asignara uno nuevo
nombre = 'eduardo'
nombre2 = nombre
print(nombre2 is nombre)
print(id(nombre2))
print(id(nombre))
nombre2 = 1
print(nombre)
print(id(nombre2))
print(id(nombre))


# Validar si el nombre del usuario es eduardo y que sea peruano o colombiano
nombre= 'eduardo'
nacionalidad = 'venezolano'
print(nombre == 'eduardo' and (nacionalidad == 'peruano' or nacionalidad == 'colombiano'))