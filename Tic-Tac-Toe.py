# This is TIC-TAC-TOE made by spdf.

import time
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def print_matrix(a):
    for m in range(3):
            for n in range(3):
                print(a[m][n], end="")
                if n != 2 :
                    print(" | ", end="")
            print('')

def winner(player1,  player2, a):
    for i in range(3):
            if a[i][0] == a[i][1] and a[i][0] == a[i][2]:
                if a[i][0] == 'X':
                    print('\n', player1, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
                else:
                    print('\n', player2, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
            elif a[0][i] == a[1][i] and a[0][i] == a[2][i]:
                if a[0][i] == 'X':
                    print('\n', player1, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
                else:
                    print('\n', player2, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
            elif a[0][0] == a[1][1] and a[0][0] == a[2][2]:
                if a[0][0] == 'X':
                    print('\n', player1, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
                else:
                    print('\n', player2, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
            elif a[1][1] == a[0][2] and a[1][1] == a[2][0]:
                if a[1][1] == 'X':
                    print('\n', player1, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
                else:
                    print('\n', player2, "is Winner !!\n\n----Thank You For playing----\n")
                    exit()
            else:
                continue
def move_validity(p, temp):
    if p1 in temp:
        print('Invalid Move.')

# Main 
temp = {}
k = 0
print("\n\n----Game Is Loading----\n  ----Please wait----")
time.sleep(1)
for i in range(5,-1,-1):
    print(" - ",i," ",end='')
    time.sleep(1)
print("\n\n    **** WELCOME To TIC-TAC-TOE ****\n")
# Taking Inputs
print('Please Enter Your Names :) ')
player1 = input('Player 1: ')
player2 = input('Player 2: ')

count = 0
while count < 10:

    print_matrix(a)
    print("\n", player1, ': X        ', player2, ": 0\n")
    print(player1, end='')
    p1 = int(input(': '))

    if p1>=1 and p1<=9:
        for i in range(3):
            for j in range(3):
                if a[i][j] == p1:
                    a[i][j] = 'X'

        print_matrix(a)
        count = count+1
        print('\n')
    else:
        print('Enter a valid Choice\n')
    if count >= 3:
        winner(player1, player2, a)

    print(player2,end='')
    p2 = int(input(': '))
    # Check for overwriting
    move_validity(p2,temp)
    
    while p2==p1:
        print('\n\nInvalid Move, Try Again!\n')
        print('\n', player2, end="")
        p2 = int(input(':'))

    if p2 >= 1 and p2 <= 9 :
        for i in range(3):
            for j in range(3):
                if a[i][j] == p2:
                    a[i][j] = '0'

        print_matrix(a)
        count = count + 1
        print("\n")
    else:
        print('Invalid Move\n')
#    Check for Player 2 winning possibilities
    if count >= 3:
        winner(player1, player2, a)