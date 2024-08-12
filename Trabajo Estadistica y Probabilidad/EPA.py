import statistics
import math
from tabulate import tabulate

# Funciones estadísticas

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
    return frec_porcent_acumulada

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
            print("10. Visualizar FRECUENCIA RELATIVA ACUMULADA.")
            print("11. Visualizar FRECUENCIA PORCENTUAL ACUMULADA.")
            print("12. Calcular y mostrar el COEFICIENTE DE CURTOSIS.")
            print("0. Regresar al menú principal\n")

            opciones = input("Ingrese los números de las opciones que desea visualizar, separados por comas (por ejemplo: 1,2,3): ")
            opciones = [opcion.strip() for opcion in opciones.split(',')]

            if '0' in opciones:
                return

            for opcion in opciones:
                if opcion == '1':
                    print(tabulate([["MEDIA", calcular_media(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '2':
                    moda, frecuencia = calcular_moda(numeros)
                    if moda is None:
                        print("No hay moda en los datos.")
                    else:
                        print(tabulate([["MODA", f"{moda} (Frecuencia: {frecuencia})"]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '3':
                    print(tabulate([["MEDIANA", calcular_mediana(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '4':
                    print(tabulate([["DESVIACIÓN ESTÁNDAR", calcular_desviacion(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '5':
                    print(tabulate([["VARIANZA", calcular_varianza(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '6':
                    print(tabulate([["FRECUENCIA ABSOLUTA", frecuencia_absoluta(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '7':
                    print(tabulate([["FRECUENCIA RELATIVA", frecuencia_relativa(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '8':
                    print(tabulate([["FRECUENCIA PORCENTUAL", frecuencia_porcentual(numeros)]], headers=["Operación", "Resultado en porcentajes (%)"], tablefmt="grid"))
                elif opcion == '9':
                    print(tabulate([["FRECUENCIA ABSOLUTA ACUMULADA", frecuencia_absoluta_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '10':
                    print(tabulate([["FRECUENCIA RELATIVA ACUMULADA", frecuencia_relativa_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '11':
                    print(tabulate([["FRECUENCIA PORCENTUAL ACUMULADA", frecuencia_porcentual_acumulada(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                elif opcion == '12':
                    print(tabulate([["COEFICIENTE DE CURTOSIS", coeficiente_curtosis(numeros)]], headers=["Operación", "Resultado"], tablefmt="grid"))
                else:
                    print(f"Opción {opcion} no válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese opciones válidas.")

def menu_distribuciones():
    while True:
        try:
            print("\nDistribuciones - Seleccione una opción:")
            print("1. Distribución Binomial.")
            print("2. Distribución de Poisson.")
            print("3. Distribución Hipergeométrica.")
            print("4. Distribución Normal (Gaussiana).")
            print("0. Regresar al menú principal\n")

            opcion = int(input("Ingrese el número de la opción que desea utilizar: "))
            if opcion == 0:
                return
            elif opcion == 1:
                n = int(input("Ingrese el número de ensayos (n): "))
                p = float(input("Ingrese la probabilidad de éxito (p): "))
                k = int(input("Ingrese el número de éxitos deseados (k): "))
                resultado = distribucion_binomial(n, p, k)
                print(tabulate([["PROBABILIDAD BINOMIAL", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            elif opcion == 2:
                lambd = float(input("Ingrese el valor de lambda (λ): "))
                k = int(input("Ingrese el número de ocurrencias deseadas (k): "))
                resultado = distribucion_poisson(lambd, k)
                print(tabulate([["PROBABILIDAD DE POISSON", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            elif opcion == 3:
                n = int(input("Ingrese el tamaño de la muestra (n): "))
                M = int(input("Ingrese el número de éxitos en la población (M): "))
                N = int(input("Ingrese el tamaño de la población (N): "))
                k = int(input("Ingrese el número de éxitos deseados en la muestra (k): "))
                resultado = distribucion_hipergeometrica(n, M, N, k)
                print(tabulate([["PROBABILIDAD HIPERGEOMÉTRICA", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            elif opcion == 4:
                x = float(input("Ingrese el valor de x: "))
                mu = float(input("Ingrese la media (μ): "))
                sigma = float(input("Ingrese la desviación estándar (σ): "))
                resultado = distribucion_normal(x, mu, sigma)
                print(tabulate([["DISTRIBUCIÓN NORMAL", resultado]], headers=["Operación", "Resultado"], tablefmt="grid"))
            else:
                print("Opción no válida. Intente nuevamente o ingrese 0 para regresar al menú principal.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

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
