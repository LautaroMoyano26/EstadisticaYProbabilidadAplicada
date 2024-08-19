import statistics
import math
import scipy.integrate as integrate
from tabulate import tabulate

# Funciones estadísticas.

def calcular_media(lista):
    return round(statistics.mean(lista), 4)

def calcular_moda(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    moda_frecuencia_maxima = max(frecuencias.values())
    moda = [num for num, freq in frecuencias.items() if freq == moda_frecuencia_maxima]
    if len(set(frecuencias.values())) == 1:
        return None, None
    else:
        return moda, moda_frecuencia_maxima

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    return round(statistics.median(lista_ordenada), 4)

def calcular_desviacion(lista):
    desviacion_estandar = statistics.stdev(lista)
    return round(desviacion_estandar, 4)

def calcular_varianza(lista):
    varianza = statistics.variance(lista)
    return round(varianza, 4)

def frecuencia_absoluta(lista):
    frecuencias = {}
    for num in lista:
        frecuencias[num] = frecuencias.get(num, 0) + 1
    return frecuencias

def frecuencia_relativa(lista):
    total = len(lista)
    frec_abs = frecuencia_absoluta(lista)
    frec_relativa = {}
    for clave, valor in frec_abs.items():
        frec_relativa[clave] = round(valor / total, 4)
    return frec_relativa

def frecuencia_porcentual(lista):
    frec_rel = frecuencia_relativa(lista)
    frec_porcentual = {}
    for clave, valor in frec_rel.items():
        frec_porcentual[clave] = round(valor * 100, 4)
    return frec_porcentual

def frecuencia_absoluta_acumulada(lista):
    frec_abs = frecuencia_absoluta(lista)
    acumulado = 0
    frec_abs_acum = {}
    for clave, valor in sorted(frec_abs.items()):
        acumulado += valor
        frec_abs_acum[clave] = acumulado
    return frec_abs_acum

def frecuencia_relativa_acumulada(lista):
    total = len(lista)
    frec_rel = frecuencia_relativa(lista)
    acumulado = 0
    frec_rel_acum = {}
    for clave, valor in sorted(frec_rel.items()):
        acumulado += valor
        frec_rel_acum[clave] = round(acumulado, 4)
    return frec_rel_acum

def frecuencia_porcentual_acumulada(lista):
    frec_porcent = frecuencia_porcentual(lista)
    acumulado = 0
    frec_porcent_acum = {}
    for clave, valor in sorted(frec_porcent.items()):
        acumulado += valor
        frec_porcent_acum[clave] = f"{round(acumulado, 4)}%"
    return frec_porcent_acum

def coeficiente_curtosis(lista):
    n = len(lista)
    media = calcular_media(lista)
    desviacion = calcular_desviacion(lista)
    suma_cuarta_potencia = 0
    for x in lista:
        suma_cuarta_potencia += (x - media) ** 4
    curtosis = (n * suma_cuarta_potencia) / ((n - 1) * (desviacion ** 4))
    curtosis = curtosis - 3
    return round(curtosis, 4)

def menu_estadistico(numeros):
    while True:
        try:
            print("\nEstadística - Seleccione las opciones deseadas (separadas por comas):")
            print("1. Visualizar la MEDIA.")
            print("2. Visualizar la MODA.")
            print("3. Visualizar la MEDIANA.")
            print("4. Visualizar la DESVIACIÓN ESTÁNDAR.")
            print("5. Visualizar la VARIANZA.")
            print("6. Visualizar FRECUENCIA ABSOLUTA.")
            print("7. Visualizar FRECUENCIA RELATIVA.")
            print("8. Visualizar FRECUENCIA PORCENTUAL.")
            print("9. Visualizar FRECUENCIA ABSOLUTA ACUMULADA.")
            print("11. Visualizar FRECUENCIA PORCENTUAL ACUMULADA.")
            print("12. Visualizar COEFICIENTE DE CURTOSIS.")
            print("13. Visualizar todos los cálculos estadísticos.")
            print("14. Salir del menú estadístico.")
            opciones = input("Ingrese las opciones deseadas (separadas por comas): ")
            opciones = [int(opcion) for opcion in opciones.split(",")]
            resultados = []
            for opcion in opciones:
                if opcion == 1:
                    resultado = calcular_media(numeros)
                    resultados.append(["MEDIA", resultado])
                elif opcion == 2:
                    moda, frecuencia_maxima = calcular_moda(numeros)
                    if moda is None:
                        resultados.append(["MODA", "No hay moda"])
                    else:
                        resultados.append(["MODA", moda])
                elif opcion == 3:
                    resultado = calcular_mediana(numeros)
                    resultados.append(["MEDIANA", resultado])
                elif opcion == 4:
                    resultado = calcular_desviacion(numeros)
                    resultados.append(["DESVIACIÓN ESTÁNDAR", resultado])
                elif opcion == 5:
                    resultado = calcular_varianza(numeros)
                    resultados.append(["VARIANZA", resultado])
                elif opcion == 6:
                    resultado = frecuencia_absoluta(numeros)
                    resultados.append(["FRECUENCIA ABSOLUTA", resultado])
                elif opcion == 7:
                    resultado = frecuencia_relativa(numeros)
                    resultados.append(["FRECUENCIA RELATIVA", resultado])
                elif opcion == 8:
                    resultado = frecuencia_porcentual(numeros)
                    resultados.append(["FRECUENCIA PORCENTUAL", resultado])
                elif opcion == 9:
                    resultado = frecuencia_absoluta_acumulada(numeros)
                    resultados.append(["FRECUENCIA ABSOLUTA ACUMULADA", resultado])
                elif opcion == 10:
                    resultado = frecuencia_relativa_acumulada(numeros)
                    resultados.append(["FRECUENCIA RELATIVA ACUMULADA", resultado])
                elif opcion == 11:
                    resultado = frecuencia_porcentual_acumulada(numeros)
                    resultados.append(["FRECUENCIA PORCENTUAL ACUMULADA", resultado])
                elif opcion == 12:
                    resultado = coeficiente_curtosis(numeros)
                    resultados.append(["COEFICIENTE DE CURTOSIS", resultado])
                elif opcion == 13:
                    resultados.append(["MEDIA", calcular_media(numeros)])
                    resultados.append(["MODA", calcular_moda(numeros)])
                    resultados.append(["MEDIANA", calcular_mediana(numeros)])
                    resultados.append(["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)])
                    resultados.append(["VARIANZA", calcular_varianza(numeros)])
                    resultados.append(["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)])
                    resultados.append(["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)])
                    resultados.append(["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)])
                    resultados.append(["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)])
                    resultados.append(["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)])
                    resultados.append(["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)])
                    resultados.append(["COEFICIENTE DE CURTOSIS", coeficiente_curtosis(numeros)])
                elif opcion == 14:
                    break
                else:
                    print("Opción no válida. Por favor, ingrese una opción válida.")
            print(tabulate(resultados, headers=["Cálculo", "Resultado"], tablefmt="grid"))
        except ValueError:
            print("Error: Por favor, ingrese una opción válida.")

def distribucion_binomial(n, p, k):
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def distribucion_hipergeometrica(n, M, N, k):
    return (math.comb(M, k) * math.comb(N - M, n - k)) / math.comb(N, n)

def distribucion_normal(x, mu, sigma):
    coeficiente = 1 / (2 * math.pi * (sigma ** 2)) ** 0.5
    exponente = -((x - mu) ** 2) / (2 * sigma ** 2)
    densidad = coeficiente ** exponente
    return densidad

def calcular_integral(mu, sigma, primer_parametro, segundo_parametro):
    integral, error = integrate.quad(distribucion_normal, primer_parametro, segundo_parametro, args=(mu, sigma))
    return integral
def distribucion_poisson(lambda_, k):
    return (lambda_ ** k) * (math.e ** (-lambda_)) / math.factorial(k)

def menu_distribuciones():
    while True:
        try:
            print("\nDistribuciones - Seleccione la distribución deseada:")
            print("1. Distribución Binomial.")
            print("2. Distribución Hipergeométrica.")
            print("3. Distribución Normal.")
            print("4. Distribución de Poisson.")
            print("5. Salir del menú de distribuciones.")
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
                n = int(input("Ingrese el número de ensayos (n): "))
                p = float(input("Ingrese la probabilidad de éxito (p): "))
                k = int(input("Ingrese el número de éxitos (k): "))
                resultado = distribucion_binomial(n, p, k)
                print(f"La probabilidad de obtener {k} éxitos en {n} ensayos con una probabilidad de éxito de {p} es {resultado:.4f}.")
            elif opcion == 2:
                n = int(input("Ingrese el número de ensayos (n): "))
                M = int(input("Ingrese el número de elementos favorables (M): "))
                N = int(input("Ingrese el número total de elementos (N): "))
                k = int(input("Ingrese el número de elementos favorables seleccionados (k): "))
                resultado = distribucion_hipergeometrica(n, M, N, k)
                print(f"La probabilidad de seleccionar {k} elementos favorables en {n} ensayos de un conjunto de {N} elementos con {M} favorables es {resultado:.4f}.")
            elif opcion == 3:
                mu = float(input("Ingrese la media (μ): "))
                sigma = float(input("Ingrese la desviación estándar (σ > 0): "))
                x = float(input("Ingrese el valor de x para el cual desea calcular la función de densidad: "))
                # Calcular la función de densidad
                resultado = distribucion_normal(x, mu, sigma)
                # Pedir los límites de integración para calcular la integral
                primer_parametro = float(input("Ingrese el primer parámetro de integración: "))
                segundo_parametro = float(input("Ingrese el segundo parámetro de integración: "))
    
                # Calcular la integral
                resultado_integral = calcular_integral(mu, sigma, primer_parametro, segundo_parametro)
                # Mostrar el resultado en una tabla
                print(tabulate([["DENSIDAD NORMAL", resultado],
                                ["INTEGRAL", resultado_integral]], 
                                headers=["Operación", "Resultado"], 
                                tablefmt="grid"))
            elif opcion == 4:
                lambda_ = float(input("Ingrese la tasa de llegada (λ): "))
                k = int(input("Ingrese el número de eventos (k): "))
                resultado = distribucion_poisson(lambda_, k)
                print(f"La probabilidad de que ocurran {k} eventos con una tasa de llegada de {lambda_} es {resultado:.4f}.")
            elif opcion == 5:
                break
            else:
                print("Opción no válida. Por favor, ingrese una opción válida.")
        except ValueError:
            print("Error: Por favor, ingrese una opción válida.")
            
def ingresar_datos():
    cantidad = 0
    numeros = []
    print('Ingrese los datos uno por uno (ENTER), luego para ir al menú ingrese "n" \n')
    while True:
        numero = input(f"Ingrese el dato número {cantidad + 1}: ")
        if numero.lower() == "n":
            break
        else:
            try:
                numero = float(numero)
                cantidad += 1
                numeros.append(numero)
            except ValueError:
                print("Por favor, ingrese un número válido o escriba 'n' para terminar.")
    return numeros

def main():
    while True:
        try:
            print("\nMenú Principal:")
            print("A. Cálculos Estadísticos")
            print("B. Cálculos de Distribuciones")
            print("0. Salir")

            opcion_principal = input("Ingrese la opción que desea seleccionar: ").upper()

            if opcion_principal == "0":
                print("Saliendo del programa...")
                break
            elif opcion_principal == "A":
                numeros = ingresar_datos()
                menu_estadistico(numeros)
            elif opcion_principal == "B":
                menu_distribuciones()
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()