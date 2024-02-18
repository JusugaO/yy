import math
def calcular_area_circulo(radius):
    area = math.pi * radius ** 2
    return area

radius =float(input("ingrese el radio del circulo:"))

area = calcular_area_circulo(radius)
print("el area del circulo con radio",  radius, "es:", area)
