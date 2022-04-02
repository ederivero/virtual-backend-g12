import unittest
# por defecto el patro del nombre de los archivos es test*.py, si queremos modificar el patron usaremos la configuracion -p | --pattern

# si queremos ver el detalle de nuestros casos de test usaremos -v | --verbose


def numero_par(numero: int):
    # retornar verdado si es par o falso si es impar
    return numero % 2 == 0


# todo escenario de testing (pruebas) sera basado en clases
class PruebaTest(unittest.TestCase):
    # la clase TestCase me permite hacer varios tipos de comparaciones y ademas le indicara a python que clase de testing debe hacer

    # cada escenario de prueba sera un metodo
    def test_sumatoria(self):
        numero1 = 1
        numero2 = 2
        resultado = numero1 + numero2
        # comprobar si numero1 + numero2 = 3
        self.assertEqual(resultado, 3)

    # si estamos concientes que el test va a fallar pero aun asi queremos mantenerlo tal y como esta, entonces podemos usar el decorador expectedFailure que no nos indicara un fallo pero que se espera el fallo
    @unittest.expectedFailure
    def test_resta(self):
        numero1 = 1
        numero2 = 2
        resultado = numero1 - numero2
        self.assertEqual(resultado, 3)


class NumeroParTest(unittest.TestCase):
    # los metodos siempre deben empezar con 'test_' porque si no lo colocamos no lo considerara al momento de hacer test
    def test_par(self):
        '''Debera retornar True si el numero es par'''
        # pasare un numero
        resultado = numero_par(2)
        self.assertEqual(resultado, True)

    def test_impar(self):
        '''Debera retornar False si el numero es impar'''
        resultado = numero_par(3)
        self.assertEqual(resultado, False)

    def test_error(self):
        '''Debera arrojar un error si se le pasa una letra en vez de un numero'''
        # pasare algo que no sea un numero
        # si se que el siguiente test fallara pero es parte del caso entonces puedo usar el assertRaises que lo que recibira sera el tipo de error que va a generar para poder testearlo
        with self.assertRaises(TypeError, msg='Error al ingresar un caracter en vez de un numero') as error:
            numero_par('a')

        self.assertEqual(
            error.msg, "Error al ingresar un caracter en vez de un numero")
