def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Check if it's a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

text = "Empowering Tomorrow"
vowels, consonants = count_vowels_consonants(text)
print("Vowels:", vowels)
print("Consonants:", consonants)
