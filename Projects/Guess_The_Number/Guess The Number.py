#Guess the Number
import random
rand1 = random.randint(0,100)
guess = 1 #Number of guess should be 9

while (guess <=9):
    user_input = int(input("Guess a Number: "))
    if user_input > rand1:
        diff = user_input - rand1
        print(f"Your input is greater than the number\n>>The difference is {diff}")
    elif user_input < rand1:
        diff = user_input - rand1
        print (f"Your input is less than the number\n>>The difference is {diff}")
    elif user_input == rand1:
        print(f"YOU WON!!\nYou took {guess} tries to win the game")
        break
    print(9-guess, " Tries left !! " )
    guess = guess + 1
if guess > 9:
    print("you lost no number of tries")

