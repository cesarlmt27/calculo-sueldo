from read import *

def inputs():
    #Solicitar sueldo líquido.
    while True:
        sueldo_liquido = input("Ingrese sueldo líquido: ")
        try:
            val = float(sueldo_liquido)
            if val < 0:
                print("Solo se puede ingresar valores numéricos positivos.")
                continue
            sueldo_liquido = round(float(sueldo_liquido), 2)
            break
        except ValueError:
            print("Solo se puede ingresar valores numéricos positivos.")

    #Solicitar administradora AFP.
    while True:
        print("Seleccione administradora AFP: ")
        for i in administradoras_afp:
            print(i)

        adm_afp = input()
        
        if(adm_afp in administradoras_afp):
            comision_afp = administradoras_afp[adm_afp]  #Declarar valor de la comisión de la administradora AFP.
            break

    #Solicitar tipo de contrato.
    while True:
        print("Seleccione tipo de contrato: ")
        print("Contrato indefinido")
        print("Contrato a plazo fijo")
        contrato = input()
        if(contrato == "Contrato indefinido"):
            break
        elif(contrato == "Contrato a plazo fijo"):
            dp_fijos['SC'] = 0
            break

    return sueldo_liquido, comision_afp


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
    return round(sueldo_bruto, 2)
