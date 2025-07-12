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
os.system('clear')
os.system('figlet Hello HangMan | lolcat')
os.system('echo .')
time.sleep(0.5)
os.system('echo .')
time.sleep(0.4)
os.system('echo .')
time.sleep(0.2)
os.system('echo .')
time.sleep(0.7)

# define alphabet
alphabet = [' ', 'a', 'b', 'c', 'd',  'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# convert the alhabet into an allowed set of input
allowed_chars_set = set(alphabet)


# phrase input validation loop
go = True
while go:
    # get phrase for the game
    os.system('clear')
    phrase = input("Enter hangman phrase: ")
    #print(f"This is the user's phrase:\n{phrase}")

    # check that phrase is only alphabetical characters
    onlyalphabeticalcharacters = all(char in allowed_chars_set for char in phrase)
    if onlyalphabeticalcharacters == False:
        print('only alphabetical characters and space characters are allowed :(')
        time.sleep(5)
    else:
        # validate input to user to make sure phrase is correct
        os.system('clear')
        print('___________________________________________________________')
        print(f"{phrase}")
        print('___________________________________________________________')
        print('is the phrase correct?', end=" ")
        yn = input("(Y^N):").lower()

        # can we break from input phrase loop yet?
        if yn == 'y' and onlyalphabeticalcharacters == True:
            go = False


print(f"{phrase}")        
os.system('clear')
os.system('figlet Game Starting... | lolcat')
time.sleep(1.2)
os.system('clear')
os.system('figlet H | lolcat')
os.system('clear')
os.system('figlet HE | lolcat')
os.system('clear')
os.system('figlet HEL | lolcat')
os.system('clear')
os.system('figlet HeLL | lolcat')
os.system('clear')
os.system('figlet HELLo | lolcat')
os.system('clear')
os.system('figlet HELLO w | lolcat')
os.system('figlet HELLO WOR | lolcat')
os.system('clear')
os.system('figlet HELLO - | lolcat')
os.system('clear')
os.system('figlet HELLO --- | lolcat')
os.system('clear')
os.system('figlet HELLO H-- | lolcat')
os.system('clear')
os.system('figlet HELLO HA- | lolcat')
os.system('clear')
os.system('figlet HELLO HAN | lolcat')
os.system('clear')
os.system('figlet HELLO HANG | lolcat')
os.system('clear')
os.system('figlet HELLO HANGM | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMA | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMAN | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMAN | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMAN | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMAN | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMAN | lolcat')
os.system('clear')
os.system('figlet HELLO HANGMAN | lolcat')
time.sleep(3.2)
# TODO: convert  the game start splash screen into a loop but for now procedural it for to get there quick
# TODO: lint code, clean code, remove redundancies this redacted as fuck but we wanna build logic first right? right
# TODO: hey add a go loop for phase validation and sanitization
