from read import *

#Solicitar sueldo bruto.
print("Ingrese sueldo bruto: ")
sueldo_bruto = float(input())

#Solicitar administradora AFP.
print("Seleccione administradora AFP: ")
adm_afp = input()


comision_afp = float(administradoras_afp[adm_afp])  #Declarar valor de la comisión de la administradora AFP.


def calcular_sueldo_imponible(sueldo_bruto, dp_fijos, comision_afp):
    descuentos_provisionales = sueldo_bruto * (dp_fijos['AFP'] + comision_afp + dp_fijos['CS'] + dp_fijos['SC'])
    sueldo_imponible = sueldo_bruto - descuentos_provisionales
    return round(sueldo_imponible, 2)


sueldo_imponible = calcular_sueldo_imponible(sueldo_bruto, dp_fijos, comision_afp)
print(sueldo_imponible)