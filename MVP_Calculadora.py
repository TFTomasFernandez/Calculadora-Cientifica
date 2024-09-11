# Importar la biblioteca math para operaciones matemáticas avanzadas
import math

# Definir la función principal de la calculadora científica
def calculadora_cientifica():
    # Mostrar el mensaje de bienvenida y las operaciones disponibles
    print("Bienvenido a la calculadora científica.")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponencial")
    print("6. Logaritmo")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Raíz cuadrada")
    
    # Bucle infinito para permitir múltiples operaciones hasta que el usuario decida salir
    while True:
        # Solicitar al usuario que seleccione una operación o escriba 'salir' para terminar
        operacion = input("\nSelecciona una operación (1-10) o escribe 'salir' para terminar: ")

        # Si el usuario escribe 'salir', se termina el bucle y la calculadora
        if operacion == 'salir':
            print("Calculadora finalizada.")
            break

        # Operaciones básicas: Suma, Resta, Multiplicación y División
        if operacion in ['1', '2', '3', '4']:
            # Solicitar al usuario que ingrese dos números
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Realizar la operación seleccionada y mostrar el resultado
            if operacion == '1':
                print(f"Resultado: {num1 + num2}")
            elif operacion == '2':
                print(f"Resultado: {num1 - num2}")
            elif operacion == '3':
                print(f"Resultado: {num1 * num2}")
            elif operacion == '4':
                if num2 != 0:
                    print(f"Resultado: {num1 / num2}")
                else:
                    print("Error: División por cero.")

        # Operación exponencial
        elif operacion == '5':
            # Solicitar al usuario que ingrese la base y el exponente
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            # Calcular y mostrar el resultado
            print(f"Resultado: {math.pow(base, exponente)}")

        # Operación de logaritmo
        elif operacion == '6':
            # Solicitar al usuario que ingrese un número
            num = float(input("Ingresa el número: "))
            # Calcular y mostrar el resultado
            print(f"Resultado: {math.log(num)}")

        # Operación de seno
        elif operacion == '7':
            # Solicitar al usuario que ingrese un ángulo en radianes
            angulo = float(input("Ingresa el ángulo en radianes: "))
            # Calcular y mostrar el resultado
            print(f"Resultado: {math.sin(angulo)}")

        # Operación de coseno
        elif operacion == '8':
            # Solicitar al usuario que ingrese un ángulo en radianes
            angulo = float(input("Ingresa el ángulo en radianes: "))
            # Calcular y mostrar el resultado
            print(f"Resultado: {math.cos(angulo)}")

        # Operación de tangente
        elif operacion == '9':
            # Solicitar al usuario que ingrese un ángulo en radianes
            angulo = float(input("Ingresa el ángulo en radianes: "))
            # Calcular y mostrar el resultado
            print(f"Resultado: {math.tan(angulo)}")

        # Operación de raíz cuadrada
        elif operacion == '10':
            # Solicitar al usuario que ingrese un número
            num = float(input("Ingresa el número: "))
            # Calcular y mostrar el resultado si el número es no negativo
            if num >= 0:
                print(f"Resultado: {math.sqrt(num)}")
            else:
                print("Error: Raíz cuadrada de un número negativo no está definida.")
        else:
            # Mensaje de error si la operación seleccionada no es válida
            print("Operación no válida. Intenta de nuevo.")

# Llamar a la función principal para ejecutar la calculadora
calculadora_cientifica()
