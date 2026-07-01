CREATE TABLE contactos (
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);

INSERT INTO contactos(nombre, primer_apellido, segundo_apellido, email, telefono)
VALUES
('Alvaro', 'Diaz', 'Rodriguez', 'alvarodiaz@gmail.com', '123456789'),
('Kanye', 'Omari', 'West', 'kanyewest@gmail.com', '1122334455'),
('Taylor', 'Alison', 'Swift', 'taylorswift@gmail.com', '198919889');

SELECT * FROM contactos;