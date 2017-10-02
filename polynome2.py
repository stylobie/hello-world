from math import *
aStr = input("que vaut a, coeff de x^2\n")
bStr = input("que vaut b, coeff de x\n")
cStr = input("que vaut c\n")

a = float(aStr)
b = float(bStr)
c = float(cStr)

delta = (b**2) - (4 * a * c)
x0 = (-b / (2 * a))
print(delta)

zeroError = 0.00000001


if delta < 0 - zeroError:
    print("le polynome n'admet pas de racines réeles dans R")
elif delta > 0 + zeroError:
    print("le polynome admet deux racines sur R : x1 :",(-b + sqrt(delta)) / (2 * a), "et x2 :",(-b - sqrt(delta)) / (2 * a))
else:
    print("le polynome admet une racine double sur R : x =", x0)
