vowels = ['a', 'e', 'i', 'o', 'u']

word = input("Enter a word: ")

word_without_vowels = ''.join([char for char in word if char.lower() not in vowels])
print(word_without_vowels)


#second question checking if all letter start with P

word1= "Peter"
word2= "Photography"

def check_for_p(word1, word2):
    if list(word1)[0] == list(word2)[0]:
        return True
    else:
        return False

#calling back the function and passing urguments
print(check_for_p(word1, word2))
