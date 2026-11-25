Gastos = []

while True:
    print("Gestor de Gastos Personales")
    print("1. Agregar gasto")
    print("2. Mostrar gastos")
    print("3. Filtrar por categoría")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        descripcion = input("Ingrese la descripción del gasto: ")
        monto = float(input("Ingrese el monto del gasto: "))
        categoria = input("Ingrese la categoría del gasto: ")
        Gastos.append({"descripcion": descripcion, "monto": monto, "categoria": categoria})
        print("Gasto agregado exitosamente.")
        
        
    elif opcion == "2":
        if not Gastos:
            print("No hay gastos registrados.")
        else:
            print("Lista de gastos:")
            for gasto in Gastos:
                print(f"Descripción: {gasto['descripcion']}, Monto: {gasto['monto']}, Categoría: {gasto['categoria']}")

    elif opcion == "3":
        categoria = input("Ingrese la categoría para filtrar: ")
        gastos_filtrados = [gasto for gasto in Gastos if gasto['categoria'] == categoria]
        if not gastos_filtrados:
            print(f"No hay gastos registrados para la categoría '{categoria}'.")
        else:
            print(f"Lista de gastos para la categoría '{categoria}':")
            for gasto in gastos_filtrados:
                print(f"Descripción: {gasto['descripcion']}, Monto: {gasto['monto']}, Categoría: {gasto['categoria']}")
    elif opcion == "4":
        print("Saliendo del gestor de gastos.")
        break
        
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")