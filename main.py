import csv

afp= 0.1
comision_salud = 0.07
seguro_cesantia_ind = 0.006


sueldo_bruto = float(input())
cafp = input()


administradora_afp = {}

with open('csv/administradora_afp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            administradora_afp[row[0]] = row[1]


comision_afp = float(administradora_afp[cafp])

descuentos_provisionales = sueldo_bruto * (afp + comision_afp + comision_salud + seguro_cesantia_ind)

sueldo_imponible = sueldo_bruto - descuentos_provisionales

print(round(sueldo_imponible, 2))