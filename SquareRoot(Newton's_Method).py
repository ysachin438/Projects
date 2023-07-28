import random
num = int(input('Enter a number to find its square root: '))
list1 = [i for i in range(1,num)]
x = 1
while 0.5*(x+round(num/x,2)) != num:
    x = random.choice(list1)
    while not x in list1 and len(list1)==0:
        x = random.choice(list1)
    list1.remove(x)
print(x)