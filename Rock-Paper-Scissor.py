import random
# Winner Logic
def winner(x, y):
    print('\nYour Choice: ',x,"        Computer Choice: ",y)
    if x == y:
        print("\nIts Draw.\n")
    elif x == 'Rock' and y == 'Scissor':
        print("\nYou Win!.\n")
    elif y == 'Rock' and x == 'Scissor':
        print('\nComputer Wins.\n')
    elif x == "Paper" and y == "Rock":
        print('\n---You Win---\n')
    elif y == "Paper" and x == 'Rock':
        print('\n---Computer Win---\n')
    elif x == 'Scissor' and y == 'Paper':
        print('\n---You win---\n')
    elif y == 'Scissor' and x == 'Paper':
        print('\n---Computer Win---\n')
    else:
        print('Invalid Choice.')

#final calls     
print("----Rock-Paper-Scissor----")
options = ['Rock', 'Paper', 'Scissor']
while True: 
    print('\n')
    for i in range(len(options)):
        print(i+1,". ",options[i])
    userchoice = int(input("Enter your choice: "))
    if userchoice >= 1 or userchoice <=3:
# Computer Choice
        cchoice = random.choice(options)
# check for winner
        winner(options[userchoice-1], cchoice)
# Check logic to play again
        replay_choice = input('\n\nPRESS 0 to Play Again and any key to exit. ')
        if replay_choice!= '0':
            print('Exit Successful.\n---Thank You---')
            break
    else:
        print('Invalid Choice.')