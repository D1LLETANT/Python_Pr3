def deciding(a, b):
    if a != b:
        max_number = max(a, b)
        return max_number, max_number
    else:
        return 0, 0

a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

result_a, result_b = deciding(a, b)

print("a =", result_a)
print("b =", result_b)