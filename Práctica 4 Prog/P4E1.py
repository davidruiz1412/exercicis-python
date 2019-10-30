#DAVID RUIZ ORDÓÑEZ "Pida al usuario 5 números y diga cual es el mayor y cuál
#el menor."
#P4E1

print("Introduce 5 números:\n")
a=int (input())
b=int (input())
c=int (input())
d=int (input())
e=int (input())

if(a>=b) and (a>=c) and (a>=d) and (a>=e):
    may=a
if(b>=a) and (b>=c) and (b>=d) and (b>=e):
    may=b
if(c>=a) and (c>=b) and (c>=d) and (c>=e):
    may=c
if(d>=a) and (d>=b) and (d>=c) and (d>=e):
    may=d
if(e>=a) and (e>=b) and (e>=c) and (e>=d):
    may=e
if(a<=b) and (a<=c) and (a<=d) and (a<=e):
    mini=a
if(b<=a) and (b<=c) and (b<=d) and (b<=e):
    mini=b
if(c<=a) and (c<=b) and (c<=d) and (c<=e):
    mini=c
if(d<=a) and (d<=b) and (d<=c) and (d<=e):
    mini=d
if(e<=a) and (e<=b) and (e<=c) and (e<=d):
    mini=e

print("El mayor es %d y el menor es %d" % (may,mini))
