def calk1 (n1, n2, n3):
    r1 = n1 ** 2 if n1 >= 0 else n1 ** 4
    r2 = n2 ** 2 if n2 >= 0 else n2 ** 4
    r3 = n3 ** 2 if n3 >= 0 else n3 ** 4
    return r1, r2, r3

n1 = float(input("Перше число: "))
n2 = float(input("Друге число: "))
n3 = float(input("Третє число: "))

calk1 (n1, n2, n3)

print ("Результати",calk1(n1, n2, n3))
