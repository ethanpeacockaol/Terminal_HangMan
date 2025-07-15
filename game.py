# Terminal Hangman

import os
import time
import animate

animate.hello_hangman()
alphabet = [' ', 'a', 'b', 'c', 'd',  'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
allowed_chars_set = set(alphabet)

go = True
while go:
    os.system('clear')
    phrase = input("Enter hangman phrase: ")
    phrase = phrase.lower()
    onlyalphabeticalcharacters = all(char in allowed_chars_set for char in phrase)
    if onlyalphabeticalcharacters == False:
        print('only alphabetical characters and space characters are allowed :(')
        time.sleep(5)
    else:
        os.system('clear')
        print('___________________________________________________________')
        print(f"{phrase}")
        print('___________________________________________________________')
        print('is the phrase correct?', end=" ")
        yn = input("(Y^N):").lower()

        if yn == 'y' and onlyalphabeticalcharacters == True:
            go = False

animate.loading_game()
os.system('clear')
_ = input("Please pass the phone to your opponent and hit Enter to start the game.")

incorrect_guesses = 0
incorrect_letters = []
correct_letters = []
guessalphabet = alphabet.copy()
del(guessalphabet[0])
allowed_guess_set = set(guessalphabet)
max_incorrect_guesses = 7

go = True
while go:
    os.system('clear')
    go = animate.draw_board(incorrect_guesses, incorrect_letters, correct_letters, phrase)
    if incorrect_guesses == max_incorrect_guesses:
        go = False
        print("\n\nYou lose and you let your lil hangman buddy die :(")
        time.sleep(2)
        os.system("python explode.py")
    if go == False:
        break
    guess = input("Please guess an alphabetical charcter: ")
    guess = guess.lower()
    guess_single_char = len(guess) == 1
    guessonlyalphabet = all(char in allowed_guess_set for char in guess)
    if guess_single_char == True and guessonlyalphabet == True and guess not in incorrect_letters:
        if guess in phrase:
            correct_letters += guess
        if guess not in phrase:
            incorrect_letters += guess
            incorrect_guesses += 1
    else:
        print("\n\nhey you didnt make a correct guess selection, please try again :(")
        time.sleep(3)

