vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Enter a word: ")

word_without_vowels = ''.join([char for char in word if char.lower() not in vowels])
print(word_without_vowels)
