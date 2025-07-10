import random
import time

start = time.time()
chances = 0
number = random.randint(1,100)

print('I am thinking of a number between 1 and 100 \n ' \
'Please select the difficulty level: \n ' \
'1. Easy (10 Chances) \n ' \
'2. Medium (5 Chances) \n ' \
'3. Hard (3 Chances)')

difficulty_s = input("difficulty: ")
difficulty_i = int(difficulty_s)

if (difficulty_i == 1):
   chances +=10
if (difficulty_i == 2):
   chances +=5
if (difficulty_i == 3):
   chances +=3

guess_s = input("Enter your guess: ")
guess_i = int(guess_s)

# change loop and make better later: https://roadmap.sh/projects/number-guessing-game

if (guess_s != number):
   if (guess_i > number):
      print("Incorrect, the number is less than", guess_s)
      guess_s = input("Try again: ")
      chances2 = chances - 1
      chances = chances2
   if (guess_i < number):
      print("Incorrect, the number is greater than", guess_s)
      guess_s = input("Try again: ")
      chances2 = chances - 1
      chances2 = chances
      if chances == 0:
         print("Game over, no more guesses :(")

print("Congratulations, you won!")
end = time.time()
length = str(round(end - start, 2))
print("It took", length,  "seconds!")   
