CREATE TABLE users(
	id varchar(16) PRIMARY KEY,
	name varchar (250),
	user varchar (30),
	email varchar (70) unique,
	status numeric,
	type numeric,
	passwd varchar (532)

);

CREATE TABLE proveedores(
	id varchar(16) PRIMARY KEY,
	name varchar (16),
	RFC varchar (12) unique,
	legalName varchar(250),
	legalAddress varchar (250),
	active boolean
);

CREATE TABLE color(
	id varchar(16) PRIMARY KEY,
	name varchar(40),
	primaryColorCode varchar(6),
	secondaryColoir varchar(6)
);

CREATE TABLE talla(
	id varchar(16) PRIMARY KEY,
	size varchar (5),
	chest NUMERIC(5,2),
	length NUMERIC(5,2),
	gender char(1)
);
CREATE TABLE playera(
	id varchar(16) PRIMARY KEY,
	name varchar (160),
	ASIN varchar (16) unique,
	material varchar(30),
	idProveedor varchar(16), 
	FOREIGN KEY  (idProveedor) REFERENCES proveedores(id)
);
CREATE TABLE estampado(
	id varchar(16) PRIMARY KEY,
	name varchar (160),
	UnitaryPrice numeric (8,2),
	material varchar(40),
	heigth NUMERIC(5,2),
	width NUMERIC(5,2)
);

Create TABLE product (
	id varchar(16) PRIMARY KEY,
	playeraId varchar(16),
	FOREIGN KEY (playeraId) REFERENCES playera(id)
);

CREATE TABLE playera_color(
	playeraId varchar(16),
	colorId varchar(16),
	PRIMARY KEY (playeraId,colorId),
	FOREIGN KEY (playeraId) REFERENCES playera(id),
	FOREIGN KEY (colorId) REFERENCES color(id)
);
CREATE TABLE playera_talla(
	playeraId varchar(16),
	tallaId varchar(16),
	PRIMARY KEY (playeraId,tallaId),
	FOREIGN KEY (playeraId) REFERENCES playera(id),
	FOREIGN KEY (tallaId) REFERENCES talla(id)
);

CREATE TABLE product_estampado(
	productId varchar(16),
	estampadoId varchar(16),
	PRIMARY KEY (productId,estampadoId),
	FOREIGN KEY (productId) REFERENCES product(id),
	FOREIGN KEY (estampadoId) REFERENCES estampado(id)
);