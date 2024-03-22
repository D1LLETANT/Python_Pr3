def count_negative(a, b, c):

    count = 0

    if a < 0:
        count += 1
    if b < 0:
        count += 1
    if c < 0:
        count += 1
    return count

a = float(input("а: "))
b = float(input("b: "))
c = float(input("c: "))

count = count_negative(a, b, c)
print("Негативних чисел:", count)