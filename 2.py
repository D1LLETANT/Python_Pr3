Coordinate1 = 0
Coordinate2 = 0

def calk2 (A1, A2, B1, B2):
    global Coordinate1, Coordinate2
    Coordinate1 = (A1 ** 2 + A2 ** 2) ** 0.5
    Coordinate2 = (B1 ** 2 + B2 ** 2) ** 0.5
    if Coordinate1 < Coordinate2:
        print("Точка A знаходиться ближче до початку координат.")
    if Coordinate1 > Coordinate2:
        print("Точка B знаходиться ближче до початку координат.")
    return Coordinate1, Coordinate2

A1 = float(input("A1: "))
A2 = float(input("A2: "))
B1 = float(input("B1: "))
B2 = float(input("B2: "))

calk2 (A1, A2, B1, B2)