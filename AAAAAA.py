num1 = float(input("Введите первое число: "))
operator = input("Введите операцию (+, -, *, /): ")
num2 = float(input("Введите второе число: "))

match operator:
    case "+":
        print(f"{num1} + {num2} =", num1 + num2)
    case "-":
        print(f"{num1} - {num2} =", num1 - num2)
    case "*":
        print(f"{num1} * {num2} =", num1 * num2)
    case "/":
        if num2 == 0:
            print("Ошибка")
        else:
            print(f"{num1} / {num2} =", num1 / num2)
    case _:
        print("Ошибка")