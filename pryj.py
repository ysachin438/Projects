import array
def check( key,x, m, n):
    for i in range(9):
        if x[m][i] == key:
            return 0
        if x[i][n]== key:
            return 0
    # case 1: 
    if m<=2 and n<=2:
        for i in range(3):
            for j in range(3):
                if x[i][j]==key:
                    return 0
    # case 2: 
    elif m>2 and m<=5 and n<=2:
        for i in range(3,6):
            for j in range(3):
                if x[i][j]==key:
                    return 0
    # case 3: 
    elif m > 5 and m <= 8 and n <= 2:
        for i in range(6,9):
            for j in range(3):
                if x[i][j]==key:
                    return 0
    # case 4: 
    elif m <= 2 and n > 2 and n <= 5:
        for i in range(3):
            for j in range(3,6):
                if x[i][j]==key:
                    return 0
    # case 5: 
    elif m > 2 and m <= 5 and n > 2 and n <= 5:
        for i in range(3,6):
            for j in range(3,6):
                if x[i][j]==key:
                    return 0
    # case 6: 
    elif m > 5 and m <= 8 and n>2 and n <= 5:
        for i in range(6,9):
            for j in range(3,6):
                if x[i][j]==key:
                    return 0
    # case 7:
    elif m <=2 and n > 5 and n <= 8:
        for i in range(3):
            for j in range(6,9):
                if x[i][j]==key:
                    return 0 
    # case 8:
    elif m > 2 and m <= 5 and n > 5 and n <= 8:
        for i in range(3,6):
            for j in range(6,9):
                if x[i][j]==key:
                    return 0
    elif m> 5 and m<=8 and n>5 and n<=8:
        for i in range(6,9):
            for j in range(6,9):
                if x[i][j]==key:
                    return 0
    return key
# x = [[0]*10]*10
x = [['-',5,2,'-','-',6,'-','-','-'],
     [1,6,'-',9,6,'-','-','-',4],
     ['-',4,9,8,'-',3,6,2,'-'],
     [4,'-','-','-','-','-',8,'-','-'],
     ['-',8,3,2,'-',1,5,9,'-'],
     ['-','-',1,'-','-','-','-','-',2],
     ['-',9,7,3,'-',5,2,4,'-'],
     [2,'-','-','-','-',9,'-',5,6],
     ['-','-','-',1,'-','-',9,7,'-']]
#x = [['-', '-', 0, 0, 0, 0, 0, 0, 0, 0]]
list =[]
count = 1
a=0
while a<10:
    for i in range(9):
        for j in range(9):
            # find blank places in maze
            if x[i][j]=='-':
                for k in range(1,10):
                    # find numbers to be filled at blank spaces and store it in list
                    res = check(k,x,i,j)
                    if res == 0:
                        continue
                    else:
                        x[i][j]=res
                #     else:
                #         list.append(k) #---> storing possible numbers
                # if len(list) == 1:
                #     x[i][j]=res+1
                #     # print(i,j,'-->',list,'\n')
                # else:
                #     list.clear()          
            print(" ",x[i][j]," |",end="")
        print("\n_____|_____|_____|_____|_____|_____|_____|_____|_____|")
    print('\n\n')
    a = a + 1
