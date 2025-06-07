def reverse_list(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        # Swap elements
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
    return lst

# Input
lst = list(map(int, input("Enter list elements separated by space: ").split()))

# Output
reversed_lst = reverse_list(lst)
print("Reversed list:", reversed_lst)
