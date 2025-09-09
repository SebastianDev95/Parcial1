
def ejercicio5():
    estudiantes = []
    while True:
        nombre = input("Ingrese su nombre o fin para terminar: ")
        if nombre.lower() == "fin":
            break
        try:
            nota = int(input("Ingrese su nota: "))
        except ValueError:
            print("La nota debe ser un número entero.")
            continue
        estudiantes.append((nombre, nota))
    print("Estudiantes ingresados:")
    for nombre, nota in estudiantes:
        print(f"Nombre: {nombre}, Nota: {nota}")
    lista_diccionarios = [{"nombre": nombre, "nota": nota} for nombre, nota in estudiantes]
    print(lista_diccionarios)

    # Promedio de notas
    if estudiantes:
        suma = 0
        for _, nota in estudiantes:
            suma += nota
        promedio = suma / len(estudiantes)
    else:
        promedio = 0
    print(f"Promedio de notas: {promedio}")

    # Mejor estudiante
    if estudiantes:
        mejor = estudiantes[0]
        for est in estudiantes:
            if est[1] > mejor[1]:
                mejor = est
        print(f"Mejor estudiante: {mejor[0]}, Nota: {mejor[1]}")

    # Peor estudiante
    if estudiantes:
        peor = estudiantes[0]
        for est in estudiantes:
            if est[1] < peor[1]:
                peor = est
        print(f"Peor estudiante: {peor[0]}, Nota: {peor[1]}")

ejercicio5()
