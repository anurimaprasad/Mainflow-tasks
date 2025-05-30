# Fibonacci Sequence
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Initialize the Fibonacci sequence
fibonacci = []

# Generate the sequence
a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a+b
    
print("Fibonacci sequence:")
print(fibonacci)
