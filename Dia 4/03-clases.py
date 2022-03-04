# Programacion Orientada a Objetos > POO | OOP
# la programacion debe estar creada en base a clases
# toda parte del codigo debe de ser tratada como si fuese una plantilla 
# clases > son plantillas para que puedan ser utilizadas varias veces sin la necesidad de modificar su forma en relacion al objeto sino que al revez 

class Persona:
    # las variables creadas dentro de la clase pasan a llamarse atributos
    fec_nac = '2000-01-01'
    nombre = 'Juan'
    soltero= True
    estatura = 1.50
    # las acciones que puede tener una clase se definen como funciones, pero una funcion al ser creada dentro de una clase pasa a llamarse metodo
    # en cada metodo siempre como primer parametro obligatoriamente se utiliza la palabra self sirve para hacer referencia dentro de la instancia a los atributos y metodos de esa misma instancia para que haga uso de esa copia y que posiblemente no traiga la informacion estatica de la clase
    def saludar(self):
        self.decir_nombre()
        self.fec_nac
        print('Hola como estan')
        return 'hola {}'.format(self.nombre)

    def decir_nombre(self):
        print('digo el nombre')

# cuando una variable se crea a raiz de una clase, esta variable pasa a llamar instancia (instancia > copia en su totalidad de la clase)
persona1 = Persona()
persona2 = Persona()
# modificamos el valor origina del atributo a uno personalizado
persona2.nombre = 'Eduardo'
persona1.nombre = 'Carolina'
persona2.nombre = 'Josue'
persona2.saludar()
print(persona1.nombre)
# sobre escribimos el valor predeterminado del atributo nombre a uno nuevo y esto generara que si las instancias que siguen usando el atributo con su valor original cambien a este nuevo valor ya que es un atributo estatico
Persona.nombre = 'Roberto'
print(persona1.nombre)
# Un atributo estatico es un atributo que puede ser accedido sin la necesidad de crear una instancia
# por defecto en python cualquier atributo creado a nivel de la clase es un atributo estatico
print(Persona.nombre)
print(persona2.nombre)