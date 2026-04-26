# ============================
# DATA LAB - ENTREGA 1 (MESSI)
# ============================

def cargar_datos(ruta):
    datos = []
    archivo = open(ruta, "r", encoding="utf-8")

    encabezado = archivo.readline().strip().split(",")

    for linea in archivo:
        linea = linea.strip()
        columnas = linea.split(",")
        datos.append(columnas)

    archivo.close()
    return encabezado, datos


def mostrar_columnas(encabezado):
    print("\nColumnas disponibles:")
    for i in range(len(encabezado)):
        print(f"{i}: {encabezado[i]}")
    print()


def buscar(datos, encabezado, termino):
    resultados = []

    for fila in datos:
        for campo in fila:
            if termino.lower() in campo.lower():
                resultados.append(fila)
                break

    print("\nResultados encontrados:\n")
    print(" | ".join(encabezado))
    print("-" * 60)

    for r in resultados:
        print(" | ".join(r))

    print(f"\nSe encontraron {len(resultados)} registros.\n")


def estadisticas(datos, encabezado, indice):
    valores = []

    for fila in datos:
        try:
            numero = float(fila[indice])
            valores.append(numero)
        except:
            continue

    if len(valores) == 0:
        print("\nNo hay datos numéricos en esa columna.\n")
        return

    maximo = valores[0]
    minimo = valores[0]
    suma = 0

    for v in valores:
        if v > maximo:
            maximo = v
        if v < minimo:
            minimo = v
        suma += v

    promedio = suma / len(valores)

    print(f"\nEstadísticas de: {encabezado[indice]}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")
    print(f"Promedio: {promedio:.2f}\n")


def filtrar(datos, encabezado, indice, limite):
    resultados = []

    for fila in datos:
        try:
            valor = float(fila[indice])
            if valor > limite:
                resultados.append(fila)
        except:
            continue

    print(f"\nRegistros donde {encabezado[indice]} > {limite}\n")
    print(" | ".join(encabezado))
    print("-" * 60)

    for r in resultados:
        print(" | ".join(r))

    print(f"\nTotal encontrados: {len(resultados)}\n")


def menu():
    encabezado, datos = cargar_datos("messi.csv")

    while True:
        print("====== DATA LAB - MESSI ======")
        print("1. Buscar registros")
        print("2. Estadísticas de columna")
        print("3. Filtrar por valor")
        print("4. Ver columnas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            termino = input("Ingrese término a buscar: ")
            buscar(datos, encabezado, termino)

        elif opcion == "2":
            mostrar_columnas(encabezado)
            indice = int(input("Seleccione columna numérica: "))
            estadisticas(datos, encabezado, indice)

        elif opcion == "3":
            mostrar_columnas(encabezado)
            indice = int(input("Seleccione columna numérica: "))
            limite = float(input("Ingrese valor mínimo: "))
            filtrar(datos, encabezado, indice, limite)

        elif opcion == "4":
            mostrar_columnas(encabezado)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida\n")


menu()
