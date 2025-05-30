# Leap year check
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example
year = 2024
print("Is Leap Year:", is_leap_year(year))  # Output: True
