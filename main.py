import random



number = random.randint(1, 100)
attempts = 11
guess = 0
print("Welcome to the Python's Official Number gusessing")
print("Rules:")
print("1. Guess any number from 1 to 10.")
print("2. You have only 10 attempts\nso the attempt counter will run and display each time you enter a wrong number")
print("Have fun")
if attempts >= 1:
 while guess != number:
  guess = int(input("enter your guess:"))
  attempts -= 1
  if guess > number:
   print("The number is High!!!")
  elif guess < number:
   print("The number is low!!!")
  else:
   print("Congratulations!!!")
else:
  print("You have lost!\nTry again")
