#Pida al usuario el precio de un producto y el nombre del producto y muestre
#el mensaje con el precio del IVA (21%). Por ejemplo: “ Tu bicicleta vale 100
#euros y con el 21 % de IVA se queda en 121 euros en total”.
#P3E5

precio=int (input("Introduce el precio del producto:\n"))
nombre=str (input("Introduce el nombre del producto:\n"))
iva=float (precio*1.21)
print("El precio de tu %s es de %d y con el impuesto iva asciende a %f" % (nombre,precio,iva))
