# variable global
nombre = 'Eduardo'

# si definimos una variable de manera global pero la queremos modificar dentro de una funcion no sera posible ya que al momento de querer modificarla nos pedira que esa variable exista de manera aislada dentro de esa funcion
def saludar():
    global nombre
    # global > le estaremos indicando a la funcion que queremos utilizar una variable definida fuera de la misma para hacer modificaciones dentro de la funcion
    nombre = nombre * 2
    print(nombre)

saludar()

# ahora definimos una variable local
# si definimos variables dentro de la funcion solamente estas podran ser usadas dentro de las mismas mas no afuera de ellan aun asi mandemos a llamar a la funcion xq la variable se crea cuando se llama y se destruye cuando se termina de ejecutar esa funcion (ese sub bloque de codigo)
def x():
    ganacia = 0.15


x()
# no puedo mandar a llamar variables que solamente existen dentro de una funcion
# print(ganancia)