# encapsulamiento > es declara tipos de accesibilidad a los atributos y metodos
class Producto:
    def __init__(self, nombre, precio):
        # existen 3 tipos de accesibilidad a los atributos y metodos de una clase: public 
        self.nombre = nombre
        self.precio = precio
        # privado : cuando se define un atributo con '__' estaremos indicando que esta sera de caracter privado osea que no podra ser accedido desde fuera de la clase ni siquiera su misma instancia podra acceder
        # un atributo sera privado cuando no es necesaria la interaccion con un agente externo
        self.__ganancia = self.precio * 0.30
        # protegido protected: 
        # self.__beneficios = True if self.precio > 500 else False
    
    def mostrar_info(self):
        return {
            'nombre': self.nombre,
            'precio': self.precio,
            'ganancia': self.__ganancia,
            # {:.3f} estaremos indicando que convertiremos este valor a string y solamente lo limitaremos a tener 3 decimales, obviamente redondeara estos valores
            'igv': '{:.3f}'.format(self.__calcular_igv()),
            # 'beneficios': self.__beneficios
        }

    def aumentar_ganancia(self):
        self.__ganancia = self.__ganancia * 1.10
    
    def __calcular_igv(self):
        resultado = self.precio * 0.18
        return resultado

cepillo = Producto('Cepillo dental', 3.80)
# atributo publico = porque puedo acceder a este tanto desde la misma clase como en su instancia
cepillo.nombre
# atributo privado = solamente podra ser accedido a el dentro de la misma clase pero no desde su instancia
cepillo.__ganancia = 100
# cepillo.__calcular_igv()
print(cepillo.mostrar_info())
cepillo.aumentar_ganancia()
print(cepillo.mostrar_info())