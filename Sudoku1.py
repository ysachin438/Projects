import numpy
global x
x = [[0,5,2,0,0,6,0,0,0],
     [1,6,0,9,6,0,0,0,4],
     [0,4,9,8,0,3,6,2,0],
     [4,0,0,0,0,0,8,0,0],
     [0,8,3,2,0,1,5,9,0],
     [0,0,1,0,0,0,0,0,2],
     [0,9,7,3,0,5,2,4,0],
     [2,0,0,0,0,9,0,5,6],
     [0,0,0,1,0,0,9,7,0]]
def check(num,m,n):
    global x
    for i in range(9):
        if x[m][i]==num:
            return False
        if x[i][n]==num:
            return False
    p = (m//3)*3
    q=(n//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if x[p+i][q+i]==num:
                return False
    return True
def sudoku():
    global x
    for i in range(9):
        for j in range(9):
            if x[i][j]==0:
                for k in range(1,10):
                    if check(k,i,j)==True:
                        x[i][j]=k
                        sudoku()
                        x[i][j]=0
    print(numpy.matrix(x))
    input("ENter")
    
