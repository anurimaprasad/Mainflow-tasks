def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

text = "Empowering Tomorrow"
length = string_length(text)
print("Length of the string:", length)
