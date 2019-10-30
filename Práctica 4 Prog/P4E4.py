#DAVID RUIZ ORDÓÑEZ "Pida al usuario tres números y un cuarto número,
#y compruebe si éste último es divisor de los tres números primeros.
#P4E4

print("Introduce tres números:\n")
a=int(input())
b=int(input())
c=int(input())
print("Introduce un cuarto número:\n")
d=int(input())

if (d%a==0) and (d%b==0) and (d%c==0):
    print("El número %d es divisor de %d, %d y %d" % (d,a,b,c))
else:
    print("El número %d no es divisor de %d, %d y %d" % (d,a,b,c))
