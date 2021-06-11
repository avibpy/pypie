#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:31:11 2021

@author: avanishbidar
"""

my_list = [[1,2,3],[4,5,6],[7,8,9]]


def display(a):
    print(f'{a[0][0]} | {a[0][1]} | {a[0][2]}')
    print('----------')
    print(f'{a[1][0]} | {a[1][1]} | {a[1][2]}')
    print('----------')
    print(f'{a[2][0]} | {a[2][1]} | {a[2][2]}')


def user_first():
    user_choice_variable = ''
    while user_choice_variable not in ['X', 'O']:
        user_choice_variable = input('Enter X or O')
        if user_choice_variable not in ['X', 'O']:
            print('Wrong choice')
    if user_choice_variable == 'X':
        return True
    else:
        return False
        
#Take the cell input from the user 

def user_input():
    choice = ''
    while choice not in  range(1,10) :
        choice = int(input('Enter you cell number '))
        
    if choice not in range(1,9):
        print('Please make the correct selection ')
    return choice 


#Change the Logic using counter 


def flagger(Flag):
    
    if Flag == True:
        return False
    else:
        return True
    
def flagger_update(Flag):
    if Flag == True:
        return 'X'
    else:
        return 'O'

#Modify cell output 
def cell_modification(my_list, choice, Flag):
    choice = choice

    if choice in range(1,4):
        my_list[0][choice -1] = flagger_update(Flag)
    if choice in range(4,7):
        my_list[1][choice -4] = flagger_update(Flag)    
    if choice in range(7,10):
        my_list[2][choice -7] = flagger_update(Flag)
    
    return my_list

def game_on():
    print('Want to continue game')
    continue_game = ''
    while continue_game not in ['Y', 'N']:
        continue_game = input('Y or N')
        if continue_game not in ['Y','N']:
            print('Wrong entry')
    return continue_game


def game_rules(my_list):
    new_list = [[],[],[]]
    
    result = False  
            
    #Veritcal
    
    for i in my_list:
        for j in range(0,3):
            new_list[j].append(i[j])
    
    for i in new_list:
        if i.count('X') == 3 or i.count('O') ==3 :
            print(f' {i[0]} wins the game ')
            result = True
            
            
    #Horizaontal 
    
    for i in my_list:
        if i.count('X') == 3 or i.count('O') ==3:
            print(f' {i[0]} wins the game ')
            result = True
    #Diagonal
    
    i=0
    j=0
    
    a = my_list
    if(a[i][j]==a[i+1][j+1]==a[i+2][j+2]):
        print(f'Player {a[1][1]} wins the game ')
        result = True
    if(a[i][j+2]==a[i+1][j+1]==a[i+2][j]):
        print(f'Player {a[1][1]} wins the game ')
        result = True
        
    return result


flag_x = user_first()
game_mode = ''
flag1 = flag_x
count = 0 


while game_mode not in ['N'] and count <10:
    
    choice = user_input()
    my_list = cell_modification(my_list, choice, flag1)
    display(my_list)
    flag1 = flagger(flag1)
    
    if game_rules(my_list) == True: 
        print(game_rules(my_list))
        my_list = [[1,2,3],[4,5,6],[7,8,9]]

        game_mode = game_on()
        print('\n'*10)
        count = 0
        
    
    print('\n'*6)
    
    count = count + 1
    if count == 9:
        print('Match tie')
        game_mode = game_on()
        my_list = [[1,2,3],[4,5,6],[7,8,9]]

#Whether he wants to continue 


#final logic 







