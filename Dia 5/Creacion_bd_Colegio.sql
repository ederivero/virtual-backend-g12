-- Necesito una base de datos para almacenar los alumnos de mi colegio
-- mi colegio es solamente de primaria y solamente quiero almacenar
-- el alumno con su informacion que seria nombre, ape pat, ape mat, correo
-- numero de emergencia, y de cada seccion almacenar su nombre (A,B,C) y su 
-- ubicacion (SEGUNDO PISO, PRIMER PISO, SOTANO, etc)
-- por si acaso el alumno puede cambiar de seccion cada año pero almacenar su historial

CREATE DATABASE colegios;

USE colegios;

CREATE TABLE IF NOT EXISTS alumnos(
	id INT PRIMARY KEY AUTO_INCREMENT,
);

CREATE TABLE IF NOT EXISTS niveles(
	id INT PRIMARY KEY AUTO_INCREMENT,
);

CREATE TABLE IF NOT EXISTS alumnos_niveles(
	id INT PRIMARY KEY AUTO_INCREMENT,
);