# Esto es un comentario y sirve para dar contexto de que se hace, se hizo o se hara
# TODO: logica para este controlador

edad = 30

# variables de texto
nombre = 'eduardo'
apellido = "de'rivero"

# si queremos tener un texto que pueda contener saltos de linea
descripcion = """hola amigos:
como estan?
yo muy bien jeje
"""

descripcion2 = '''¿hola amigos:
como estan?'''

desCripcion2 = "adios"

print(descripcion2)
print(desCripcion2)

# variables numericas
year = 2022

# type() => mostrara que tipo de variable es
print(type(year))
print(type(desCripcion2))

# Python no se puede crear una variable sin un contenido a exepcion del None
# en python None = null | undefined
especialidad = None

# en Python no hace validacion del tipo de dato primario (si la variable 'nace' siendo string) normal se puede cambiar su tipo a otro (Boolean, int, float, array, etc.)
# en Python no existen las constantes
dni= [123123123]
dni= 'peruano'
dni= False

# id() > dara la ubicacion de esa variablen en relacion a la memoria del dispositivo
print(id(dni))


print(type(especialidad))

mes, dia = "febrero", 28

print(mes)

# del > elimina la variable de la memoria 
del mes

# si queremos usar luego de la eliminacion esa variable no sera posible ya que se elimino de la memoria
print(mes)