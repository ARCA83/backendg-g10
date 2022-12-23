-- Asi se crea una base de datos
CREATE DATABASE IF NOT EXISTS practicas;

USE practicas;
-- ahora procederemos a crear nuestra primera tabla
CREATE TABLE usuarios (
-- nombre datatype 		[conf adicionales]
	id 		INT  	auto_increment unique key,
    nombre 	TEXT 	NOT NULL,
    DNI		CHAR(8) UNIQUE
);
