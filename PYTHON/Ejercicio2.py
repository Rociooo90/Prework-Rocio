"""
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
"""
def calcular_total_con_propina(total_cuenta, porcentaje_propina=15):
    propina = total_cuenta * (porcentaje_propina / 100)
    total_a_pagar = total_cuenta + propina 
    return total_a_pagar
