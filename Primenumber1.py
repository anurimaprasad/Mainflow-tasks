def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, not prime
    return True  # No divisors found, number is prime

# Example usage:
n = int(input("Enter a number: "))
print(is_prime(n))
