import math

x = float(input("Введіть x: "))

if x > 0.53:
    y = 3 - 0.127 * x + math.log(abs(x + 2))
    print("f(x) =", y)

elif -1.2 < x <= 0.53:
    y = 2.35 * math.exp(4 * x - 1) + math.cos(x)
    print("f(x) =", y)

else:
    z = x + 0.3 * math.cos(x)

    if z >= 0:
        y = 0.11 * math.sqrt(z)
        print("f(x) =", y)
    else:
        print("За цієї умови функція не має дійсного значення.")