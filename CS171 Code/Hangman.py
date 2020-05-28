import random
answerlist= ['acquaintance', 'affable', 'awkward', 'bagpipes', 'croquet', 'cryptic', 'dwarves', 'euphoria', 'fervid', 'fishhook', 'fjord', 'gazebo', 'gypsy', 'haiku', 'haphazard', 'hyphen', 'insolent', 'ivory', 'jazzy', 'jinx', 'jukebox', 'jurisdiction', 'kiosk', 'klutz', 'lollygagging', 'mandolin', 'memento', 'mystify', 'neophyte', 'ostracize', 'oxygen', 'pajama', 'phlegm', 'pixel', 'polka', 'pyroclastic', 'quip', 'receipt', 'rhythmic', 'rogue', 'sphinx', 'squawk', 'supercalifragilisticexpialidocious', 'swivel', 'tourniquet', 'tranquil', 'twelfth', 'undulation', 'vendetta', 'wildebeest', 'xenophobia', 'yacht', 'zealous', 'zephyr']
random.shuffle(answerlist)
answer= (answerlist[0])

display = []
display.extend(answer)
unused_correct_letters = []
unused_correct_letters.extend(display)
used_correct_letters = []
used_letters = []

for i in range(len(display)):
    display[i] = "_"

print(' '.join(display))
print()

correct_guesses = 0
incorrect_guesses_left = 8

while correct_guesses < len(answer):
    guess= input("Please guess a letter. You have " + str(incorrect_guesses_left) + " incorrect guesses left: ")
    guess= guess.lower() 
    
    if guess not in used_correct_letters and guess not in unused_correct_letters:
        incorrect_guesses_left= incorrect_guesses_left - 1    

    if guess in used_letters and guess not in used_correct_letters:
        incorrect_guesses_left= incorrect_guesses_left + 1
        print("That letter is not in the word and you guessed it already. Pick another letter.")
    
    if len(guess) != 1 or type(guess) == int:
        incorrect_guesses_left= incorrect_guesses_left + 1
        print("Please enter only a single letter.")

    for i in range(len(answer)):
        if answer[i] == guess and guess in unused_correct_letters:
            display[i] = guess
            correct_guesses= correct_guesses + 1
            unused_correct_letters.remove(guess)
            used_correct_letters.append(guess)

    if guess in used_correct_letters:
        print("Alright, you've used that letter. Pick another letter now.")

    used_letters.append(guess)

    if incorrect_guesses_left <= 0:
        print("Sorry, you're out of guesses. You lose! The answer was: " + answer) 
        quit()
    print(' '.join(display))
    print()

print(answer + " was the answer! Congrats, you guessed the word!")