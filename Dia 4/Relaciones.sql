CREATE TABLE vacunaciones(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) UNIQUE NOT NULL ,-- nombre que no se pueda repetir y que no admita valores vacios
    estado BOOL DEFAULT TRUE, -- estado que solo acepte bools [su valor por defecto sea true]
    fecha_vencimiento DATE, -- fecha_vencimiento fecha
    procedencia ENUM('USA', 'CHINA', 'RUSIA', 'UK'), -- procedencia sus valores pueden ser USA, CHINA, RUSIA, UK
    lote VARCHAR(10) -- lote no puede superara los 10 caracteres
);

CREATE TABLE vacunatorio (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    latitud FLOAT,
    longitud FLOAT,
    direccion VARCHAR(200),
    horario_atencion VARCHAR(100)
);