while True:
    print("Selecciona una operacion:\n"
        "1. Suma\n"
        "2. Resta\n"
        "3. Multiplicacion\n"
        "4. Division")

    eleccion = input("Ingresa tu eleccion (1/2/3/4): ")

    if eleccion in ('1', '2', '3', '4'):
        numero_1 = float(input("Ingresa el primer numero: "))
        numero_2 = float(input("Ingresa el segundo numero: "))

        if eleccion == '1':
            print(numero_1 + numero_2)
        elif eleccion == '2':
            print(numero_1 - numero_2)
        elif eleccion == '3':
            print(numero_1 * numero_2)
        elif eleccion == '4':
            if numero_2 == 0:
                print("No se puede dividir por 0")
            else:
                print(numero_1 / numero_2)
        siguiente = input("Quieres hacer otra operacion? (si/no): ")
        if siguiente.lower() != 'si':
            break
    else:
        print("Eleccion invalida")