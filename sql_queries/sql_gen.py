import random, string
from copy import copy
from people.personas import Persona

RESULT = "sql/"

INSERT = "INSERT INTO %s (%s) VALUES (%s);"
COUNTER = 0

#REGISTROS POR TABLA:
DEPT = 12
CIUD = 50
RUBR = 10
CLIE = 2000
FACT = 40000
REGF = FACT * 8
ARTI = 200
PROD = 40
CODI = 40 #?
VEND = 200
EMPL = VEND
TELE = 230

def INC_COUNTER():
    global COUNTER
    COUNTER +=1
    return COUNTER

def PLACEHOLDER():
    return ''

def deco_str(func):
    def wrapper():
        return '"%s"' % (func())
    return wrapper

@deco_str
def get_zone():
    return 'algo'

def get_depto():
    return random.randint(0,DEPT)

@deco_str
def random_str():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))

@deco_str
def get_calif():
    calif = ['malo', 'regular', 'bueno', 'muy bueno']
    return random.choice(calif)

def get_ciudad():
    return random.randint(0,CIUD)

def get_departamento():
    return random.randint(0, DEPT)

def get_poblacion():
    return random.randint(10000, 500000)

@deco_str
def get_direccion():
    calle = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(5))
    return calle + str(random.randint(100, 1000))

@deco_str
def get_telefono():
    return str(random.randint(100000,999999))

def get_cliente():
    return random.randint(0,CLIE)

def get_vendedor():
    return random.randint(0,VEND)

def get_articulo():
    return random.randint(0,ARTI)

def get_factura():
    return random.randint(0, FACT)

def get_unidades():
    return random.randint(0,10)

def get_importe():
    return random.randint(200, 10000)

def get_producto():
    return random.randint(0, PROD)

def get_tam():
    return random.randint(1,20)

def get_sueldo():
    return random.randint(1000000,3000000)

def get_horas_cap():
    return random.randint(0, 200)

def get_local():
    return random.randint(0,30)

def get_legajo():
    return random.randint(0, EMPL)

from datetime import date
def get_date():
    return date(random.randint(2010, 2016), random.randint(1,12), random.randint(1,28)).isoformat()


@deco_str
def get_descripcion():
    return "Descripcion "*8

def get_familia():
    return random.randint(0,40)

def get_duracion():
    return random.randint(0,30)

exclude = {}
def fk(path, exclude=False):
    a, b = path.split(".")
    return random.choice(tables[a][2])[b]

def pk(f):
    return len(tables[f][2]) + 1


tables = {
        'Departamentos':
            (DEPT,
             {
                'Id_depto': (lambda: pk("Departamentos")),
                'Nom_depto': INC_COUNTER,
                'Zona': get_zone
             },
             []
        ),
        'Ciudades':
            (CIUD,
             {
                'Id_ciudad': (lambda: pk("Ciudades")),
                'Id_depto': (lambda: fk("Departamentos.Id_depto")),
                'Nom_ciudad': (lambda: Persona().localidad),
                'Poblacion': get_poblacion,
                'Clasificacion': get_calif
             },
             []
            ),
        'Vendedores':
            (VEND,
             {
                'Id_vendedor': (lambda: pk("Vendedores")),
                'Nombre': (lambda: "%s %s" % (Persona().nombre, Persona().apellido)),
                'Direccion': get_direccion,
                'Telefono': get_telefono,
                'Especialidad': random_str
             },
             []
            ),
        'Rubros':
            (RUBR,
             {
                'Id_rubro':(lambda: pk("Rubros")),
                'Nom_rubro': random_str
             },
             []
            ),
        'Clientes':
            (CLIE,
             {
                'Id_cliente': (lambda: pk("Clientes")),
                'Nombre': (lambda: "%s %s" % (Persona().nombre, Persona().apellido)),
                'Direccion': get_direccion,
                'Telefono': get_telefono,
                'Ciudad': (lambda: fk("Ciudades.Id_ciudad")), #v
                'Departamento': (lambda: fk("Departamentos.Id_depto")),
                'Rubro': random_str,
                'Categoria': random_str,
                'Fecha_alta': get_date
             },
             []
            ),
        'Facturas':
            (FACT,
             {
                'Factura': (lambda: pk("Facturas")),
                'Fecha': get_date,
                'Cliente': (lambda: fk("Clientes.Id_cliente")),
                'Vendedor':(lambda: fk("Vendedores.Id_vendedor")),
             },
             []
            ),
        'Productos':
            (PROD,
             {
                'Id_producto':(lambda: pk("Productos")),
                'Id_familia': get_familia,
                'Id_duracion': get_duracion
             },
             []
            ),

        'Articulos':
            (ARTI,
             {
                'Id_articulo':(lambda: pk("Productos")),
                'Id_producto': (lambda: fk("Productos.Id_producto")),
                'Id_tamano': get_tam
             },
             []
            ),

        'Registros_Facturas':
            (REGF,
             {
                'Factura': (lambda: fk("Facturas.Factura")),
                'Articulo': (lambda: fk("Articulos.Id_articulo")),
                'Importe': get_importe,
                'Unidades': get_unidades,
             },
             []
            ),
        'Codigos':
            (CODI,
             {
                'Tipo':(lambda: pk("Codigos")),
                'Codigo': (lambda: pk("Codigos")),
                'Descripcion': get_descripcion
             },
             []
            ),
        #RRHH
        'Empleado':
            (VEND,
             {
                'legajo': (lambda: pk("Empleado")),
                'nombre': '',
                'apellido': '',
                'direccion': get_direccion,
                'sueldo': get_sueldo,
                'horas_capacitacion': get_horas_cap,
                'fecha_ingreso': get_date,
                'id_local': get_local
            },
            []
            ),
        'Telefono_empleado':
            (TELE,
             {
                'legajo': (lambda: pk("Empleado")),
                'telefono_empleado': get_telefono
             },
             []
            )
        }

def insert_str(table, columns, values):
        col_str = ', '.join(columns)
        val_str = ', '.join(values)
        return INSERT % (table, col_str, val_str) +'\n'


def gen_sql():
    vendedores = []
    tablas = ['Departamentos', 'Ciudades', 'Clientes', 'Productos', 'Articulos', 'Vendedores', 'Facturas', 'Empleado', 'Registros_Facturas', 'Rubros', 'Codigos', 'Telefono_empleado']
    for table in tablas:
        COUNTER = 0
        with open('%s%s.sql' % (RESULT, table), 'w+a') as sql_file:
            cant, columns, all = tables[table][0], tables[table][1], tables[table][2]
            cols = columns.keys()
            if table == 'Empleado':
                x = cols.pop(cols.index('legajo'))
                cols = [x] + cols

            for i in range(cant):
                if table == 'Empleado':
                    vux = vendedores.pop()
                    vux = vux.split(" ")

                n = {}
                values = []
                for col in cols:
                    if table == 'Empleado' and col in ("nombre", "apellido"):
                        if col == "nombre":
                            vvv = vux[0]
                        else:
                            vvv = vux[1]
                    else:
                        n[col] = columns[col]()
                        vvv = n[col]

                    values.append(str(vvv))
                all.append(n)

                new_insert = insert_str(table, columns, values)

                sql_file.write(new_insert)

        if table == "Vendedores":
            vendedores = [i["Nombre"] for i in tables["Vendedores"][2]]



gen_sql()

