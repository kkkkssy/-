import math

# Функция для вычисления выражения
def compute_expression(x, num):
    try:
        log_base = abs(num / 10) + 2
        log_argument = (1 - num) / math.sin(x + num)

        if log_argument <= 0:
            raise ValueError("Error")
        
        first_component = math.log(log_argument, log_base)
        second_component = abs(math.cos(math.log(abs(x))) / num)
        
        result = max(first_component, second_component)
        return result
    except ValueError as e:
        raise ValueError(f"Error")
    except ZeroDivisionError:
        raise ValueError("Error")

# Функция для ввода данных с проверкой
def get_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Ошибка ввода данных, попробуйте снова.")

# Главная функция программы
def main():
    print("Программа для вычисления выражений.")
    
    # Ввод начальных и конечных значений
    start_x = get_input("Введите начальное значение X: ")
    end_x = get_input("Введите конечное значение X: ")
    
    # Ввод DeltaX с проверкой
    while True:
        delta_x = get_input("Введите шаг изменения deltaX: ")
        if delta_x > 0:
            break
        print("Ошибка: шаг deltaX должен быть положительным. Попробуйте снова.")
    
    # Заголовок таблицы
    print("+----------+---------------+---------------------------+")
    print("| Номер    |       X       |          Результат        |")
    print("+----------+---------------+---------------------------+")
    
    constant_num = 22  # Фиксированное значение num
    row_num = 1

    # Итерация по значениям X
    x = start_x
    while x <= end_x + 1e-9:  # Допустимая погрешность для сравнения с end_x
        try:
            result = compute_expression(x, constant_num)
            print(f"| {row_num:>8} | {x:>13.6f} | {result:>25.7f} |")
        except ValueError as e:
            print(f"| {row_num:>8} | {x:>13.6f} | {str(e):>25} |")
        
        print("+----------+---------------+---------------------------+")
        row_num += 1
        x += delta_x

if __name__ == "__main__":
    main()
