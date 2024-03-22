def count(a, b, c, k):

    mass = []

    if not a % k:
        mass.append(a)
    if not b % k:
        mass.append(b)
    if  not c % k:
        mass.append(c)
    return mass

a = float(input("а: "))
b = float(input("b: "))
c = float(input("c: "))
k = float(input("k: "))

mass = count(a, b, c, k)

if mass:
    print(f"Число {k} є дільником чисел: {mass}")
else:
    print(f"Число {k} не є дільником жодного з чисел.")
