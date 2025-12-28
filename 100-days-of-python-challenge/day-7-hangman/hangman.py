import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'x', 'z']
words_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words_list)
lives = 6
wordparts = []
newword = ''.join([letter if letter in wordparts else '-' for letter in word])

print('Welcome to the PyHangman Game!')

guess = input('Please enter a letter: ')

while lives > 0 and newword != word:
    if guess in word:
        wordparts.append(guess)
        newword = ''.join([letter if letter in wordparts else '-' for letter in word])
        print(f'Good guess! {newword}')
        guess = input('Please enter a letter: ')
    elif guess not in word and guess in letters:
        lives -= 1
        print(f'Wrong guess. You have {lives} lives left.')
        guess = input('Please enter a letter: ')
    else:
        print('Invalid input. Please enter a lowercase letter from the English alphabet.')
        guess = input('Please enter a letter: ')

if lives == 0:
    print(f'Game over! The word was "{word}".')

if newword == word:
    print(f'Congratulations! You guessed the word "{word}".')