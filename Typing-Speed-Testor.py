#This is typing speed tester.
import random as p
import time as t
#to find mistakes during typing
def mistake(text1, usertext1):
    text = text1.split()
    usertext = usertext1.split()
    error = 0
    for match_word in range(len(text)):
        try:
            if text[match_word]!= usertext[match_word]:
                error = error + 1
        except:
            error = error + 1
    return error

#to calculate typing speed
def speed(st,et,usertext):
    timetaken = et - st
    ts = len(usertext)/timetaken
    return  round(ts ,2)

#User choices and inputs
file = open('M:\MyGit\Textfile.txt', 'r')
text1 = (file.read()).split(".")
while True:
    print("------TYPING SPEED TESTOR------")
    choic = input('\n Are You Ready (y/n): ')
    if choic == 'y':
        st = t.time()
        text = p.choice(text1)
        print(text)
        usertxt = input("Enter Text: ")
        et = t.time()
        print('Your typing speed: ',speed(st,et,usertxt))
        print('Total Mistakes : ',mistake(text,usertxt))
        break
    elif choic == 'n':
        print("\n---Thank You---\n\nYou can exit now.\n\n")
        break
    else:
        print('Invalid Choice.')

