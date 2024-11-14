# ALLAN ABARCA

empleados = {}

def incluir_empleado():
    id_empleado = input("Ingrese cédula del empleado: ")
    nombre = input("Ingrese el nombre del empleado: ")
    empleados[id_empleado] = {"Nombre": nombre, "Horas Laboradas": []}
    print("Empleado incluido con éxito.")

def consultar_empleado():
    id_empleado = input("Ingrese cédula del empleado que desea consultar: ")
    if id_empleado in empleados:
        horas = empleados[id_empleado]["Horas Laboradas"]
        print(f"ID: {id_empleado}")
        print(f"Nombre: {empleados[id_empleado]['Nombre']}")
        print("Horas laboradas por quincena: ")
        if horas:
            for index, hora in enumerate(horas, start=1):
                print(f"  Quincena {index}: {hora} horas")
        else:
            print("  No se han registrado horas.")
    else:
        print("El empleado con ésa cédula no existe.")

def registrar_horas():
    while True:
        id_empleado = input("Ingrese cédula del empleado para registrar horas laboradas: ")
        if id_empleado in empleados:
            horas = float(input("Ingrese el número de horas laboradas en esta quincena: "))
            empleados[id_empleado]["Horas Laboradas"].append(horas)
            print("Horas laboradas registradas con éxito.")
        else:
            print("El empleado con ésa cédula no existe.")

        continuar = input("¿Desea registrar horas para otro empleado? (S/N): ").strip().lower()
        if continuar != "sí":
            break

def borrar_empleado():
    id_empleado = input("Ingrese cédula del empleado que desea borrar: ")
    if id_empleado in empleados:
        del empleados[id_empleado]
        print("Empleado borrado con éxito.")
    else:
        print("El empleado con ésa cédula no existe.")

def menu():
    while True:
        print("\nMenú Principal")
        print("1. Incluir Empleado")
        print("2. Consultar Empleado")
        print("3. Registrar Horas Laboradas")
        print("4. Borrar Empleado")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            incluir_empleado()
        elif opcion == "2":
            consultar_empleado()
        elif opcion == "3":
            registrar_horas()
        elif opcion == "4":
            borrar_empleado()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()
