# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 19:02:55 2021

@author: Gregory
"""
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number netween 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
    print(f"Yay, congrats. You have guessed the number {random_number}")
        
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low != high:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)??")
        if feedback =="h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
            
    print(f"Yay! The computer guessed your, {guess}, correctly!")
    
computer_guess(10)