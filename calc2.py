try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Операція (+, -, , /): ")

    if operation == "+":
        print("Результат:", num1 + num2)
    elif operation == "-":
        print("Результат:", num1 - num2)
    elif operation == "":
        print("Результат:", num1 * num2)
    elif operation == "/":
        print("Результат:", num1 / num2)
    else:
        print("Некоректна операція")
except ZeroDivisionError:
    print("Анріал ділити на нуль")
except ValueError:
    print("Леее брат веди правильні числа")