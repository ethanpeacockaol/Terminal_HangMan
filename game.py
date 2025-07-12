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

# define alphabet
alphabet = [' ', 'a', 'b', 'c', 'd',  'e', 'f', 'g',  'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# get phrase for game
phrase = input("Enter hangman phrase: ")
print(f"This is the user's phrase:\n{phrase}")

# check that phrase is only alphabetical characters
allowed_chars_set = set(alphabet)
test  = all(char in allowed_chars_set for char in phrase)
print(test)

# TODO: hey add a go loop for phase validation and sanitization
