
-- Crear tabla de movilidad
CREATE TABLE movilidad (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE,
    region VARCHAR(50),
    retail INT,
    grocery INT,
    parks INT,
    transit INT,
    workplace INT,
    residential INT
);

-- Insertar datos para San Salvador
INSERT INTO movilidad (fecha, region, retail, grocery, parks, transit, workplace, residential)
VALUES ('2022-10-15', 'San Salvador', 47, 61, 10, 34, 33, 1);
