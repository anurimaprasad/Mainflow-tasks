def remove_duplicates(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)
