# un error es una mala ejecucion del codigo que hara que mi proyecto o script deje de funcionar
# en python tenemos varios errores para los diferentes sucesos:
# locals()['__builtins__'] > me retornara del diccionario de locals() todos los errores definidos dentro de python y los atributos de los errores. 
# dir > nos permite listar estos atributos como strings para poder leerlos facilmente
# locals() > nos devuelve todas las variables disponibles que tenemos en python en este scope

# print(dir(locals().get('__builtins__')))

# todo try tiene que tener OBLIGATORIAMENTE al menos un except
try:
    valor = int(input('Ingresa un numero:'))
    print('Yo me ejecuto si todo salio bien')
    print(valor)
except ValueError:
    # entrara a este except cuando el error sea de tipo ValueError (error de conversion de un str a un int)
    print('Error al convertir un string a un numero')
except Exception as error:
    print(error.args)
    # capturara el error causante impidiendo que el programa deje de funcionar
    # solamente ingresara cuando tengamos un error 
    print('Oops algo salio mal intentalo nuevamente')

print('Yo finalizo correctamente')


while True:
    try:
        valor = int(input('Ingresa un numero: '))
        break
    except:
        print('Valor incorrecto, solo pueden ser numeros')

print(valor)

try:
    resultado = 1 / 1
    # voy a buscar el producto a la base de datos
    producto = None
    if (producto is None):
        raise Exception('El producto no existe en la bd')
except:
    print('hubo un error')
else:
    # el else en el caso de los try-except se ejecutara si nunca ingreso a un except, osea si el funcionamiento fue el esperado sin errores
    # hace la boleta o genera el proceso de pago del e-commerce
    print('La division se ejecuto sin problemas')
finally:
    # ingresara si el try fue exitoso o no osea si del mismo ingreso a algun except o no
    print('Yo me ejecutare si todo fue bien y fue mal')
