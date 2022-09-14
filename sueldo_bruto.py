from read import *

def inputs(sueldo_liquido, adm_afp, contrato):
    try:
        sueldo_liquido = round(float(sueldo_liquido), 2)
        if(sueldo_liquido< 0):
            exit()
    except ValueError:  #Error que se genera al no puder convertir en "float" la variable.
        exit()

    if(isinstance(adm_afp, str) and adm_afp in administradoras_afp):
        comision_afp = administradoras_afp[adm_afp]  #Declarar valor de la comisión de la administradora AFP.
    else:
        exit()

    if(isinstance(contrato, str) and contrato == "Contrato a plazo fijo"):
        dp_fijos['SC'] = 0
    elif(isinstance(contrato, str) and contrato == "Indefinido"):
        pass
    else:
        exit()

    sueldo_imponible = calcular_sueldo_imponible(sueldo_liquido)
    sueldo_bruto = calcular_sueldo_bruto(sueldo_imponible, comision_afp)

    return sueldo_bruto


def calcular_sueldo_imponible(sueldo_liquido):
    for i in tabla_sl:  #Recorrer cada lista de la lista "tabla_sl"
        if(sueldo_liquido >= float(i[0]) and sueldo_liquido <= float(i[1])):  #Verificar el rango donde se encuentra el sueldo liquido obtenido.
            factor = float(i[2])       #Declarar el factor del rango donde se encuentra el sueldo liquido.
            descuento = float(i[3])    #Declarar el descuento del rango donde se encuentra el sueldo liquido.
    
    sueldo_imponible = (sueldo_liquido - descuento) / (1 - factor)
    return round(sueldo_imponible, 2)


def calcular_sueldo_bruto(sueldo_imponible, comision_afp):
    #Suma de los valores de pago de cotizaciones previsionales, de salud y seguro de cesantía.
    suma = dp_fijos['AFP'] + comision_afp + dp_fijos['CS'] + dp_fijos['SC']
    sueldo_bruto = (sueldo_imponible) / (1 - suma)

    sueldo_bruto = "${:,.2f}".format(sueldo_bruto)

    return sueldo_bruto
