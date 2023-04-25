import csv

with open('prueba.csv', newline='') as File:  

    reader = csv.reader(File)

    for row in reader:

        print(row [1])
        print(row [3])
        print(row [5])
        print(row [7])
        nombre = (row [1])


print(nombre)