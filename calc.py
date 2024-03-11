def calculate(expression):
    elements = expression.split()
    if len(elements) != 3:
        raise ValueError("Неправильный формат выражения")

    a, operator, b = elements
    a = int(a)
    b = int(b)
    if not (1 <= a <= 10 and 1 <= b <= 10):
        raise ValueError("Числа должны быть от 1 до 10 включительно")

    if operator == '+':
        return str(a + b)
    elif operator == '-':
        return str(a - b)
    elif operator == '*':
        return str(a * b)
    elif operator == '/':
        if b == 0:
            raise ValueError("Деление на ноль")
        return str(a // b)
    else:
        raise ValueError("Неподдерживаемая операция")

def main(input_str):
    try:
        result = calculate(input_str)
        return "Результат: " + result
    except ValueError as e:
        return "Ошибка: " + str(e)

input_expression = input("Введите арифметическое выражение (например, 5 + 3): ")
print(main(input_expression))