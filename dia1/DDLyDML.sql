USE practicas;
CREATE TABLE usuarios (
	id 		INT  	auto_increment unique key,
    nombre 	TEXT 	NOT NULL,
    DNI		CHAR(8) UNIQUE
);

CREATE TABLE tareas(
	id 			INT 			AUTO_INCREMENT PRIMARY key,
    titulo 		VARCHAR(100) 	UNIQUE,
    descripcion TEXT,
    usuario_id INT,
    -- CREO LA RELACION ENTRE LAS TABLAS 
    -- indico entre parentesis la columna de esta tabla y luego la tabla (su columna)
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
);
-- SUB LENGUAJES
-- DDL (Data Definition Languaje)
-- Es un lenguaje que sirve para definir estructuras de datos (Crear Bd, crear tablas,
-- actualizar tablas, eliminar tablas)
-- CREATE (Crear)
-- ALTER (Actualizar)
-- DROP (Eliminar) elimina absolutamente TODO

-- DML (Data Manipulation Language)
-- Es un lenguaje que sirve para definir la informacion que ira dentro de las estructuras
-- Insertar datos, actualizar datos, eliminar datos y leer datos.alter
-- INSERT (Insertar)
-- SELECT (Visualizar)
-- UPDATE (Actualizar)
-- DELETE (Eliminar)

INSERT INTO usuarios ( nombre, dni) VALUES ('ANTHONY','42036434');
-- Si queremos utilizar el valor por defecto de una columna
INSERT INTO usuarios (ID, nombre, dni) VALUES (default,'JUANA','42536434');

-- Si queremos ingresar varios usuarios
INSERT INTO usuarios (id, nombre, dni) VALUES (default, 'PEPE','45506434'),
											  (DEFAULT, 'MARIA','48494644'),
                                              (DEFAULT, 'JUANA','40494640');
INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES
				(default, 'ir a la playa','ire a la playa el fin de semana',1),
                (default, 'ir a la piscina','ire a la piscina en clases de natacion',2);
-- Visualizar la informacion
SELECT nombre,dni FROM usuarios;

-- Visualizar la totalidad de las columnas
SELECT * FROM usuarios;

INSERT INTO usuarios(id, nombre, dni)VALUES (default, 'Juana','12456598'),
											(default, 'Maria','03643442');
                                            
-- nombre columna seleciona todas las columnas donde nombre sea Juana
SELECT * FROM usuarios WHERE nombre='Juana' AND id= 4;

-- seleccion todas las tareas cuando se el usuario 1 y/o 2
SELECT * FROM tareas where usuario_id = 1 or usuario_id= 2;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'Ir a comer', 'Comer un sabroso pollito a la brasa', 1),
                                                                (DEFAULT, 'Comer pizza', 'Comer una sabrosa pizza con peperoni', 1);
   
-- buscar una palabra o palabras dentro de un texto   
SELECT * FROM tareas WHERE usuario_id=1 AND titulo LIKE '%comer%';
SELECT * FROM usuarios WHERE nombre LIKE '%Y';
SELECT * FROM usuarios WHERE nombre LIKE 'J%';

-- Si queremos hacer la distincion entre mayus y minus entonces antes de poner el texto colocaremos la palabra
-- BINARY y esto sirve para que haga la comparacion a nivel de numeros de caracteres (formato ASCII)
SELECT * FROM usuarios WHERE nombre LIKE BINARY 'j%';

-- _> indico cuando caracteres debe de "saltar"(ubicacion) para que busque el caracter indicado
SELECT * FROM usuarios WHERE nombre LIKE '_N%';

SELECT * FROM usuarios WHERE nombre NOT LIKE '_N%';

SELECT * FROM tareas;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'no hacer nada', 'no hacer nada porque es domingo', null);

SELECT * FROM tareas;

SELECT * FROM usuarios INNER JOIN tareas ON  usuarios.id = tareas.usuario_id;

INSERT INTO tareas (id, titulo, descripcion, usuario_id) VALUES (DEFAULT, 'Jugar LOL', 'Juagar con mis amigos pros',3);

-- Interseccion entre la tabla usuarios con la tabla tareas donde usuarios.id = tareas.usuario_id
SELECT * FROM usuarios INNER JOIN tareas ON usuarios.id = tareas.usuario_id;

SELECT * FROM usuarios LEFT JOIN tareas ON usuarios.id = tareas.usuario_id;

SELECT * FROM usuarios RIGHT JOIN tareas ON usuarios.id = tareas.usuario_id;

-- FULL OUTER JOIN
-- Selecciona todos los usuarios aun asi no tengan tareas y todas las tareas aun asi no tengan usuarios 
-- hace una mezcla completa entre los usuarios y las tareas respetando sus conexiones
SELECT * FROM usuarios LEFT JOIN tareas ON usuarios.id = tareas.usuario_id UNION
SELECT * FROM usuarios RIGHT JOIN tareas ON usuarios.id = tareas.usuario_id;

-- UNION mezcla o combina las dos o mas consultas en una sola 'tabla virtual' pero estas consultas tienen
-- que tener el mismo numero de columnas, sino 'el UNION' sera incorrecto
SELECT nombre FROM usuarios UNION
SELECT titulo FROM tareas;

-- CONCATENAR > juntar combinar

SELECT concat(titulo,' y tambien ', descripcion) AS 'Nombre completo'FROM tareas;

-- 1 Devolver todos los usuarios cuyo DNI contengan el numero 5
SELECT * FROM usuarios WHERE dni LIKE '%5%';

-- 2 Devolver todos los usuarios cuyo DNI tengan 3 digito 8
SELECT * FROM usuarios WHERE dni LIKE '__8%';

-- 3 Devolver todas las tareas del usuario Eduardo
SELECT * FROM usuarios INNER JOIN tareas ON  usuarios.id = tareas.usuario_id WHERE nombre='Eduardo';
