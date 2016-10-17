// Facturacion y ventas

CREATE TABLE Departamentos (
    Id_depto serial primary key,
    Nom_depto int NULL,
    Zona varchar NULL
)

CREATE TABLE Ciudades (
    Id_ciudad serial primary key,
    Id_depto int not null, 
    Nom_ciudad varchar(50) not null, 
    Poblacion int not null,
    Clasificacion varchar(50)
)

CREATE TABLE Rubros (
    Id_rubro serial primary key,
    Nom_rubro varchar(50) not NULL
)

CREATE TABLE Clientes (Id_cliente serial primary key,
    Nombre varchar(50) not null,
    Direccion varchar(50) not null,
    Telefono varchar(50) not null,
    Ciudad int references Ciudades(Id_ciudad), /*FK*/
    Departamento int references Departamentoreferences(Id_depto),/*FK*/
    Rubro varchar(50) not null,
    Categoria varchar(50) not null,
    Fecha_alta date not null
 )

CREATE TABLE Facturas (Factura serial primary key,
     Fecha date not null,
     Cliente int references Clientes(Id_cliente), /*FK*/
     Vendedor int references Vendedores(Id_vendedor) /*FK*/
)
CREATE TABLE Registros-Facturas (Factura serial not null,
     Articulo serial not null, /*double pk*/
     Importe int not null,
     Unidades int not null)

ALTER TABLE Registros-Facturas ADD CONSTRAINT "ID_reg_fact" PRIMARY KEY (Factura, Articulo);


CREATE TABLE Articulos (Id_articulo serial primary key,
     Id_producto int references Productos(Id_producto),/*FK*/
     Id_tamaño int not null)

CREATE TABLE Productos (Id_producto serial primary key,
    Id_familia int not null,
    Id_duracion int not null)

CREATE TABLE Codigos (Tipo serial not null,
    Codigo serial not null, /*double pk*/
    Descripcion varchar(50) not null) 

ALTER TABLE Codigos ADD CONSTRAINT "ID_codigos" PRIMARY KEY (Tipo, Codigo);


CREATE TABLE Vendedores (Id_vendedor serial primary key,
     Nombre varchar(50) not null,
     Direccion varchar(50) not null,
     Telefono varchar(50) not null,
     Especialidad varchar(50) not null
) 

// Recursos humanos

Empleado(legajo serial primary key, nombre varchar(50) not null, apellido varchar(50) not null, direccion varchar(50) not null, sueldo int not null, horas_capacitacion int not null, fecha_ingreso date not null, id_local int not null)
Telefono_empleado(legajo int not null, telefono_empleado varchar(50) not null)

