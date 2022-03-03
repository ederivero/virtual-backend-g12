# mientras que
numero = 0
while numero <= 10:
    # pass > sirve para indicar dentro de un bloque de codigo que aun no hemos definido la logica que no haga pero que no de error
    print(numero)

    # bucle infinito (infinite loop) > es un ciclo que se va a ejecutar por siempre y nunca tendra fin
    numero += 1
    # break
else:
    print('el while termino bien')


# en relacion a los siguientes numeros indicar cuantos son pares y cuantos son impares
numeros =[1,5,16,28,234,67,29, 0]

# Hay x numeros pares
# Hay x numeros impares
# Pueden utilizar o un while o un for

# PISTA: usar el modulo

# PRIMERO CON FOR
par, impar = 0 , 0
for numero in numeros:
    if numero % 2 == 0 :
        # la division entre dos me da un residuo 0 osea par
        par +=1
    else:
        impar += 1

print('Hay {} numeros pares'.format(par))
print('Hay {} numeros impares'.format(impar))

# AHORA CON WHILE
posicion = 0
par, impar = 0 , 0

while posicion < len(numeros):
    if numeros[posicion] % 2 == 0:
        par += 1
    else:
        impar += 1
    posicion += 1

print('Hay {} numeros pares'.format(par))
print('Hay {} numeros impares'.format(impar))
