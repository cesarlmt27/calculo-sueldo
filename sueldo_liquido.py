from read import *

#Solicitar sueldo bruto.
while True:
    sueldo_bruto = input("Ingrese sueldo bruto: ")
    try:
        val = float(sueldo_bruto)
        if val < 0:
            print("Solo se puede ingresar valores numéricos positivos.")
            continue
        sueldo_bruto = round(float(sueldo_bruto), 2)
        break
    except ValueError:
        print("Solo se puede ingresar valores numéricos positivos.")

#Solicitar administradora AFP.
#print("Seleccione administradora AFP: ")
adm_afp = 'AFP Capital' #input()

comision_afp = administradoras_afp[adm_afp]  #Declarar valor de la comisión de la administradora AFP.

#Solicitar tipo de contrato.
#print("Seleccione tipo de contrato: ")
contrato = 'indefinido' #input()

if(contrato == 'fijo'):
    dp_fijos['SC'] = 0


def calcular_sueldo_imponible(sueldo_bruto, dp_fijos, comision_afp):
    descuentos_provisionales = sueldo_bruto * (dp_fijos['AFP'] + comision_afp + dp_fijos['CS'] + dp_fijos['SC'])
    sueldo_imponible = sueldo_bruto - descuentos_provisionales
    return round(sueldo_imponible, 2)


sueldo_imponible = calcular_sueldo_imponible(sueldo_bruto, dp_fijos, comision_afp)


for i in tabla_si:  #Recorrer cada lista de la lista "tabla_si"
    if(sueldo_imponible >= float(i[0]) and sueldo_imponible <= float(i[1])):  #Verificar el rango donde se encuentra el sueldo imponible obtenido.
        factor = float(i[2])       #Declarar el factor del rango donde se encuentra el sueldo imponible.
        descuento = float(i[3])    #Declarar el descuento del rango donde se encuentra el sueldo imponible.


def calcular_sueldo_liquido(sueldo_imponible, factor, descuento):
    impuestos_legales = sueldo_imponible * factor - descuento
    sueldo_liquido = sueldo_imponible - impuestos_legales
    return round(sueldo_liquido, 2)

sueldo_liquido = calcular_sueldo_liquido(sueldo_imponible, factor, descuento)

print(sueldo_liquido)