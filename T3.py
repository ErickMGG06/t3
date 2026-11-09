import random
import math

def calcular_montecarlo():
    print("--- CÁLCULO DE INTERSECCIÓN ELIPSE E HIPÉRBOLA (MONTE CARLO) ---")
    a = float(input("Ingrese el valor de a (para la elipse): "))
    b = float(input("Ingrese el valor de b (para la elipse): "))
    c = float(input("Ingrese el valor de c (para la hipérbola): "))
    d = float(input("Ingrese el valor de d (para la hipérbola): "))
    n = int(input("Ingrese la cantidad de puntos aleatorios: "))

    dentro_elipse = 0
    en_interseccion = 0

    x_min, x_max = -a, a
    y_min, y_max = -b, b

    for _ in range(n):
        x = random.uniform(x_min, x_max)
        y = random.uniform(y_min, y_max)

        cond_elipse = (x**2 / a**2) + (y**2 / b**2) <= 1.0

        if cond_elipse:
            dentro_elipse += 1

            cond_hiperbola = (x**2 / c**2) - (y**2 / d**2) >= 1.0

            if cond_hiperbola:
                en_interseccion += 1

    area_elipse_formula = math.pi * a * b

    if dentro_elipse > 0:
        area_aprox_interseccion = (en_interseccion / dentro_elipse) * area_elipse_formula
    else:
        area_aprox_interseccion = 0.0

    print("\n--- RESULTADOS ---")
    print(f"Puntos aleatorios totales generados: {n}")
    print(f"Puntos que cayeron dentro de la elipse: {dentro_elipse}")
    print(f"Puntos que cayeron en la intersección: {en_interseccion}")
    print(f"Área teórica de la elipse: {area_elipse_formula:.4f}")
    print(f"Área aproximada de la intersección: {area_aprox_interseccion:.4f}")

if __name__ == "__main__":
    calcular_montecarlo()