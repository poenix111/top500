-- Cantidad de entradas de cada pais, ordenada descendente
SELECT pais, COUNT(*) AS count FROM registros GROUP BY pais ORDER BY `count` DESC
-- Cantidad de entradas de cada pais, ordenada ascendente
SELECT pais, COUNT(*) AS count FROM registros GROUP BY pais ORDER BY `count` ASC
-- Cantidad de entradas de cada pais en especifico año
SELECT pais, COUNT(*) AS count FROM registros WHERE año = 2009 GROUP BY pais ORDER BY `count` DESC
-- Cantidad de entradas de cada pais desde el 2009
SELECT pais, COUNT(*) AS count FROM registros WHERE año >= 2009 GROUP BY pais ORDER BY `count` DESC
-- Cantidad de entradas de cada pais desde el 2009, limitando el resultado a 5
SELECT pais, COUNT(*) AS count FROM registros WHERE año >= 2009 GROUP BY pais ORDER BY `count` DESC LIMIT 5