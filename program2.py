import math

xm = float(input("Введіть x точки M: "))
ym = float(input("Введіть y точки M: "))

xa = float(input("Введіть x точки A: "))
ya = float(input("Введіть y точки A: "))

xb = float(input("Введіть x точки B: "))
yb = float(input("Введіть y точки B: "))

xc = float(input("Введіть x точки C: "))
yc = float(input("Введіть y точки C: "))

da = math.sqrt((xa - xm) ** 2 + (ya - ym) ** 2)
db = math.sqrt((xb - xm) ** 2 + (yb - ym) ** 2)
dc = math.sqrt((xc - xm) ** 2 + (yc - ym) ** 2)

if da >= db and da >= dc:
    print("Найбільш віддалена точка — A")
    print("Відстань =", da)
elif db >= da and db >= dc:
    print("Найбільш віддалена точка — B")
    print("Відстань =", db)
else:
    print("Найбільш віддалена точка — C")
    print("Відстань =", dc)