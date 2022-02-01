#!/usr/bin/env python3
import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f"\nUser: {user}  Computer: {computer}\n")
    if user == computer:
        return 'Tie\n'
    if is_win(user,computer):
        return 'You won!\n'

    return 'You lost!\n'

def is_win(player1, player2):
    # returns boolean -- returns 1 if player 1 wins and 0 if player 2 wins
    if(player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
        return True
    else:
        return False

print(play())
