CREATE TABLE IF NOT EXISTS Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    phone VARCHAR(50),
    website VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Direcciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    street VARCHAR(100),
    suite VARCHAR(50),
    city VARCHAR(100),
    zipcode VARCHAR(20), #codigo postal
    FOREIGN KEY (user_id) REFERENCES Usuarios(id)
);

CREATE TABLE IF NOT EXISTS Geolocalizacion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    direccion_id INT,
    lat VARCHAR(50), #latitud
    lng VARCHAR(50), #longitud
    FOREIGN KEY (direccion_id) REFERENCES Direcciones(id)
);

CREATE TABLE IF NOT EXISTS Empresas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    name VARCHAR(100),
    catchPhrase VARCHAR(255), #frase clave
    bs VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Usuarios(id)
);

CREATE TABLE IF NOT EXISTS Tareas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    titulo VARCHAR(100),
    completada BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (user_id) REFERENCES Usuarios(id)
);
