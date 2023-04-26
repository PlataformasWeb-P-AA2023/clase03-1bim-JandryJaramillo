archivo = open('ejercicio/data/Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

lineas = archivo.readlines()

for l in lineas: 

 l = l.split("|")

 nombre = l[1]

 canton = l[5]

 provincia = l[3]

 parroquia = l[7]

 cadena = """ nombre:%s\n provincia:%s \n canton:%s \n parroquia:%s """ %(nombre, provincia, canton, parroquia) 

 print (cadena)

archivo.close()