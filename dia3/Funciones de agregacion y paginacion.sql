-- FUNCIONES DE AGREGACION
-- Funciones que permiten efectuar operaciones sobre algunas columnas para obtener resultados

USE minimarket;
SELECT * FROM productos;

-- Para utilizar cualquier funcion de agregacion se tien que indicar la clausula GROUP BY y esta clausula 
-- servira para indicar como queremos que se realice la agrupacion antes de utilizar funcion
-- si solamente queremos obtener un solo resultado  entonces la clausula GROUP BY no se puede tomar en consideracion

-- AVG( COLUMNA )
SELECT categoria_id, AVG(precio) 
FROM productos
GROUP BY categoria_id;

-- MAX (COLUMNA) > El valor maximo de esa columna
SELECT MAX(precio)
FROM productos;

-- MIN (columna)
SELECT MIN(precio)
FROM productos;

-- COUNT (columna) > cuenta los registros que tenemos
SELECT COUNT(precio)
FROM productos;

-- SUM (columna) > suma el contenido de esa columna
-- PostgresSQL o SQL Server intentamos hacer una sumatoria de una columna que no es numeriaca arroja un error
SELECT SUM(precio)
FROM productos;

-- PAGINACION
SELECT * FROM productos
LIMIT 2 -- Indica cuantos quiero devolver
OFFSET 4; -- Indica cuantos quiero 'Saltarme' para empenzar

-- ORDENAMIENTO
SELECT * FROM productos
ORDER BY fecha_vencimiento DESC,nombre DESC; -- ASC >Ascendente| DESC > Descendente


-- En MySQL obligatoriamente para utilizar el OFFSET debemos indicar el LIMIT
SELECT SUM(p.precio)
FROM productos AS p INNER JOIN categorias AS c ON p.categoria_id = c.id
WHERE c.nombre= 'Otros'
GROUP BY p.id
ORDER BY fecha_vencimiento DESC
LIMIT 1
OFFSET 0;
