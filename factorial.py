#Factorial Calculation

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Input from the user
try:
    n = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {n} is {factorial(n)}")
except ValueError:
    print("Invalid input. Please enter an integer.")
