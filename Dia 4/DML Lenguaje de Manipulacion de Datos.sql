USE prueba;

-- Sub parte de SQL: 
-- DML: Data Manipulation Language (Lenguaje de Manipulacion de Datos)
-- Se utiliza para la manipulacion de la informacion dentro de una base de datos
-- INSERT, SELECT, UPDATE, DELETE

INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					 ('Eduardo','73500746', 'DNI', true);

INSERT INTO clientes (nombre, documento, tipo_documento, estado) VALUES
					('Estefani','15945675', 'DNI', true),
                    ('Fabian','1594987896', 'RUC', false);

-- SELECT : es el comando que sirve para visualizar la informacion de una determinada tabla o tablas

-- SELECT col1, col2, ... FROM tabla;
SELECT nombre, documento FROM clientes;

--  si queremos observar todas las columnas de esa tabla(s)
SELECT * FROM clientes;

-- 						WHERE col_nombre = valor > < >= <=
-- al usar parentesis en una condicional hara que esas condiciones internas se ejecuten primero para
-- luego recien el resultado se compare con la condicion externa
SELECT * FROM clientes WHERE documento = '73500746' AND (nombre = 'Eduardo' OR nombre = 'Estefani');

-- Seleccionar a todas las personas que tiene DNI y que su estado sea true
SELECT * FROM clientes WHERE tipo_documento = 'DNI' AND estado = true;<

-- LIKE en columnas de string para hacer una similitud y ademas usaremos los '%' para indicar si no se sabe
-- en que parte exactamente esta esa letra o letras
SELECT * FROM clientes WHERE nombre LIKE 'Edu%o';

-- UPDATE sirve para actualizar uno o varios registros de una determinada tabla
-- UPDATE tabla SET col=nuevo_valor , ....   WHERE col=val;
UPDATE clientes SET nombre = 'Ramiro', documento = '33333568' WHERE nombre= 'Eduardo';

-- Modo seguro > es el modo que nos impide hacer actualizaciones (UPDATE) y eliminaciones (DELETE) sin usar
-- una col que sea indice (o PK) 
-- Otra forma de acceder mediante el Workbench es en el menu Edit > Preferences > SQL Editor y al final estara
-- opcion para modificar
-- Para desactivar el modo seguro:
SET SQL_SAFE_UPDATES = false;


-- DELETE sirve para eliminar REGISTROS de una determinada tabla
DELETE FROM clientes WHERE id = 1;



SELECT * FROM clientes;



