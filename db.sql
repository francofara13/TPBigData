/*Facturacion y ventas*/

CREATE DATABASE Facturacion_venta ENCODING 'utf-8';

CREATE TABLE Departamentos (
    Id_depto int primary key,
    Nom_depto int NULL,
    Zona varchar NULL
);

CREATE TABLE Ciudades (
    Id_ciudad int primary key,
    Id_depto int not null, 
    Nom_ciudad varchar(50) not null, 
    Poblacion int not null,
    Clasificacion varchar(50)
);

CREATE TABLE Rubros (
    Id_rubro int primary key,
    Nom_rubro varchar(50) not NULL
);

CREATE TABLE Clientes (Id_cliente int primary key,
    Nombre varchar(50) not null,
    Direccion varchar(50) not null,
    Telefono varchar(50) not null,
    Ciudad int not null, /*FK*/
    Departamento int not null,/*FK*/
    Rubro varchar(50) not null,
    Categoria varchar(50) not null,
    Fecha_alta date not null
 )

CREATE TABLE Facturas (Factura int primary key,
    Fecha date not null,
    Cliente int not null, /*FK*/
    Vendedor int not null /*FK*/
);
CREATE TABLE Registros_Facturas (Factura int not null,
    Articulo int not null, /*double pk*/
    Importe int not null,
    Unidades int not null
);

ALTER TABLE Registros-Facturas ADD CONSTRAINT "ID_reg_fact" PRIMARY KEY (Factura, Articulo);


CREATE TABLE Articulos (Id_articulo int primary key,
    Id_producto int not null,/*FK*/
    Id_tamaño int not null
);

CREATE TABLE Productos (Id_producto int primary key,
    Id_familia int not null,
    Id_duracion int not null)

CREATE TABLE Codigos (
    Tipo int not null,
    Codigo int not null, /*double pk*/
    Descripcion varchar(50) not null 
);

ALTER TABLE Codigos ADD CONSTRAINT "ID_codigos" PRIMARY KEY (Tipo, Codigo);


CREATE TABLE Vendedores (
    Id_vendedor int primary key,
    Nombre varchar(50) not null,
    Direccion varchar(50) not null,
    Telefono varchar(50) not null,
    Especialidad varchar(50) not null
); 

/* Recursos humanos */
CREATE DATABASE Recursos_Humanos ENCODING 'utf-8';

CREATE TABLE Empleado (
    legajo int primary key,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    direccion varchar(50) not null,
    sueldo int not null,
    horas_capacitacion int not null,
    fecha_ingreso date not null,
    id_local int not null
);
     
CREATE TABLE Telefono_empleado (
    legajo int not null,
    telefono_empleado varchar(50) not null
);
