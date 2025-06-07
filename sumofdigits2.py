def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Example usage:
n = int(input("Enter a number: "))
print(sum_of_digits(n))
