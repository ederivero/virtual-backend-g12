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
    nombre varchar(100) not null,
    apellido_paterno varchar(45),
    apellido_materno varchar(45),
    correo varchar(45) unique ,
    numero_emergencia varchar(20) not null
);

CREATE TABLE IF NOT EXISTS niveles(
	id INT PRIMARY KEY AUTO_INCREMENT,
    seccion varchar(45) not null,
    ubicacion varchar(45),
    nombre varchar(45) not null
);

CREATE TABLE IF NOT EXISTS alumnos_niveles(
	id INT PRIMARY KEY AUTO_INCREMENT,
    alumno_id int,
    nivel_id int,
    fecha_cursada year,
    FOREIGN KEY(alumno_id) REFERENCES alumnos(ID),
    FOREIGN KEY(nivel_id) REFERENCES niveles(ID)
);

