from ast import Param
from pickle import PROTO
from random import randrange

words = ["cow", "giraffe", "football","basketball","camp","university","charger","science","human","computer", "octopus","cartoon", "zoo","elevator","airplane","cruise"]

hidden_word = words[randrange(len(words))]
print(hidden_word)
guessed_letters = []
max_rounds = 0

while True:
    max_rounds += 1

    while True:
        letter = input("Choose a letter: ").lower()

        if len(letter) != 1 :
           print("Error! Only one letter: ")

        elif not letter.isalpha():
            print("Error! Write only letters: ")

        elif letter in guessed_letters:
            print("Already guessed that. Choose another letter: ")

        else:
            break

    guessed_letters.append(letter)

    if letter in hidden_word:
        print(f"Letter : {letter} appears {hidden_word.count(letter)}" )

    found = True

    for c in hidden_word:
        if c in guessed_letters:
            print(c,end="")
        else:
            print("_",end="")
            found = False
    print("")

    if found:
        print("Congatulations you found the word!!!")
        break

    if max_rounds >= 10:
        print("You failed!")
        print(f"The hidden word was {hidden_word}")
        break