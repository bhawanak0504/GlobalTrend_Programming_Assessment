def fibonacci(n):
    # Base case: return n if n is 0 or 1
    if n <= 1:
        return n
    # Recursive case: return the sum of the two preceding Fibonacci numbers
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input
n = int(input("Enter the value of n: "))
# Calculate the nth Fibonacci number
fib_number = fibonacci(n)
# Print the result
print(f"The {n}th Fibonacci number is: {fib_number}")