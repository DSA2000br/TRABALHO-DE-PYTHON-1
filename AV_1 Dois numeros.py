print("Calculadora de divisão não suprema.")
while True:
    try:
        num1 = int(input("Digite o numero 1: "))
        num2 = int(input("Digite o numero 2: "))
        print(f"{num1} / {num2} = {num1 / num2}")
        break
    except ValueError:
        print("Digite NUMEROS inteiros.")
    except ZeroDivisionError:
        print("Zero? serio?")