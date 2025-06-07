import math

def compute_lcm_gcd(a, b):
    gcd = math.gcd(a, b)
    lcm = abs(a * b) // gcd
    return lcm, gcd

# Input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Output
lcm, gcd = compute_lcm_gcd(a, b)
print("LCM:", lcm)
print("GCD:", gcd)
