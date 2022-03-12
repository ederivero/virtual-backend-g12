# factory 
from faker import Faker
from random import randint, choice
# no es necesario definir que providers se utilizaran ya que por defecto al crear la instancia de la clase Faker internamente se cargan todos los providers standar
# from faker.providers import internet, person
fake = Faker()
# le agregamos un provider adicional a nuestro faker para que ahora pueda utilizar los tradicionales y los de internet
# fake.add_provider({internet, person})
# tanto el add_provider como el provider es necesario declararlo siempre que se este usando un standard provider (solamente sera necesario cuando sea un provider de la comunidad)

def generar_alumnos(limite):

    for persona in range(limite):
        nombre = fake.first_name()
        apePat = fake.last_name()
        apeMat = fake.last_name()
        correo = fake.ascii_free_email()
        # utilizando faker generar un numero aleatorio entre 911111111 hasta 999999999
        # telefono = fake.random_int(min=911111111, max=999999999)
        # fake.bothify(text='asd###??', letters='xdhola')
        telefono = fake.bothify(text='9########')
        # telefono = fake.phone_number()
        sql= '''INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES
                            ('%s', '%s', '%s', '%s', '%s');''' % (nombre, apePat, apeMat, correo, telefono)

        '''INSERT INTO alumnos (nombre, apellido_paterno, apellido_materno, correo, numero_emergencia) VALUES
                            ('{}', '{}', '{}', '{}', '{}');'''.format(nombre, apePat, apeMat, correo, telefono)
        print(sql)

def generar_niveles():
    secciones = ['A', 'B', 'C']
    ubicaciones = ['Sotano', 'Primer Piso', 'Segundo Piso', 'Tercer Piso']
    niveles = ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto']
    # iterar los niveles y en cada nivel colocar como minimo dos secciones y como maximo 3 (random_int) y luego agregar aleatoriamente la ubicacion a ese nivel
    # Primero A Segundo Piso
    # Primero B Tercer Piso
    # Segundo A Sotano
    for nivel in niveles:
                        # entre 2 hasta <= 3 (2 | 3)
        pos_secciones = randint(2, 3)
        # pos_secciones = fake.random_int(min=2, max=3)
        for posicion in range(0, pos_secciones):
            # pos_ubicacion = fake.random_int(min=0, max= 3)
            # ubicacion= ubicaciones[pos_ubicacion]
            ubicacion = choice(ubicaciones)
            seccion = secciones[posicion]
            nombre = nivel
            sql = '''INSERT INTO niveles (seccion, ubicacion, nombre) VALUES
                                    ('%s', '%s', '%s');''' % (seccion, ubicacion,nombre)
            # print('Nivel', nivel)
            # print('Seccion', secciones[posicion])
            # print('Ubicacion', ubicaciones[pos_ubicacion])
            print(sql)

def generar_niveles_alumnos():
    # generar un numero aleatorio que sera el id del alumno y el id del nivel y un anio de manera en la cual no se puede volver a generar ese mismo alumno con un nivel inferior pero con un anio superior
    # ALUMNO_ID    NIVEL_ID    YEAR
    #     1            3        2000   // 3 > segundo A 
    #     1            1        1999   // 1 > primero A ✔️
    #     1            1        2002   // 1 > primero A ❌
    # en total tiene que haber unos 80 registros
    
    pass


generar_niveles()