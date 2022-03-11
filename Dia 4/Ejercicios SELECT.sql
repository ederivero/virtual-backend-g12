-- INSERTAR DATA
USE prueba;
-- En bases de datos y lenguajes de programacion se usa el ISO 8601 https://es.wikipedia.org/wiki/ISO_8601
INSERT INTO vacunas (nombre, estado, fecha_vencimiento, procedencia, lote) VALUES
					('PFIZER', true, '2022-08-16', 'USA', '123jkl'),
                    ('SINOPHARM', true, '2022-10-10', 'CHINA', 'vxcvxc'),
                    ('MODERNA', true, '2022-09-14', 'USA', 'zxczxc'),
                    ('SPUTNIK', false, '2022-10-04', 'RUSIA', 'ghjkhjfg');

INSERT INTO vacunatorios (nombre, latitud, longitud, direccion, horario_atencion, foto, vacuna_id) VALUES
						('CAMINO REAL', 14.121, -21.121, 'AV GIRASOL 115', 'LUN-VIE 07:00 - 15:00', null, 1),
                        ('HOSP. GNRAL.', 17.521, 11.1891, 'AV CIRCUNVALACION S/N', 'LUN-VIE 07:00 - 15:00', 'hospital.jpg', 2),
                        ('POSTA CERRO AZUL', 11.258, 67.447, 'AAHH LOS QUERUBINES LOTE 3 MZ J', 'LUN-SAB 07:00 - 15:00', 'foto01.png', 1),
                        ('ESTADIO LOS PALITOS', 24.121, -21.121, 'CALLE ESPINOSA 1115', 'LUN-MIE-VIE 07:00 - 15:00', 'est0001.jpg', 3),
                        ('PLAZA DEL AMOR', 4.116, -21.121, 'AV DE LOS HEROES ANONIMOS S/N', 'LUN-VIE 07:00 - 15:00', null, 1);
                        
                        
                        
-- 1. Mostrar los nombres de las vacunas
SELECT nombre FROM vacunas;
-- 2. Mostrar las vacunas que sean de procedencia USA
SELECT * FROM vacunas WHERE procedencia = 'USA';
-- 3. Mostrar las vacunas que NO sean de procedencia USA != | NOT LIKE | <> | NOT campo = '...'
SELECT * FROM vacunas WHERE procedencia != 'USA';
-- 4. Mostrar las vacunas que en su lote tengan los digitos 'xc'
SELECT * FROM vacunas WHERE lote LIKE '%xc%';
-- 5. Mostrar todos los vacunatorios que tengan horario de atencion los dias miercoles
SELECT * FROM vacunatorios WHERE horario_atencion LIKE '%MIE%' 
							OR horario_atencion LIKE '%LUN-VIE%' 
							OR horario_atencion LIKE '%LUN-SAB%';
-- 6. Mostrar todos los vacunatorios que tengan la vacuna_id 1 pero que tengan foto
SELECT * FROM vacunatorios WHERE vacuna_id = 1 AND foto IS NOT NULL; 
