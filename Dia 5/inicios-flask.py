# no se puede crear un archivo con el mismo nombre de una libreria que vamos a utilizar
from flask import Flask
from datetime import datetime

# __name__ > muestra si el archivo es el archivo raiz o principal del proyecto, si el archivo es el archivo principal entonces el valor de __name__ sera __main__ porque estoy en el archivo principal de mi proyecto (el archivo del cual estoy iniciando todo) caso constrario sino es el archivo principal indicara otro valor
# print(__name__)
app = Flask(__name__)

# los decoradores es un patron de software que se utiliza para modificar el funcionamiento de un metodo o de una clase en particular sin la necesidad de emplear otros metodos como la herencia
@app.route('/')
# voy a modificar el comportamiento del metodo route para cuando su ruta sea '/' y su nuevo comportamiento sera el siguiente definido en la funcion inicial
def inicial():
    print('Me llamaron!')
    # siempre en los controladores tenemos que devolver una respuesta!
    return 'Bienvenido a mi API 🔌' 
    # Para abrir la ventana de emojis: 
    # Windows: Tecla Windows + .
    # Mac: Ctrl + Command + Spaciadora


@app.route('/api/info')
def info_app():
    # para dar un formato a la fecha se usar el metodo strftime() > string from time
    return {
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M:%S') # me devuelve la hora y fecha actual del servidor JS: new Date()
    }

# inicializaremos nuestro servidor de Flask
# debugging > significa que estamos en modo de prueba y que con ello cada vez que guardemos se reinicia el servidor automaticamente
app.run(debug=True)

print('Yo no me ejecuto')
# !!!!
# todo lo que declaremos luego de la llamada al metodo run() nunca se ejecutara ya que el metodo run() hace que el programa se quede 'colgado' esperando una peticion del cliente