import sueldo_liquido as sl
import sueldo_bruto as sb

while True:
    print("¿Qué desea calcular? (Ingresar el número de la opción)")
    print("0. Sueldo líquido")
    print("1. Sueldo bruto")
    consulta = int(input())

    if consulta == 0:
        tuple = sl.inputs()
        sueldo_imponible = sl.calcular_sueldo_imponible(tuple[0], tuple[1])
        sueldo_liquido = sl.calcular_sueldo_liquido(sueldo_imponible)
        print(sueldo_liquido)
        break

    elif consulta == 1:
        tuple = sb.inputs()
        sueldo_imponible = sb.calcular_sueldo_imponible(tuple[0])
        sueldo_bruto = sb.calcular_sueldo_bruto(sueldo_imponible, tuple[1])
        print(sueldo_bruto)
        break