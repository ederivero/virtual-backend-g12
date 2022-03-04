# herencia > extraer informacion de una clase padre

# DRY > Don't Repeat Yourself (no te repitas a ti mismo)

class Usuario:
    def __init__(self, nombre, apellido, correo):
        self.nombre =  nombre
        self.apellido = apellido
        self.correo  = correo

    def saludar(self):
        return 'hola soy {}'.format(self.nombre)

# alumno ha heredado todos los atributos y metodos (comportamiento) de la clase padre (Usuario)
class Alumno(Usuario):
    def __init__(self, nombre, apellido, correo, padres):
        # forma de validar el tipo de dato de un parametro
        # if type(nombre) != 'str':
        #     raise Exception('Tipo invalido')

        # super() > sirve para mandar a llamar a la clase de la cual estamos haciendo la herencia para no volver a escribir la misma logica, ademas solamente servira para poder acceder a los metodos de la clase de la cual estamos heredando
        super().__init__(nombre, apellido, correo)
        self.padres = padres
    
    def info(self):
        return {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'padres': self.padres,
            'saludar': super().saludar()
        }

alumnoPedro = Alumno('Pedro', 'Flores', 'pflores@gmail.com',[{
    'nombre':'Wilber',
    'apellido':'Martinez'
},{
    'nombre':'Juliana',
    'apellido':'Perez'
}])

print(alumnoPedro.info())