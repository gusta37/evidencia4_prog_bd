USE Simulador_de_vuelo;

CREATE TABLE piloto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    licencia VARCHAR(50)
);

CREATE TABLE destino (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    coordenadas VARCHAR(50) -- Puedes almacenar información como latitud y longitud
);

CREATE TABLE vuelo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    altitud INT,
    velocidad INT,
    direccion VARCHAR(10),
    piloto_id INT,
    destino_id INT,
    FOREIGN KEY (piloto_id) REFERENCES piloto(id),
    FOREIGN KEY (destino_id) REFERENCES destino(id)
);

INSERT INTO piloto (nombre, licencia) VALUES ('Juan Pérez', 'LIC12345');
INSERT INTO piloto (nombre, licencia) VALUES ('Ana Gómez', 'LIC67890');
INSERT INTO piloto (nombre, licencia) VALUES ('Luis Fernández', 'LIC54321');

INSERT INTO destino (nombre, coordenadas) VALUES ('Nueva York', '40.7128° N, 74.0060° W');
INSERT INTO destino (nombre, coordenadas) VALUES ('Los Ángeles', '34.0522° N, 118.2437° W');
INSERT INTO destino (nombre, coordenadas) VALUES ('Chicago', '41.8781° N, 87.6298° W');

INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (10000, 500, 'norte', 1, 1);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (8000, 450, 'sur', 2, 2);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (5000, 400, 'este', 3, 3);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (2000, 350, 'oeste', 1, 1);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (10000, 600, 'norte', 2, 2);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (7000, 470, 'sur', 3, 3);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (4000, 390, 'este', 1, 1);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (3000, 370, 'oeste', 2, 2);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (9000, 550, 'norte', 3, 3);
INSERT INTO vuelo (altitud, velocidad, direccion, piloto_id, destino_id) VALUES (6000, 460, 'sur', 1, 1);

SELECT * FROM vuelo;

SELECT * FROM vuelo WHERE altitud > 5000;

SELECT * FROM vuelo WHERE direccion = 'norte';

SELECT * FROM vuelo WHERE velocidad > 400;

SELECT * FROM vuelo ORDER BY altitud DESC LIMIT 1;

SELECT vuelo.*, piloto.nombre AS piloto_nombre, piloto.licencia, destino.nombre AS destino_nombre, destino.coordenadas
FROM vuelo
JOIN piloto ON vuelo.piloto_id = piloto.id
JOIN destino ON vuelo.destino_id = destino.id;

