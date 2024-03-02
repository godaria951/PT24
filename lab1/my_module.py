def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ділення на нуль неможливе"

numerator = 10
denominator = 2
result = divide(numerator, denominator)
print(f"Результат ділення {numerator} на {denominator}: {result}")

