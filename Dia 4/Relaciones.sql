CREATE TABLE vacunas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL ,-- nombre que no se pueda repetir y que no admita valores vacios
    estado BOOL DEFAULT TRUE, -- estado que solo acepte bools [su valor por defecto sea true]
    fecha_vencimiento DATE, -- fecha_vencimiento fecha
    procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'), -- procedencia sus valores pueden ser USA, CHINA, RUSIA, UK
    lote VARCHAR(10) -- lote no puede superara los 10 caracteres
);

CREATE TABLE vacunatorios (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    latitud FLOAT,
    longitud FLOAT,
    direccion VARCHAR(200),
    horario_atencion VARCHAR(100),
    -- La llave foranea (FK Foreign Key) es la representacion de la relacion entre la otra tabla e indicara todo su contenido
    -- representado solo por su id
    vacuna_id INT,
    FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);

-- DDL Data Definition Language > se usara para la definicion de donde se almaceran los datos en mi bd
-- Para Renombrar una tabla con un nuevo nombre
-- RENAME TABLE valor_antiguo TO nuevo_valor;
-- CREATE TABLES | CREATE DATABASE 
-- DROP elimina la tabla y su contenido a diferencia del DELETE que solo elimina el contenido
-- DROP TABLE vacunatorios;
-- DROP DATABASE prueba;

-- Eliminara la columna de la tabla y perderemos todos los datos que hubiesen en ella
-- ALTER TABLE vacunatorios DROP COLUMN latitud;

-- Agregara una nueva columna indicando el tipo de dato 
-- No podemos agregar valores por defecto a los tipos de datos BLOB, TEXT, GEOMETRY o JSON
ALTER TABLE vacunatorios ADD COLUMN imagen VARCHAR(100) DEFAULT 'imagen.png' AFTER horario_atencion;

-- RENAME COLUMN > renombra la columna
ALTER TABLE vacunatorios RENAME COLUMN imagen TO foto;
-- ALTER TABLE vacunatorios CHANGE imagen foto VARCHAR(100) DEFAULT 'imagen.png'; -- Para versiones de mysql 5.6.x hasta 5.7.x
-- MODIFY COLUMN > cambiar el tipo de dato y los configuraciones adicionales 
-- NO PODREMOS CAMBIAR EL TIPO DE DATO si ya hay informacion en esa columna y no corresponde con el nuevo tipo de dato
-- ALTER TABLE vacunatorios MODIFY COLUMN imagen INT UNIQUE NOT NULL ;

-- Un vacunatorio podra tener una sola vacuna pero una vacuna puede estar presente en varios vacunatorios
-- vacunas < vacunatorios

-- SOLO FUNCIONA EN MYSQL 
DESC vacunatorios;





