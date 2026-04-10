def vowels_counter(sentence):
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count = count + 1
    return count

sentence = input("Enter the sentence: ")
no_of_vowels = vowels_counter(sentence)
print(no_of_vowels)