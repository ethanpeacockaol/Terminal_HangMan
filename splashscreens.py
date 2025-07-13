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
