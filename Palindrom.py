# Palindrom check

def is_palindrome(s):
    return s == s[::-1]

# Example
input_str = "radar"
print("Is Palindrome:", is_palindrome(input_str))
