def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."


numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))
result = divide_numbers(numerator, denominator)
print(f"Result: {result}")