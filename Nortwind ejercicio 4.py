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

#Quiere saber cuándo fue la última vez que se pidió un producto de cada catgoría.


sql_query = f"""
SELECT c.category_name,
       MAX(o.order_date) AS ultima_fecha_pedido
FROM categories c
JOIN products p ON c.category_id = p.category_id
JOIN order_details od ON p.product_id = od.product_id
JOIN orders o ON od.order_id = o.order_id
GROUP BY c.category_name
ORDER BY ultima_fecha_pedido DESC;
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row)


#Necesita saber si existe algún producto que nunca se haya vendido por su precio original. 
#Resultado sale 0 por lo que: no existen productos que nunca se hayan vendido a su precio original. Todos los productos han tenido al menos una venta sin descuento, por lo que se han vendido al menos una vez a su precio original.

sql_query = f"""
SELECT p.product_name
FROM products p
JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_id, p.product_name
HAVING MIN(od.discount) > 0;
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 

print(len(df))

#En concreto, tienen especial interés por los productos con categoría "Confections". Devuelve el ID del producto, el nombre del producto y su ID de categoría.
sql_query = f"""
SELECT p.product_id,
       p.product_name,
       p.category_id
FROM products p
JOIN categories c 
ON p.category_id = c.category_id
WHERE c.category_name = 'Confections';
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 

#Quiere saber si existe algún proveedor del que pueda prescindir ya que todos los productos que tiene se encuentran descontinuados.
#Resultado no sale nada:  No se han encontrado proveedores cuyos productos estén completamente descontinuados. Esto indica que todos los proveedores actuales mantienen al menos un producto activo, por lo que no sería recomendable prescindir de ninguno basándose en este criterio. Aun asi hago prueba con otra query de que salgan productos activos y salen 67.

sql_query = """
SELECT s.supplier_id, s.company_name
FROM suppliers s
JOIN products p ON s.supplier_id = p.supplier_id
GROUP BY s.supplier_id, s.company_name
HAVING SUM(CASE WHEN p.discontinued = 0 THEN 1 ELSE 0 END) = 0;
"""    

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 

sql_query = """
    SELECT COUNT(*) 
FROM products 
WHERE discontinued = 0;
"""   
cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 

#Extraer los clientes que compraron mas de 30 articulos "Chai" en un único pedido
sql_query = f"""
SELECT c.customer_id,
       c.company_name,
       o.order_id,
       SUM(od.quantity) AS total_chai
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
WHERE p.product_name = 'Chai'
GROUP BY c.customer_id, c.company_name, o.order_id
HAVING SUM(od.quantity) > 30;
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 

#Indica los clientes cuya suma total de carga en los pedidos sea mayor de 1000
sql_query = """
SELECT c.customer_id,
       c.company_name,
       SUM(od.unit_price * od.quantity) AS total_gastado
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
GROUP BY c.customer_id, c.company_name
HAVING SUM(od.unit_price * od.quantity) > 1000
ORDER BY total_gastado DESC;
"""

cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 

#Desde recursos humanos nos piden seleccionar los nombres de las ciudades con 5 o más empleadas de cara a estudiar la apertura de nuevas oficinas.
#Resultado no me sale nada, creo que es porque la tabla tiene 9 empleados repartidos entre varias ciudades y ninguna ciudad tiene más de 5 empleados por eso no sale nada.
sql_query = f"""
SELECT city,
       COUNT(*) AS num_empleados
FROM employees
GROUP BY city
HAVING COUNT(*) >= 5;
"""
cursor.execute(sql_query)
df = cursor.fetchall()

for row in df:
    print(row) 