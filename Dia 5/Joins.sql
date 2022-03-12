-- JOINS
-- es la manera de ingresar desde una tabla hacia otra mediante una col en comun
USE prueba;
-- el uso de los joins solamente se podra realizar en el bloque de FROM
-- Devuelvem todas las columnas de la tabla vacunatorios haciendome una interseccion
-- con la tabla vacunas en la que sea igual su col (vacunatorio)vacuna_id = (vacunas)id

SELECT * FROM vacunas;
SELECT * 
FROM VACUNATORIOS INNER JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;
-- WHERE vacuna_id = 1;

-- LEFT JOIN
-- traera todo el contenido de la tabla de la izq y adicionalmente el contenido de interseccion
-- con la tabla de la derecha
SELECT *
FROM VACUNATORIOS LEFT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;


-- RIGHT JOIN
-- traera todo el contenido de la tabla de la der y adicionalmente el contenido de interseccion
-- con la tabla de la izquierda
SELECT *
FROM VACUNATORIOS RIGHT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;

-- FULL OUTER JOIN
-- traera toda la informacion tanto de la tabla de la izq como de la derecha y opcionalmente si hay alguna
-- interseccion lo hara sino no importa
SELECT *
FROM VACUNATORIOS LEFT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id UNION
SELECT *
FROM VACUNATORIOS RIGHT JOIN VACUNAS ON VACUNATORIOS.vacuna_id = VACUNAS.id;


INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
						 ('POSTA JOSE GALVEZ', 14.26598, 32.2569, 'AV. EL SOL 755', 'LUN-VIE 15:00 22:00', null, null); 

-- Si se usa en la clausula WHERE o en el SELECT una columna ambigua (que se repite el mismo nombre) hay que especificar
-- de que tabla estamos hablando
SELECT vacu.nombre, vac.nombre
FROM VACUNATORIOS vac JOIN VACUNAS AS vacu ON vac.vacuna_id = vacu.id
WHERE vacu.nombre = 'Pfizer';

-- tambien se puede colocar alias a las tablas para evitar escribir su nombre en su totalidad o escribir un nombre
-- mas entendible con la palabra AS (opcional)

-- 1. Devolver todos los vacunatorios en los cuales la vacuna sea Sinopharm y su horario de atencion sea de LUN-VIE
SELECT * 
FROM vacunatorios JOIN vacunas on vacunatorios.vacuna_id = vacunas.id
WHERE vacunas.nombre='SINOPHARM' AND horario_atencion LIKE '%LUN-VIE%';

-- 2. Devolver solamente las vacunas cuyo vacunatorio este ubicado entre la latitud -5.00 y 10.00
SELECT vacunas.nombre
FROM vacunatorios JOIN vacunas on vacunatorios.vacuna_id = vacunas.id
WHERE latitud BETWEEN -5 AND 10 ;

SELECT vacunas.nombre
FROM vacunatorios JOIN vacunas on vacunatorios.vacuna_id = vacunas.id
WHERE latitud > -5 AND latitud < 10 ;

-- 3. Devolver todas las vacunas que no tengan vacunatorio y solamente mostrar su procedencia y nombre
SELECT procedencia, vacunas.nombre 
FROM vacunatorios RIGHT JOIN vacunas on vacunatorios.vacuna_id = vacunas.id
WHERE vacuna_id IS NULL;


