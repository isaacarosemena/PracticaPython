#Creador Isaac Arosemena
#Fecha 27/06/2016
#version de python 3.5

print ('*'*30) #multiplicacion de cadenas 

''' Este es un comentario para varias lineas '''
#   Este es un comentario para una sola linea


print ("Hola mundo") #Cadena con  comilla doble
print ('Hola mundo') #Cadena con  comilla simple
print (""" Esto es para imprimir una frase larga con varios renglones """)

#tipo de concatenacion
nombre = 'Isaac Arosemena'
apellido="Rosario"

print("hola,"+nombre) #Concatenando cadena no proporciona espacio
print("hola,",nombre) #imprimiendo cadena proporcionando espacion con la coma
print('hola,',nombre) #imprimiendo cadena con comilla simple 
print("hola, %s su segundo apellido es %s" %(nombre, apellido)) #imprimiendo cadena con direccion 

#uso de end en print para controlar salido
''' el print () por defecto retorna un \n salto de linea para controlarlo se utiliza un end="" para que no lo haga '''

print (nombre, end = '\n\n') #controlando la impresion para tabular verticalmente 
print (nombre, end = apellido)
print (nombre, end = " ")
print(apellido)

#uso de sep en print para control de salida
''' el print () con el sep para separar la cadena con el caracte que indiques '''

print (nombre,apellido,sep='\t')
print (nombre,apellido,sep="-",end="\v")
print ("Esto es todo amigos")


