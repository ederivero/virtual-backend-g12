# funciones 
# almacenara un bloque de codigo con su comportamiento y solamente se ejecutara cuando esa sea invocado (llamado)

# al momento de llamar a la funcion tenemos que pasarle el mismo numero de parametros que hemos definido
def sumar(numero1, numero2):
    print('Se realizara la sumatoria . . . ')
    print(numero1 + numero2)

sumar(5,7)

def nombre(x):
    '''Funcion que recibe un string y lo imprime por consola :)'''
    print(x)

nombre('Eduardo')

# mostrara la documentacion de la funcion si es que hay
print(nombre.__doc__)

# ahora, tambien podriamos definir funciones que ejecuten algo y que nos den una respuesta
usuario= []
def registrar(nombre, email, telefono):
    '''Funcion que registra un usuario y lo guarda en una lista'''
    # aqui registraremos el usuario 
    usuario.append({
        'nombre': nombre,
        'email': email,
        'telefono': telefono
    })

    return ('usuario creado exitosamente', usuario[0], 201)

# si una funcion retorna mas de un valor (retornara una tupla) entonces podemos hacer dos cosas: 1. si solamente declaramos una variable ahi se almacenara toda la tupla, 2. si queremos almacenar cada valor de la tupla en una variable podemos hacer una destructuracion de esa tupla declarando el mismo numero de variables que el numero de contenidos de la tupla
resultado, estado_civil, nacionalidad = registrar('Eduardo', 'ederiveroman@gmail.com', '974207075')
rpta = registrar('Eduardo', 'ederiveroman@gmail.com', '974207075')

print(rpta)
print(resultado)
print(estado_civil)
print(nacionalidad)


productos=[]
# Si nosotros creamos una funcion que opcional reciba ciertos parametros, estos parametros opcionales SIEMPRE deben de ir al final, primero los requeridos y luego los opcionales
def registrar_productos(nombre, precio, estado=True, almacen='Almacen del cercado'):
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'estado': estado,
        'almacen': almacen
    })
    return 'Producto agregado exitosamente'

# siempre tenemos que pasar obligatoriamente los parametros que no tienen valores por defecto
registrar_productos('Tomates', 4.50)
registrar_productos('Apio', 1.40, False)
registrar_productos('Cebolla', 5.30, True, 'Almacen nuevo mercado')
# otra forma de pasar parametros
registrar_productos(almacen='Almacen de la costa', nombre='Pescado tilapia', precio=2.50)



