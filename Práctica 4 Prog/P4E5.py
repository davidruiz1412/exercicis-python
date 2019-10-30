#DAVID RUIZ ORDÓÑEZ "Pida al usuario un importe en euros y diga si el cajero
#automático le 	puede dar dicho importe utilizando el mismo billete y el más
#grande (recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5€).
 	
#Por ejemplo: 
#25 euros → “el cajero te devuelve 5 billetes de 5 euros”
 	
#20 euros → “el cajero de devuelve 1 billete de 20 euros”
 	
#130 euros → “el cajero te devuelve 13 billetes de 10 euros”

#P4E5

importe=int(input("Introduce un importe:\n"))

if(importe%500==0):
    cantidad=(importe/500)
    if (cantidad==1):
        print("El cajero te devuelve 1 billete de 500 euros")
    else:
        print("El cajero te devuelve %d billetes de 500 euros" % (cantidad))
elif(importe%100==0):
    cantidad=(importe/100)
    if (cantidad==1):
        print("El cajero te devuelve 1 billete de 100 euros")
    else:
        print("El cajero te devuelve %d billetes de 100 euros" % (cantidad))
elif(importe%50==0):
    cantidad=(importe/50)
    if (cantidad==1):
        print("El cajero te devuelve 1 billete de 50 euros")
    else:
        print("El cajero te devuelve %d billetes de 50 euros" % (cantidad))
elif(importe%20==0):
    cantidad=(importe/20)
    if (cantidad==1):
        print("El cajero te devuelve 1 billete de 20 euros")
    else:
        print("El cajero te devuelve %d billetes de 20 euros" % (cantidad))
elif(importe%10==0):
    cantidad=(importe/10)
    if (cantidad==1):
        print("El cajero te devuelve 1 billete de 10 euros")
    else:
        print("El cajero te devuelve %d billetes de 10 euros" % (cantidad))
elif(importe%5==0):
    cantidad=(importe/5)
    if (cantidad==1):
        print("El cajero te devuelve 1 billete de 5 euros")
    else:
        print("El cajero te devuelve %d billetes de 5 euros" % (cantidad))
