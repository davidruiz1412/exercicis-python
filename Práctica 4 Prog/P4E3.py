#DAVID RUIZ ORDÓÑEZ "Pida al usuario si quiere calcular el área de un triángulo
#o un cuadrado, y pida los datos según que caso y muestre el resultado.
#P4E3

respuesta=str(input("¿Quiere calcular el area de un cuadrado o de un triángulo?(c/t)\n"))
if(respuesta=='c'):
    lado=int(input("Introduce el valor del lado del cuadrado:\n"))
    print("El área de su cuadrado es", (lado*lado))
elif(respuesta=='t'):
    base=int(input("Introduce la base de tu triágulo:\n"))
    altura=int(input("Introduce la altura de tu triágulo:\n"))
    print ("El área de tu triángulo es", (base*altura/2))
else:
    print("Error: la respuesta no es válida")
