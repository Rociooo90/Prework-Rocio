import psycopg2
print("Librería importada correctamente")

conexion = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="admin",
    port="5432"
)

cursor = conexion.cursor ()
#cursor.execute ('Select version();')


## EJERCICIO 1 YA TENEMOS EL ESQUEMA EN DBEAVER
## EJERCICIO 2
##¿Cuántos empleados tenemos contratados en 'Global Importaciones'? Indica
#su id, nombre, apellido, ciudad y país.

sql_query = f"""
SELECT employee_id,
    first_name,
    last_name,
    city,
    country
FROM employees
ORDER BY employee_id;
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)

##¿Qué productos tenemos? Indica el id del producto, id del proveedor, nombre
#del producto, precio por unidad, unidades en stock, unidades pedidas al
#proveedor y productos descontinuados

sql_query = f"""
SELECT product_id,
       products.supplier_id,
       product_name,
       unit_price,
       units_in_stock
       units_on_order,
       discontinued
FROM   products
"""


cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)


# ¿Tenemos productos descontinuados?. Indica el nombre del producto, y
#cantidad que nos queda en stock. (El atributo Discontinued es un booleano: si
#es igual a 1 el producto ha sido descontinuado). Respuesta no hay productos discontinuados...

sql_query = f"""
SELECT product_name,
       units_in_stock
FROM   products
WHERE  discontinued = 1
ORDER BY  units_in_stock DESC, product_name; 
"""


cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)


#¿Qué proveedores tenemos? Indica el id de la compañía, nombre de la
#compañía, ciudad y país.

sql_query = f"""
SELECT supplier_id,
       company_name,
       city,
       country
FROM   suppliers
ORDER BY  supplier_id; 
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)

#¿Qué pedidos hemos tenido? Indica el número de pedido, id del cliente,id del
#transportista, dia del pedido, día requerido de llegada y día de llegada real.
sql_query = f"""
SELECT order_id,
       customer_id,
       ship_via,
       order_date,
       required_date,
       shipped_date
FROM   orders
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)


##¿Cuántos pedidos hemos tenido? --Solucion 830
sql_query = """
SELECT COUNT(*) FROM   orders 
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)

#¿Cuántos clientes tenemos? Indica el id del cliente, nombre de la compañía,
#ciudad y país.

sql_query = f"""
SELECT customer_id,
       company_name,
       city,
       country
FROM   customers 
"""

cursor.execute(sql_query)
df = cursor.fetchall()
for row in df:
    print(row)


# ¿Con qué empresas de transporte trabajamos? Indica su id del transportista y
#el nombre de la compañía.

sql_query = f"""
SELECT shipper_id,
       company_name
FROM   shippers
"""

cursor.execute(sql_query)
df = cursor.fetchall()
for row in df:
    print(row) 


#¿Cómo son las relaciones de reporte de resultados entre los empleados?

sql_query = f"""
SELECT employee_id,
       reports_to
FROM   employees
"""

cursor.execute(sql_query)
df = cursor.fetchall()
for row in df:
    print(row) 