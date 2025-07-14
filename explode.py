# make explosion animation of hangman if they lose the game
# add the song memory by cats after explosion

import os
import time





hangmanempty = "dont let me die friend!\n  |--------\\\n  |           \n  |           \n__|__"
hangmanhead = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |           \n__|__"
hangmanfirsttorso = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |         |\n__|__"
hangmanleftarm = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\n__|__"
hangmanrightarm = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__"
hangmanlowertorso = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n"
hangmanleftleg = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n           /"
hangmanfull = "dont let me die friend!\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n           / \\"
hangmanlist = [hangmanempty, hangmanhead, hangmanfirsttorso, hangmanleftarm, hangmanrightarm, hangmanlowertorso, hangmanleftleg, hangmanfull]

for frame in hangmanlist:
    print(frame)
    time.sleep(2)
    os.system("clear")
