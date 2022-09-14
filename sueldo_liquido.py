from read import *

def inputs(sueldo_bruto, adm_afp, contrato):
    try:
        sueldo_bruto = round(float(sueldo_bruto), 2)
        if(sueldo_bruto < 0):
            return "error"
    except ValueError:  #Error que se genera al no poder convertir en "float" la variable.
        return "error"
    
    if(isinstance(adm_afp, str) and adm_afp in administradoras_afp):
        comision_afp = administradoras_afp[adm_afp]  #Declarar valor de la comisión de la administradora AFP.
    else:
        return "error"

    if(isinstance(contrato, str) and contrato == "Contrato a plazo fijo"):
        dp_fijos['SC'] = 0
    elif(isinstance(contrato, str) and contrato == "Contrato indefinido"):
        pass
    else:
        return "error"

    sueldo_imponible = calcular_sueldo_imponible(sueldo_bruto, comision_afp)
    sueldo_liquido = calcular_sueldo_liquido(sueldo_imponible)

    return sueldo_liquido


def calcular_sueldo_imponible(sueldo_bruto, comision_afp):
    descuentos_provisionales = sueldo_bruto * (dp_fijos['AFP'] + comision_afp + dp_fijos['CS'] + dp_fijos['SC'])
    sueldo_imponible = sueldo_bruto - descuentos_provisionales
    return round(sueldo_imponible, 2)


def calcular_sueldo_liquido(sueldo_imponible):
    for i in tabla_si:  #Recorrer cada lista de la lista "tabla_si"
        if(sueldo_imponible >= float(i[0]) and sueldo_imponible <= float(i[1])):  #Verificar el rango donde se encuentra el sueldo imponible obtenido.
            factor = float(i[2])       #Declarar el factor del rango donde se encuentra el sueldo imponible.
            descuento = float(i[3])    #Declarar el descuento del rango donde se encuentra el sueldo imponible.

    impuestos_legales = sueldo_imponible * factor - descuento
    sueldo_liquido = sueldo_imponible - impuestos_legales
    
    sueldo_liquido = "${:,.2f}".format(sueldo_liquido)

    return sueldo_liquido
