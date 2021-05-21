#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 22 00:01:46 2021

@author: avanishbidar
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

guess = int(input('Enter the magic number'))
store = []
attempt =1

x = int(input('Enter you first guess'))
if guess == x:
    print('You guess it correctly in the first guess')
elif x in range(guess,guess+11) or x in range(guess -10 ,guess):
    print('warm')
else:
    print('cold')
while guess != x:
    y = int(input('Enter your guess'))
    if guess == y:
        print(f'You guessed it correctly in {attempt}th attemp')
        break
    if y > guess:
        store.append(y-guess)
    elif y < guess:
        store.append(guess-y)
    if store[len(store)-1] < store[len(store)-2]:
        print('warmer')
    else:
        print('colder')
    
    attempt = attempt + 1
    

    
