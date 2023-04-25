archivo = open('prueba.csv', "r")

lineas = archivo.readlines()

for x in linea:

	x = x.split("|")

	nombre = x[1]
	provincia = x[3]
	canton = x[5]
	parroquia = x[7]

cadena = """ nombre:%s\n provincia

archivo.close()