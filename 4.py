x = int(input("x: "))
y = int(input("y: "))

        
def calk3(x, y):
    min_number = min(x, y)
    max_number = max(x, y)

    x = (min_number + max_number) / 2
    y = 2 * min_number * max_number

    print("Менше з цих двох чисел замінено на половину їх суми:", x)
    print("Більше з цих двох чисел замінено на подвоєний добуток:", y)

if x == y:
    print ("x = y, погано")
else:
    calk3(x, y)