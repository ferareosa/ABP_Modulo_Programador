-- Crear un nuevo usuario administrador
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin';

-- Otorgar todos los privilegios al usuario
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;

-- Aplicar los cambios de privilegios
FLUSH PRIVILEGES;

-- Creación de base de datos 
CREATE DATABASE IF NOT EXISTS skyroute;
USE skyroute;

-- Tabla Cliente
CREATE TABLE Cliente (
    cuit BIGINT PRIMARY KEY,
    razon_social VARCHAR(100),
    email VARCHAR(100)
);

-- Tabla Destino
CREATE TABLE Destino (
    id_destino VARCHAR(6) PRIMARY KEY,
    ciudad VARCHAR(100),
    pais VARCHAR(100),
    costo_base DECIMAL(10,2),
    disponible BOOLEAN
);

-- Tabla Pasaje
CREATE TABLE Pasaje (
    id_venta INT PRIMARY KEY,
    cuit BIGINT,
    id_destino VARCHAR(6),
    fecha_venta VARCHAR(20),
    estado BOOLEAN,
    costo_total DECIMAL(10,2),
    FOREIGN KEY (cuit) REFERENCES Cliente(cuit),
    FOREIGN KEY (id_destino) REFERENCES Destino(id_destino)
);

-- Datos de ejemplo

-- Clientes
INSERT INTO Cliente (cuit, razon_social, email) VALUES
(20123456789, 'Empresa A S.A.', 'contacto@empresaa.com'),
(27876543210, 'Empresa B SRL', 'info@empresab.com');

-- Destinos
INSERT INTO Destino (id_destino, ciudad, pais, costo_base, disponible) VALUES
('ArgBue', 'Buenos Aires', 'Argentina', 15000.00, TRUE),
('ChiSan', 'Santiago', 'Chile', 18000.00, TRUE),
('PerLim', 'Lima', 'Perú', 20000.00, FALSE);

-- Pasajes
INSERT INTO Pasaje (id_venta, cuit, id_destino, fecha_venta, estado, costo_total) VALUES
(1001, 20123456789, 'ArgBue', '2025-06-01', TRUE, 15000.00),
(1002, 27876543210, 'ChiSan', '2025-06-02', TRUE, 18000.00),
(1003, 20123456789, 'PerLim', '2025-06-03', FALSE, 20000.00);