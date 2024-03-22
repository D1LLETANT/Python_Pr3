def calk3 (a1, a2):
    if a1 + a2 != 180:
        if a1 == 90 or a2 == 90 or (180 - a1 - a2) == 90:
            print("Трикутник прямокутний")
        else:
            print("Трикутник не прямокутний")
    else:
        print("Не трикутник")

a1 = float(input("Перша величина: "))
a2 = float(input("Друга величина: "))

calk3(a1, a2)