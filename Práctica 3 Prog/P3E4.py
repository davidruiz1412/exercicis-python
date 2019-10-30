#Pida un número que como máximo tenga tres cifras (por ejemplo serían válidos
#1, 99 i 213 pero no 1001). Si el usuario introduce un número de más de tres
#cifras debe un informar con un mensaje de error como este “ ERROR: El número
#1005 tiene más de tres cifras”.
#DAVID RUIZ ORDOÑEZ
#P3E4

numero=int (input("Introduce un numero con 3 dígitos como máximo:\n"))
if((numero-1000)>=0):
    print("ERROR: El número",numero,"es mayor de 3 dígitos")
