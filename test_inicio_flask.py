import unittest
from app import app
from datetime import datetime


class TestInicioFlask(unittest.TestCase):
    def setUp(self):
        # en vez del constructor en las clases comun y corrientes, en los test se usa el metodo setUp que servira para configurar todas los atributos y demas cosas que vayamos a utilizar en los escenarios de test de esta clase (metodos)
        self.nombre = 'Eduardo'
        # inicia mi aplicacion de flask usando un cliente de test, aceptara peticiones http para probar los endpoints y toda la aplicacion en general, esto levantara los modelos y hara la conexion a la bd entre otras cosas
        self.aplicacion_flask = app.test_client()

    @unittest.skip('Lo salte porque solamente queria ver el funcionamiento del metodo setUp')
    def testNombre(self):
        self.assertEqual(self.nombre, 'Eduardo')

    def testEndpointStatus(self):
        '''deberia retornar la hora del servidor y su estado'''
        respuesta = self.aplicacion_flask.get('/status')
        # el body de la respuesta lo obtenemos de respuesta.json el cual nos devolvera un diccionario con el json de la rpta
        # print(respuesta.json)
        # https://strftime.org/
        self.assertEqual(respuesta.status_code, 200)
        self.assertEqual(respuesta.json.get('status'), True)
        self.assertEqual(respuesta.json.get('hora_del_servidor'),
                         datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def testLoginJWTExitoso(self):
        '''deberia retornar una token para poder ingresar a las rutas protegidas'''
        # Mocks
        body = {
            'correo': 'ederiveroman@gmail.com',
            'pass': 'Welcome123!'
        }

        respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
        self.assertEqual(respuesta.status_code, 200)
        # respuesta.json.get('access_token') != None
        self.assertNotEqual(respuesta.json.get('access_token'), None)

    def testLoginJWTCredencialesIncorrectas(self):
        '''deberia retornar un error si las credenciales son incorrectas'''
        body = {
            'correo': 'ederiveroman@gmail.com',
            'pass': 'Welcome123asdasdasd!'
        }

        respuesta = self.aplicacion_flask.post('/login-jwt', json=body)
        # hacer las suposiciones correspondientes
        self.assertEqual(respuesta.status_code, 401)
        self.assertEqual(respuesta.json.get('access_token'), None)
        self.assertEqual(respuesta.json.get(
            'description'), 'Invalid credentials')
