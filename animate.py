# TODO: convert all the animation clear wait code into here and just import it and run it as functions to keep line lenght down for now before we rewrite it in a less redundant way

import os
import time


def hello_hangman():
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


def loading_game():
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
    os.system('figlet Hello World | lolcat')
    os.system('clear')
    os.system('figlet HELLO WORLD | lolcat')
    os.system('clear')
    os.system('figlet BitCHES')
    os.system('clear')
    os.system('figlet Hello World | lolcat')
    os.system('clear')
    os.system('figlet HELLO WORLD | lolcat')
    os.system('clear')
    os.system('figlet BitCHES')
    os.system('clear')
    os.system('clear')
    os.system('figlet Hello World | lolcat')
    os.system('clear')
    os.system('figlet HELLO WORLD | lolcat')
    os.system('clear')
    os.system('figlet BitCHES')
    os.system('clear')
    os.system('clear')
    os.system('figlet Hello World | lolcat')
    os.system('clear')
    os.system('figlet HELLO WORLD | lolcat')
    os.system('clear')
    os.system('figlet BitCHES')
    os.system('clear')
    os.system('clear')
    os.system('figlet Hello World | lolcat')
    os.system('clear')
    os.system('figlet HELLO WORLD | lolcat')
    os.system('clear')
    os.system('figlet BitCHES')
    os.system('clear')
    os.system('clear')
    os.system('figlet Hello World | lolcat')
    os.system('clear')
    os.system('figlet HELLO WORLD | lolcat')
    os.system('clear')
    os.system('figlet BitCHES')
    os.system('clear')
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
    os.system('clear')
    print('.')
    time.sleep(0.2)
    os.system('clear')
    print('. .')
    time.sleep(0.2)
    os.system('clear')
    print('. . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print('. . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')
    print(' . . . . . . . . .')
    time.sleep(0.2)
    os.system('clear')

hangmanempty = "dont let me die friend!\n  |--------\\\n  |           \n  |           \n__|__"
hangmanhead = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |           \n__|__"
hangmanfirsttorso = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |         |\n__|__"
hangmanleftarm = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\n__|__"
hangmanrightarm = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__"
hangmanlowertorso = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n"
hangmanleftleg = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n           /"
hangmanfull = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n           / \\"
hangmanlist = [hangmanempty, hangmanhead, hangmanfirsttorso, hangmanleftarm, hangmanrightarm, hangmanlowertorso, hangmanleftleg, hangmanfull]

def draw_board(incorrect_guesses, incorrectletters, correctletters, phrase):
    os.system('clear')
    print(hangmanlist[incorrect_guesses])
    print()
    print()
    print(f"Incorrect guesses: {incorrectletters}")
    print()
    print("Hidden Phrase:  ")
    go = True
    hidden_phrase = ""
    for char in phrase:
        if char in correctletters:
            hidden_phrase += char
        if char == " ":
            hidden_phrase += " "
        if char != " " and char not in correctletters:
            hidden_phrase += "_"
    print(hidden_phrase)
    if hidden_phrase == phrase:
        print("You won and your hangman buddy only got hurt a lil but he alive :D!")
        time.sleep(3)
        go = False
    print()
    print()
    return go
