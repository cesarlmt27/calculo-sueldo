from read import *

#Solicitar sueldo líquido.
#print("Ingrese sueldo líquido: ")
sueldo_liquido = 4015447.57 #float(input())

#Solicitar administradora AFP.
#print("Seleccione administradora AFP: ")
adm_afp = 'AFP Capital' #input()

comision_afp = float(administradoras_afp[adm_afp])  #Declarar valor de la comisión de la administradora AFP.

#Solicitar tipo de contrato.
#print("Seleccione tipo de contrato: ")
contrato = 'indefinido' #input()

if(contrato == 'fijo'):
    dp_fijos['SC'] = 0


for i in tabla_sl:  #Recorrer cada lista de la lista "tabla_sl"
    if(sueldo_liquido > float(i[0]) and sueldo_liquido < float(i[1])):  #Verificar el rango donde se encuentra el sueldo liquido obtenido.
        factor = float(i[2])       #Declarar el factor del rango donde se encuentra el sueldo liquido.
        descuento = float(i[3])    #Declarar el descuento del rango donde se encuentra el sueldo liquido.


def calcular_sueldo_imponible(sueldo_liquido, descuento, factor):
    sueldo_imponible = (sueldo_liquido - descuento) / (1 - factor)
    return round(sueldo_imponible, 2)


sueldo_imponible = calcular_sueldo_imponible(sueldo_liquido, descuento, factor)


#Suma de los valores de pago de cotizaciones previsionales, de salud y seguro de cesantía.
suma = dp_fijos['AFP'] + comision_afp + dp_fijos['CS'] + dp_fijos['SC']


def calcular_sueldo_bruto(sueldo_imponible, suma):
    sueldo_bruto = (sueldo_imponible) / (1 - suma)
    return round(sueldo_bruto, 2)

sueldo_bruto = calcular_sueldo_bruto(sueldo_imponible, suma)

print(sueldo_bruto)