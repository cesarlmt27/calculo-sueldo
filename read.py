import csv

#Leer y almacenar los valores de "dp_fijos.csv" en un diccionario.
dp_fijos = {}
with open('csv/dp_fijos.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dp_fijos[row[0]] = float(row[1])


#Leer y almacenar los valores de "administradora_afp.csv" en un diccionario.
administradoras_afp = {}
with open('csv/adm_afp.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            administradoras_afp[row[0]] = row[1]