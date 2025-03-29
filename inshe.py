try:
    number = float(input("Напиши пінкод від карточки: "))
    if number < 0:
        print("Число не може бути від'ємним")
    else:
        print("Квадратний корінь:", number ** 0.5)
except ValueError:
    print("Правильно напиши пінкод")






try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    print("Результат ділення:", num1 / num2)
except ZeroDivisionError:
    print("Анріал ділити на нуль")
except ValueError:
    print("Правильно напиши пінкод")



    
try:
    numbers = list(map(float, input("через пробільчик братюна: ").split()))
    print("Середнє значєниє:", sum(numbers) / len(numbers))
except ValueError:
    print("Правильно напиши пінкод")
except ZeroDivisionError:
    print("Список чисел порожній")