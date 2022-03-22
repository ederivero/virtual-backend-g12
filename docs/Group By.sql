SELECT * FROM recetas LIMIT 1 OFFSET 5;
-- COUNT > contara todos los items de una tabla indicando que 
-- columna se desea usar como contador
SELECT COUNT(*) FROM recetas;
-- 5 facil , 2 dificil , 2 intermedio
SELECT COUNT(dificultad), dificultad FROM recetas GROUP BY dificultad, nombre;

-- Cuando usamos un AGGREGATE FUNCTION (funcion de agregacion) si queremos hacer una
-- clasificacion dependiendo del valor que este en determinada columna entonces
-- tenemos que usar la clausula adicional GROUP BY en la cual agrupara los resultados
-- de una manera independiente 
-- El GROUP BY es OBLIGATORIO cuando se usa una AG en los motores de bd POSTGRESQL, MSSQL, ORACLE(algunas)