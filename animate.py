# TODO: convert all the animation clear wait code into here and just import it and run it as functions to keep line lenght down for now before we rewrite it in a less redundant way

import os
import time


def hello_hangman():
    os.system('clear')
    os.system('echo H')
    os.system('clear')
    time.sleep(1)
    os.system('echo He')
    os.system('clear')
    time.sleep(.7)
    os.system('echo HEl')
    os.system('clear')
    time.sleep(0.3)
    os.system('echo HELlO')
    os.system('clear')
    os.system('echo Hello HA     G')
    os.system('clear')
    os.system('echo Hello HA   G')
    os.system('clear')
    os.system('echo HEllo Han G')
    os.system('clear')
    os.system('echo Hello HanM')
    os.system('clear')
    os.system('echo Hello HangMa')
    os.system('clear')
    os.system('echo Hello HangMan')
    os.system('clear')
    time.sleep(1)
    os.system('echo Hello HangMan .....')
    time.sleep(3)
    os.system('clear')

def loading_game():
  for i in range(1000000):
    print(9, end="6")
  print()
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
