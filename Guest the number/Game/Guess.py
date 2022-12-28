'''
Created on 9/09/2022

@author: fabian
'''

from random import randint


start = 1

end = 1000

value = randint(start, end)

print("The computer choose a number between", start , " and ", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    
    if guess < value:
        print("The number is Higher")
    elif guess > value:
        print("The number is Lower")

print("Congratulations!!! You gussed the number. You won.")
