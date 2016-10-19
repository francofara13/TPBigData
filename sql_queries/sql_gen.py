import random, string

INSERT = "INSERT INTO %s (%s) VALUES (%s);"
COUNTER = 0

#REGISTROS POR TABLA:
DEPT = 15
CIUD = 1000
RUBR = 30
CLIE = 3000
FACT = 10000
REGF = 15000
ARTI = 200
PROD = 200
CODI = 30 #?
VEND = 200
EMPL = 200
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

tables = {
        'Departamentos':
            (DEPT,
                {
                'Nom_depto': INC_COUNTER,
                'Zona': get_zone
                }
            ),
        'Ciudades':
            (CIUD,
                {
                'Id_depto': get_depto,
                'Nom_ciudad': random_str ,
                'Poblacion': get_poblacion,
                'Clasificacion': get_calif
                }
            ),
        'Rubros':
            (RUBR,
                {
                'Nom_rubro': random_str
                }
            ),
        'Clientes':
            (CLIE,
                {
                'Nombre': random_str,
                'Direccion': get_direccion,
                'Telefono': get_telefono,
                'Ciudad': get_ciudad, #
                'Departamento': PLACEHOLDER, #LA PUTA MADRE
                'Rubro': random_str,
                'Categoria': random_str,
                'Fecha_alta': PLACEHOLDER
                }
            ),
        'Facturas':
            (FACT,
                {
                'Fecha': PLACEHOLDER,
                'Cliente': get_cliente,
                'Vendedor': get_vendedor
                }
            ),
        'Registros-Facturas':
            (REGF,
                {
                'Factura': get_factura, #Doble clave primaria
                'Articulo': get_articulo,
                'Importe': get_importe,
                'Unidades': get_unidades
                }
            ),
        'Articulos':
            (ARTI,
                {
                'Id_producto': get_producto,
                'Id_tamano': get_tam
                }
            ),
        'Productos':
            (PROD, 
                {
                'Id_familia': PLACEHOLDER,
                'Id_duracion': PLACEHOLDER
                }
            ),
        'Codigos':
            (CODI,
                {
                'Tipo': PLACEHOLDER, #Dobl clave primaria
                'Codigo': PLACEHOLDER,
                'Descripcion': PLACEHOLDER
                }
            ),
        'Vendedores':
            (VEND,
                {
                'Nombre': random_str,
                'Direccion': get_direccion,
                'Telefono': get_telefono,
                'Especialidad': random_str
                }
            ),
        #RRHH
        'Empleado':
            (EMPL,
                {
                'nombre': random_str,
                'apellido': random_str,
                'direccion': get_direccion,
                'sueldo': get_sueldo,
                'horas_capacitacion': get_horas_cap,
                'fecha_ingreso': PLACEHOLDER,
                'id_local': get_local
                }
            ),
        'Telefono_empleado':
            (TELE,
                {
                'legajo': get_legajo,
                'telefono_empleado': get_telefono
                }
            )
        }

def insert_str(table, columns, values):
        col_str = ', '.join(columns)
        val_str = ', '.join(values)
        return INSERT % (table, col_str, val_str) +'\n'

for table in tables.keys():
    COUNTER = 0
    with open('%s.sql'%(table), 'w+a') as sql_file:
        cant = tables[table][0]
        columns = tables[table][1]
        for i in range(cant):
            values = []
            for col in columns.keys():
                values.append(str( columns[col]()))

            new_insert = insert_str(table, columns, values)

            sql_file.write(new_insert)

