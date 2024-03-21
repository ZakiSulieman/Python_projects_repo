from random import randint
from art import logo

easy_level_attempts = 10
hard_level_attempts = 5

def check_answer(guess,answer, attempts):
   if guess > answer:
      print("Too High")
      return attempts - 1
   elif guess < answer:
      print("Too Low ")
      return attempts - 1
   else:
      print(f"You got it! The answer was {answer}.")


def set_difficulty():
   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
   if level == 'easy':
      return easy_level_attempts
   else:
      return hard_level_attempts
   
def game():
   print(logo)
   answer = randint(1,100)
   print("Welcome to the Number Guessing Game!")
   print("I'm thinking of a number between 1 to 100.")
   # print(f"Pssst, the correct answer is {answer}")

   attempts = set_difficulty()

   guess = 0 
   while guess !=  answer:
      print(f"You have {attempts} attempts remaining to guess the number.")

      guess = int(input("Make a guess: "))

      attempts = check_answer(guess,answer, attempts)
      if attempts == 0:
         print("You've run out of guesses, you lose.")
         return
      elif guess != answer:
         print("Guess again: ")




game()



       