# IF - ELSE
# python al no utilizar las llaves para definir bloque de un comportamiento diferente tenemos que utilizar tabulaciones (TAB)

edad= int(input('Ingresa tu edad: '))

if (edad > 18):
    # todo lo que escriba aca adentro
    print('La persona es mayor de edad')
    # la alineacion nunca debe de variar si estamos en el mismo bloque de codigo
    print('otra impresion')
# se utiliza si la primera condicion fallo pero queremos hacer una segunda condicion
elif edad > 15:
    print('Puedes ingresar a la preparatoria')
elif edad > 10:
    print('Puedes vacunarte con la vacuna')
# # el else es completamente opcional y no siempre se debe utilizar con un if
else:
    print('Eres muy niño')

print('finalizo el programa')


# Validar si un numero (ingresos de una persona) ingresado por teclado es :
# * mayor a 500: indicar que no recibe el bono yanapay
# * entre 500 y mayo o igual que 250: indicar que si recibe el bono
# * es menor que 250: indicar que recibe el bono y un balon de gas
# RESOLUCION DEL EJERCICIO
ingreso = int(input('Ingrese su ingreso: '))
if ingreso > 500:
    print('No recibe el bono yanapay')
elif ingreso >= 250 and ingreso <= 500:
    print('Recibes el bono yanapay')
else:
    print('Recibe el bono y ademas su balon de gas') 

    