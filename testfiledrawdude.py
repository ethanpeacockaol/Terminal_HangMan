import time
import os





dont let me die friend!
  |--------\
  |        [ ]
  |        /|\
__|___      |
           / \      





yo, so see that up there we need to animate based off of incorrect or correct guesses that dude right

we have 1 2 3 4 5 6 7 placements being

his head []
his torso |
his left arm /
his right arm \
his penis |
his left leg /
his right leg \ 

right? so we need to just basically we can write it as a single string with spaces and \ns, we can store 7 strings in a list
every incorrect guess iterates the animationaled hangman to the next node to the right this will give the appearance of drawing him from his 
head torso leftarm right arm huge dick left leg and right leg sequentially right?

we also need a string that is just the stand to hang him from right?
so whoops we need 8 strings

okay that should be pretty easy lets save these notes and add it to the game file next


note when we get the the last element in the drawdude list, we have finished drawing the hangman and at that point you lose the game right?

also note we need to incorporate a status of letters already guessed and dissplay them to the user


lets draw an exmaple of this statically below:

in this example the user chose the phrase ethan peacock



dont let me die friend!
  |--------\
  |        [ ]
  |        /|\
__|___      |
           / \      

prev  gues -> [z r l q i m b ..]

PHRASE: e____ _______










right? so at every attempt to guess we update the if incorrect and not in the phrase previous gues slist and print

we update if guessed wrong the hangman draw node to print from

or if guessed right we update the _ hidden characters to include the letter 

for example lets say on the next turn the user or opponent or whatever guesses an a then our next screen will be this:





guess a next frame


dont let me die friend!
  |--------\
  |        [ ]
  |        /|\
__|___      |        hey the drawing isnt correct this is just the finished losed hangman game but hey they guessed a so lets show what the phrase logic would animate to right?
           / \      

prev  gues -> [z r l q i m b ..]

PHRASE: e__a_ __a____


right?? lets program that next
