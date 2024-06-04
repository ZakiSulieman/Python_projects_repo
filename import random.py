import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


print(f'Pssst, the solution is {chosen_word}.')


display = []
for char in chosen_word:
    display.append("-")
print(display)

guess = input("Guess a letter: ").lower()
for position  in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter



print(display)
      
      

        
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
