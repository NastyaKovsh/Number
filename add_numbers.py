# add_numbers.py

def add_numbers():
    try:
        # Получаем числа от пользователя
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        # Складываем числа
        result = num1 + num2

        # Выводим результат
        print(f"Сумма чисел {num1} и {num2} равна: {result}")

    except ValueError:
        print("Ошибка: Введите корректные числа.")

if __name__ == "__main__":
    add_numbers()
