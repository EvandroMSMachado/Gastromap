DROP DATABASE IF EXISTS db_gastromap;


CREATE DATABASE db_gastromap;

USE db_gastromap;

CREATE TABLE employers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(20) NOT NULL
);

CREATE TABLE patient (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    password VARCHAR(20) NOT NULL
);

CREATE TABLE form (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_patient INT NOT NULL,
    uva INT DEFAULT NULL,
    tapioca INT DEFAULT NULL,
    requeijao INT DEFAULT NULL,
    tomate INT DEFAULT NULL,
    repolho INT DEFAULT NULL,
    sorv_picole INT DEFAULT NULL,
    salgadinho INT DEFAULT NULL,
    energeticos INT DEFAULT NULL,
    form_finaliz BOOLEAN DEFAULT 0,
    FOREIGN KEY (id_patient) REFERENCES patient (id)
);


