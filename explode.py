# make explosion animation of hangman if they lose the game
# add the song memory by cats after explosion

import os
import time





hangmanempty = "uh oh\n  |--------\\\n  |           \n  |           \n__|__"
hangmanhead = "uh oh\n  |--------\\\n  |        [ ]\n  |           \n__|__"
hangmanfirsttorso = "uh oh\n  |--------\\\n  |        [ ]\n  |         |\n__|__"
hangmanleftarm = "uh oh\n  |--------\\\n  |        [ ]\n  |        /|\n__|__"
hangmanrightarm = "uh oh\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__"
hangmanlowertorso = "uh oh\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n"
hangmanleftleg = "uh oh\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n           /"
hangmanfull = "uh oh\n  |--------\\\n  |        [ ]\n  |        /|\\\n__|__       |\n           / \\"
hangmanlist = [hangmanempty, hangmanhead, hangmanfirsttorso, hangmanleftarm, hangmanrightarm, hangmanlowertorso, hangmanleftleg, hangmanfull]


os.system('clear')

for frame in hangmanlist:
    print(frame)
    time.sleep(1)
    os.system("clear")



losebanner = ['you lose!', '                                             you lose!']
uhh = 0
for i in range(20): 
    os.system("clear")
    print(losebanner[uhh])
    if i % 2 == 0:
        uhh -= 1
    else:
        uhh += 1
    time.sleep(0.5) 
