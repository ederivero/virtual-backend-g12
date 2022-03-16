use colegios;

START TRANSACTION;

UPDATE alumnos SET nombre = 'eduardo' WHERE id=54;

SELECT * FROM alumnos where id= 54;

DELETE FROM alumnos where id = 63;

SELECT * FROM alumnos where id= 63;

-- Si todo estuvo bien y no hubieron problemas entonces se guardaran los cambios
-- de manera permanente:
COMMIT;

-- Si hubo algun error y no permitio continuar entonces se retrocederan todos
-- los cambios realizados hasta la fecha
ROLLBACK;


SELECT * FROM alumnos where id= 54;
SELECT * FROM alumnos where id= 63;