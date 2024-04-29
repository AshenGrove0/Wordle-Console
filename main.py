import random as rand
import os
with open('words.txt',"r") as f:
    words = f.readlines()

print('''\u001b[35m\t\t\t\t\tWordle\u001b[0m
      \u001b[36mGuess the 5 letter word. You have 6 chances\u001b[0m
      \u001b[32mGreen = right letter, right location\u001b[0m
      \u001b[33mYellow = right letter, wrong location\u001b[0m
      \u001b[37mWhite = wrong letter, wrong location\u001b[0m''')

while True:
    word_to_guess = words[rand.randint(0,len(words)-1)]
    guesses = []
    for i in range(1,7):
        while True:
            guess = input(f"Guess {i}:").lower() + "\n"
            print(guess)
            if guess in words:
                letters = []
                for i in range(len(guess)):
                    if guess[i] == word_to_guess[i]:
                        letters.append(f"\u001b[32m{guess[i]}\u001b[0m")
                    elif guess[i] in word_to_guess and guess[i] != word_to_guess[i]: 
                        letters.append(f"\u001b[33m{guess[i]}\u001b[0m")
                    else:
                        letters.append(f"\u001b[37m{guess[i]}\u001b[0m")
                    word = ''
                    for letter in letters:
                        word += letter
                guesses.append(word.strip("\n"))
                for guess in guesses:
                    print(guess)
                if guess == word_to_guess:
                    print("Congrats! You guessed the word!")
                break
            else:
                print("That is not a valid word. Try again.")
    print(f"The correct word was: \u001b[32m{word_to_guess}\u001b[0m")
    os.system('clear')
