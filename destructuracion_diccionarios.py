def sumar(a,b):
    return a+b

print(sumar(10,5))
print(sumar(a=10, b=5))
parametros = {
    'a': 10,
    'b': 5
}
# al momento de nosotros querer pasar los parametros pero en forma de un diccionario se puede hacer la destructuracion usando los ** antes del diccionario
print(sumar(**parametros))
print(sumar(**{'a': 10,'b': 5}))
# en el caso que solamente queramos pasar los valores pero no el parametro del cual esta ese valor entonces podemos utilizar un * y se le pasara o bien una tupla o bien una lista ya que si le pasamos un diccionario solamente agarrar las llaves mas no sus valores
print(sumar(*[10,5]))

def restar(**kwargs):
    return(kwargs)

def multiplicar(*args):
    return(args)

print(multiplicar(5,4))
print(restar(x=1,y=2,z=3))