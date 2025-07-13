# Terminal Hangman


# TODO: we need to tell the user to pass the phone to their opponent

# TODO: we need to get a letter guess from the oponent

# TODO: if the letter is in the phrase we need to update the blank representations to include the correctly guessed letter

# TODO: if the letter is not in the phrase we need to draws a  piece of the hangman and add the letter to the incorrect guesses list

# TODO: we need to draw a blank represenetation of the phrase so the user can see the length of the statement as the play the game



# ____________ DOING ________________________________



# TODO: if the user writes a phrase that does not include alphabetical charcters or a space character ask them to repeat entry until its only alphabetical characters or space

# TODO: before telling user to pass the phone to the opponent we need to validate that the phrase they entered is correct (Y/N) if yes start game for opponent, if no get user to re-enter phrase

# TODO: truncate space from end of phrase if there is one or some




import os
import time
import splashscreens

splashscreens.hello_hangman()
alphabet = [' ', 'a', 'b', 'c', 'd',  'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
allowed_chars_set = set(alphabet)

go = True
while go:
    os.system('clear')
    phrase = input("Enter hangman phrase: ")
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


splashscreens.loading_game()







# TODO: print out the phrase like this example phrase == 'hey there' you should print "___ _____"
# TODO: convert  the game start splash screen into a loop but for now procedural it for to get there quick
# TODO: lint code, clean code, remove redundancies this redacted as fuck but we wanna build logic first right? right
# TODO: hey add a go loop for phase validation and sanitization
