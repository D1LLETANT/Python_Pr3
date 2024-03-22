def count_full(a, b, c):

    count = 0

    if a == int(a):
        count += 1
    if b == int(b):
        count += 1
    if c == int(c):
        count += 1
    return count

a = float(input("а: "))
b = float(input("b: "))
c = float(input("c: "))

count = count_full(a, b, c)
print("Цілих чисел:", count)