from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()

###################### perosonal achievement
# from art import logo
# from random import randint

# def compare(num,count):
#   count-=1;
#   if num>answer:
#     print("Too high\nGuess again.")
#     print (f"You have {count} attempts remaining to guess the number.")

#   elif num<answer:
#     print("Too low\nGuess again.")
#     print (f"You have {count} attempts remaining to guess the number.")
#   else:
#     print ("Correct! You got it!")
#     return True

#   return count

# print (logo)
# print ("Welcome to the Number Guessing Game!")
# print ("I'm thinking of a number between 1 and 100.")
# skill=input ("Choose a difficulty. Type 'easy' or 'hard'")
# answer=randint (1,100)
# print (answer)

# if (skill=="easy"):
#   print ("You have 10 attempts remaining to guess the number.")
#   count=10
#   while (count!=0 and count!=True):
#     num=int(input("Make a guess: "))
#     count=compare(num,count)

# else:
#   print ("You have 5 attempts remaining to guess the number.")
#   count=5
#   while (count!=0 and count!=True):
#     if count==0:
#       print("You've run out of guesses, you lose.")
#     else:
#       num=int(input("Make a guess: "))
#       count=compare(num,count)
  
