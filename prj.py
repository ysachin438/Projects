import numpy 
global x
x = [[0,4,0,0,0,7,6,0,0],
     [8,0,6,0,4,0,0,3,0],
     [0,2,7,0,0,0,0,0,8],
     [0,0,0,4,8,0,0,0,3],
     [0,9,0,7,0,6,0,4,0],
     [2,0,0,0,1,3,0,0,0],
     [4,0,0,0,0,0,8,1,0],
     [0,5,0,0,3,0,2,0,4],
     [0,0,1,5,0,0,0,6,0]]

def check(key, m, n):
    global x
    for p in range(9):
        if x[m][p] == key:
            return False
    for q in range(9):
        if x[q][n]== key:
            return False
        # # case 1: 
    # if m<3 and n<3:
    #     for i in range(0,3):
    #         for j in range(0,3):
    #             if x[i][j]==key:
    #                 print(i,j,'--->',key)
    #                 return False
    # # case 2: 
    # elif m>2 and m<6 and n<3:
    #     for i in range(3,6):
    #         for j in range(0,3):
    #             if x[i][j]==key:
    #                 return False
    # # case 3: 
    # elif m > 5 and n < 3:
    #     for i in range(6,9):
    #         for j in range(0,3):
    #             if x[i][j]==key:
    #                 return False
    # # case 4: 
    # elif m <3 and n > 2 and n < 6:
    #     for i in range(0,3):
    #         for j in range(3,6):
    #             if x[i][j]==key:
    #                 return False
    # # case 5: 
    # elif m > 2 and m <6 and n > 2 and n <6:
    #     for i in range(3,6):
    #         for j in range(3,6):
    #             if x[i][j]==key:
    #                 return False
    # # case 6: 
    # elif m > 5 and m < 9 and n>2 and n < 6:
    #     for i in range(6,9):
    #         for j in range(3,6):
    #             if x[i][j]==key:
    #                 return False
    # # case 7:
    # elif m <3 and n > 5 and n < 9:
    #     for i in range(0,3):
    #         for j in range(6,9):
    #             if x[i][j]==key:
    #                 return False 
    # # case 8:
    # elif m > 2 and m < 6 and n > 6 and n < 9:
    #     for i in range(3,6):
    #         for j in range(6,9):
    #             if x[i][j]==key:
    #                 return False
    # # Case 9:
    # elif m> 5 and m<9 and n>5 and n<9:
    #     for i in range(6,9):
    #         for j in range(6,9):
    #             if x[i][j]==key:
    #                 return False
    xc = (m//3)*3
    yc =(n//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if x[xc + i][yc + j]==key:
                return False
    return True

def sudoku():
    global x
    for i in range(9):
        for j in range(9):
            if x[i][j] == 0:
                for n in range(1,10):
                    if check(n,i,j):
                        x[i][j] = n
                        sudoku()
                        x[i][j]=0
                return
    for i in range(9):
        for j in range(9):
                print(" ",x[i][j],end="")
                if (j+1)%3==0:
                    print(" |",end='')
        if (i+1)%3==0:
            print('\n--------------------------------') 
        print()
        # print("\n_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    s=input('''
          Press 1 : To find another solution
          Press Any key to exit : ''')
    if s!='1':
        print('          Exit Successful.....')
        exit()
   
print('Sudoku Solver')        
sudoku()
