-- Crear un nuevo usuario administrador
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

-- Otorgar todos los privilegios al usuario
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;

-- Creación de base de datos 
CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

-- Crear tabla Cliente
CREATE TABLE Cliente (
    cuit BIGINT PRIMARY KEY,
    razon_social VARCHAR(100),
    email VARCHAR(100)
);

-- Crear tabla Destino
CREATE TABLE Destino (
    id_destino INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(100),
    pais VARCHAR(100),
    costo_base DECIMAL(10,2),
    disponible BOOLEAN
);

-- Crear tabla Pasaje
CREATE TABLE Pasaje (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    cuit BIGINT,
    id_destino INT,
    fecha_venta VARCHAR(20),
    estado BOOLEAN,
    costo_total DECIMAL(10,2),
    FOREIGN KEY (cuit) REFERENCES Cliente(cuit) ON DELETE CASCADE,
    FOREIGN KEY (id_destino) REFERENCES Destino(id_destino)
);

-- Establecer valor inicial de AUTO_INCREMENT
ALTER TABLE Destino AUTO_INCREMENT = 1001;
ALTER TABLE Pasaje AUTO_INCREMENT = 1001;

--DATOS DE EJEMPLO:

-- Insertar datos en Cliente
INSERT INTO Cliente (cuit, razon_social, email) VALUES
(20123456789, 'Empresa A S.A.', 'contacto@empresaa.com'),
(27876543210, 'Empresa B S.R.L.', 'info@empresab.com'),
(27876543227, 'Empresa C S.A.S.', 'pepe@pepito.com');

-- Insertar datos en Destino
INSERT INTO Destino (ciudad, pais, costo_base, disponible) VALUES
('Buenos Aires', 'Argentina', 15000.00, TRUE),
('Santiago', 'Chile', 18000.00, TRUE),
('Lima', 'Perú', 20000.00, FALSE);

-- Insertar datos en Pasaje
INSERT INTO Pasaje (cuit, id_destino, fecha_venta, estado, costo_total) VALUES
(20123456789, 1001, '01/06/2024', TRUE, 15000.00),
(27876543210, 1002, '02/06/2025', TRUE, 18000.00),
(20123456789, 1003, '03/06/2025', FALSE, 20000.00);