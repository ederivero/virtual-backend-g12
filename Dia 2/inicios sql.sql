# SQL > Structured Query Language
# un registro es un conjunto de datos y un dato es 
# un valor que por si solo no dice nada
# las bd por buenas practicas su nombre debe estar en singular

CREATE DATABASE prueba;

# Para indicar que BD vamos a utilizar usamos el comando USE
USE prueba;

# el nombre de las tablas siempre debe de ser en plural (indicara que podremos tener
# varios registro de ese tipo
CREATE TABLE clientes(
	# Ahora definimos las columnas pertenecientes a esta tabla
    # debe haber al menos una columna por tabla es decir no puede existir una
    # tabla sin columnas
    # nombre_col  tipo_dato  [config adic.]
    # el PRIMARY KEY me permitira identificar este registro con otros en relacion
    # a sus tablas adyacentes
    id INT AUTO_INCREMENT PRIMARY KEY,
    # CHAR(n) > creara una columna que SIEMPRE ocupara n espacios de caracteres
    # VARCHAR(n) > crea una columna que podra tener COMO MAXIMO n caracteres y ocupara
    # solamente el espacio que necesita
    # TEXT > reservara el espacio dinamico segun sea necesario para el valor de esa 
    # columna PERO no tendra limite
    # por defecto todas las columnas que no se especifiquen su nulicidad aceptaran valores
    # nulos
    nombre VARCHAR(50) NOT NULL,
    # UNIQUE > significa que no se puede repetir este valor una vez ingresado en un registro
    # dni CHAR(8) UNIQUE,
    # carnet_extrajeria VARCHAR(10) UNIQUE,
    documento VARCHAR(10) UNIQUE,
    # ENUM > sera dependiendo de los posibles valores su tipo de dato
    tipo_documento ENUM('C.E.', 'DNI', 'RUC', 'PASAPORTE', 'C.M.', 'OTRO'),
    # BOOL > podra ser Verdadero o Falso
    estado BOOL
);






