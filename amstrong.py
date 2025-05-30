# Armstong number
def is_armstrong_number(n):
    digits = str(n)
    num_digits = len(digits)
    total = sum(int(digit) ** num_digits for digit in digits)
    return total == n

# Example
number = 153
print("Is Armstrong Number:", is_armstrong_number(number))  # Output: True
