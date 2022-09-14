import sueldo_liquido as sl
import sueldo_bruto as sb

while True:
    print("¿Qué desea calcular? (Ingresar el número de la opción)")
    print("0. Sueldo líquido")
    print("1. Sueldo bruto")
    consulta = int(input())

    if consulta == 0:
        sueldo_liquido = sl.inputs(3724678.85, "AFP Capital", "Indefinido")
        print(sueldo_liquido)
        break
    elif consulta == 1:
        sueldo_bruto = sb.inputs(2879199.40, "AFP Capital", "Indefinido")
        print(sueldo_bruto)
        break
