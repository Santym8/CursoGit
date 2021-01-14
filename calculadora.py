from operaciones import *

print("Suma => +")
print("Resta => -")
print("Multiplicacion => *")
print("Division => /")
print("Potenciacion => **")


print("-----------------------------------")
n1 = int(input("Primer numero "))
operacion = input("Operacion ")
n2 = int(input("Segundo numero "))

if operacion == "+":
    print(suma(n1, n2))
elif operacion == "-":
    print(resta(n1,n2))
elif operacion == "*":
    print(multiplicacion(n1,n2))
elif operacion == "/":
    print(division(n1,n2))
elif operacion == "**":
    potencia(n1,n2)
else:
    print("Numero no valido")

