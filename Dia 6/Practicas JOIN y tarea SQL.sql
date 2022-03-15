-- 1. Todos los alumnos que tienen correo GMAIL
use colegios;
SELECT * FROM alumnos WHERE correo LIKE '%@gmail.com';
-- 2. Todos los alumnos (nombre, ap_pat, ap_mat) que hayan cursado en el 2002
SELECT nombre, apellido_paterno, apellido_materno
FROM alumnos INNER JOIN alumnos_niveles ON alumnos.id = alumnos_niveles.alumno_id
WHERE fecha_cursada = 2002;
-- 3. Todos los grados donde su ubicacion sea el sotano o segundo piso
SELECT *
FROM niveles WHERE ubicacion IN('Sotano', 'Segundo Piso');
-- 4. Todos los grados (Seccion y el nombre ) que han tenido alumnos en el año 2003
SELECT seccion, nombre, fecha_cursada AS año
FROM niveles INNER JOIN alumnos_niveles ON niveles.id = alumnos_niveles.nivel_id
WHERE fecha_cursada = 2003;

-- NOTA: si no tienen esas secciones usar secciones que si tengan
-- 5. Mostrar todos los alumnos del quinto A
SELECT *
FROM alumnos JOIN alumnos_niveles ON alumnos.id = alumnos_niveles.alumno_id
			 JOIN niveles ON alumnos_niveles.nivel_id = niveles.id
WHERE niveles.nombre = 'Quinto' AND niveles.seccion='A';

-- 6. Mostrar todos los correos de los alumnos del primero B 
SELECT alumnos.correo
FROM alumnos JOIN alumnos_niveles ON alumnos.id = alumnos_niveles.alumno_id
			 JOIN niveles ON alumnos_niveles.nivel_id = niveles.id
WHERE niveles.nombre='Primero' AND niveles.seccion='B'; 