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



losebanner = ['you lose!', '        you lose!']
uhh = 0
for i in range(50): 
    os.system("clear")
    print(losebanner[uhh])
    if i % 2 == 0:
        uhh -= 1
    else:
        uhh += 1
    time.sleep(1) 
