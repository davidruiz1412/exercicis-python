#DAVID RUIZ ORDÓÑEZ "Pida al usuario 5 números y diga si estos estaban en
#orden decreciente, creciente o desordenados
#P4E2

print("Introduce 5 números:\n")
a=int (input())
b=int (input())
c=int (input())
d=int (input())
e=int (input())

if (a>=b) and (b>=c) and (c>=d) and (d>=e):
    print ("Están en orden decreciente")
elif (a<=b) and (b<=c) and (c<=d) and (d<=e):
    print ("Están en orden creciente")
else:
    print ("Están desordenados")

