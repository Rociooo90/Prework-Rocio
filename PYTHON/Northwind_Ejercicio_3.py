
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

#EJERCICIO 3--1 - Haz un estudio de la evolución de los pedidos realizados a lo largo del tiempo.
#Para ello primero realiza la query necesaria para obtener los meses, años y
#pedidos durante cada mes. A continuación crea una línea temporal para ver
#dicha evolución

sql_query = f"""
SELECT
	EXTRACT (YEAR FROM order_date)::int AS YEAR,
	EXTRACT (MONTH FROM order_date)::int AS MONTH,
    COUNT (order_id) AS total_orders
FROM orders
GROUP BY 1,2
ORDER BY 1,2;
"""

cursor.execute(sql_query)
df = cursor.fetchall() 

for row in df:
    print(row)

#ejecutar la query para la linea temporal 
import pandas as pd 
import matplotlib.pyplot as plt

#Datos de ejemplo
MONTH = ['July','August', 'September', 'October','November', 'December','Janury','February','March','April','May','June','July','August','September','October','November','December','Janury','February','March','April','May']
YEAR = [1996,1996,1996,1996,1996,1996,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1997,1998,1998,1998,1998,1998]
Orders = [22,25,23,26,25,31,33,29,30,31,32,30,33,33,37,38,34,48,55,54,73,74,14]

df = pd.DataFrame ({'MONTH','YEAR','Orders'})

fig, ax = plt.subplots()
ax.plot(df['MONTH'], df['Orders'], marker='0')
plt.show() 


##EJERCICIO 3-2---Investiga cuáles son los países donde tenemos más ventas (País origen de la compañía)
# Ventas por país 
sql_query = """
SELECT c.country, 
       SUM(od.unit_price * od.quantity) AS sales
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
GROUP BY c.country;
"""

cursor.execute(sql_query)
df = cursor.fetchall() 

for row in df:
    print(row) 

 #Añades la columna continente 

continentes = {
    'Europe': ['Austria', 'Belgium', 'Denmark', 'Finland', 'France', 
               'Germany', 'Ireland', 'Italy', 'Norway', 'Poland', 
               'Portugal', 'Spain', 'Sweden', 'Switzerland', 'UK'],
    
    'America': ['Argentina', 'Brazil', 'Canada', 'Mexico', 'USA', 'Venezuela']
}

mapa = {
    'Austria': 'Europe',
    'Belgium': 'Europe',
    'Denmark': 'Europe',
    'Finland': 'Europe',
    'France': 'Europe',
    'Germany': 'Europe',
    'Ireland': 'Europe',
    'Italy': 'Europe',
    'Norway': 'Europe',
    'Poland': 'Europe',
    'Portugal': 'Europe',
    'Spain': 'Europe',
    'Sweden': 'Europe',
    'Switzerland': 'Europe',
    'UK': 'Europe',
    'Argentina': 'America',
    'Brasil': 'America',
    'Canada': 'America',
    'Mexico': 'America',
    'USA': 'America',
    'Venezuela': 'America'
}

df["continente"] = df["country"].map(mapa)
print(df.head())

#EJERCICO 3-3--Sabemos que algunos pedidos han llegado con retraso, además hay pedidos que no ha sido registrada su llegada. Investiga si la compañía de transporte
#está relacionada con ello o no. Realiza un boxplot para ver la diferencia de
#rango intercuartílico.

import pandas as pd

query = """
SELECT o.order_id,
       o.order_date,
       o.required_date,
       o.shipped_date,
       s.company_name AS shipper
FROM orders o
JOIN shippers s ON o.ship_via = s.shipper_id;
"""

df = pd.read_sql(query, conexion)

#Calculamos el retraso--la diferencia entre envio real y la fecha esperada

df["required_date"] = pd.to_datetime(df["required_date"])
df["shipped_date"] = pd.to_datetime(df["shipped_date"])

df["delay"] = (df["shipped_date"] - df["required_date"]).dt.days

#Calculamos los no entregados
df["no_entregado"] = df["shipped_date"].isnull() 

#Hacemos el boxplot 
import matplotlib.pyplot as plt

df.boxplot(column="delay", by="shipper")

plt.title("Retrasos por compañía de transporte")
plt.suptitle("")
plt.xlabel("Transportista")
plt.ylabel("Días de retraso")
plt.show() 

#EJERCICIO 3-4--Hay bastante diferencia entre el precio pagado en cada pedido. Averigüa la distribución media del precio del pedido por país de procedencia del cliente.
#Realiza la visualización que creas más conveniente para sacar conclusiones
#Necesitamos obtener los datos  de customers.country y order_details (unit price*quantity)

import pandas as pd

query = """
SELECT c.country,
       o.order_id,
       SUM(od.unit_price * od.quantity) AS total_pedido
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
GROUP BY c.country, o.order_id;
"""

df = pd.read_sql(query, conexion) 

#Calcular media por pais 
media_pais = df.groupby("country")["total_pedido"].mean().reset_index() 

#Visualización haría un gráfico de barras y lo que veo viendo los datos es: Algunos países presentan un precio medio de pedido más alto, lo que indica mayor volumen de compra
#Otros países muestran valores más bajos, con pedidos más pequeños.Existe variabilidad en algunos países, lo que indica comportamiento irregular de compra

import matplotlib.pyplot as plt

media_pais = media_pais.sort_values(by="total_pedido", ascending=False)

plt.figure()
plt.bar(media_pais["country"], media_pais["total_pedido"])
plt.xticks(rotation=90)
plt.title("Precio medio de pedidos por país")
plt.xlabel("País")
plt.ylabel("Precio medio")
plt.show()

#Investiga si existen clientes que no hayan pedido nunca. ¿Qué porcentaje de clientes no tienen pedidos registrados?
query = """
SELECT c.customer_id
FROM customers c
LEFT JOIN orders o 
ON c.customer_id = o.customer_id
WHERE o.customer_id IS NULL;
"""

import pandas as pd

clientes_sin_pedidos = pd.read_sql(query, conexion)

total_clientes = pd.read_sql("SELECT COUNT(*) FROM customers;", conexion).iloc[0,0]

num_sin_pedidos = len(clientes_sin_pedidos)

porcentaje = (num_sin_pedidos / total_clientes) * 100

print("Clientes sin pedidos:", num_sin_pedidos)
print("Total clientes:", total_clientes)
print("Porcentaje:", porcentaje) 

#Estudia los productos más demandados e investiga cuáles corre prisa hacer reestock (Los que quedan 20 o menos y no hay unidades pedidas). Realiza la
#visualización que creas más conveniente para sacar conclusiones.

import pandas as pd

query = """
SELECT p.product_name,
       p.units_in_stock,
       p.units_on_order,
       SUM(od.quantity) AS total_vendido
FROM products p
LEFT JOIN order_details od ON p.product_id = od.product_id
GROUP BY p.product_name, p.units_in_stock, p.units_on_order;
"""

df = pd.read_sql(query, conexion) 

top_productos = df.sort_values(by="total_vendido", ascending=False)

reestock = df[
    (df["units_in_stock"] <= 20) & 
    (df["units_on_order"] == 0)
]

#gráfica de top productos

import matplotlib.pyplot as plt

top10 = top_productos.head(10)

plt.figure()
plt.bar(top10["product_name"], top10["total_vendido"])
plt.xticks(rotation=90)
plt.title("Top 10 productos más demandados")
plt.ylabel("Cantidad vendida")
plt.show()

#gráfica productos necesitan restock
plt.figure()
plt.bar(reestock["product_name"], reestock["units_in_stock"])
plt.xticks(rotation=90)
plt.title("Productos con bajo stock y sin pedidos")
plt.ylabel("Unidades en stock")
plt.show() 

