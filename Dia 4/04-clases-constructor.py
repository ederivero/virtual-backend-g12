class Animal:
    # metodo constructor: este metodo se llamara cuando vayamos a crear una nueva instancia de la clase
    def __init__(self, nombre, sexo, nro_patas):
        # crear unos nuevos atributos dentro de la clase y estos ya no seran staticos
        self.nombre = nombre
        self.sexo = sexo
        self.patas = nro_patas

    def descripcion(self):
        # si queremos que los atributos que vamos a utilizar sean creados y puedan ser accedidos desde cualquier parte de la instancia de la clase entonces los deberemos de crear en el constructor 
        return 'Yo soy un {2}, soy {1}, y tengo {0} patas'.format(
            self.patas,  #0
            self.sexo,   #1
            self.nombre, #2
            )

foca = Animal('Foca', 'M', 2)
caballo = Animal('Caballo','M', 4)
gato = Animal('Gato','F', 4)

print(foca.descripcion())
print(caballo.descripcion())
print(gato.descripcion())
