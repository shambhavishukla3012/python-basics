import random

''' 1 : stone    2 : paper    3 : scissor '''
l=[1,2,3]
q = random.choice(l)                             # computer

while True:
    print("\n1: STONE \n2: PAPER \n3: SCISSOR ")
    a=int(input("ENTER YOUR CHOICE --> "))       # player

    print("\nRESULT :-")
    if(q==1 ):
        if(a==2):
            print('PLAYER WINS')
    if(q==3 ):
        if(a==1):
            print('PLAYER WINS')
    if(q==2 ):
        if(a==3):
            print('PLAYER WINS')

    if(q==1 ):
        if(a==3):
            print('COMPUTER WINS')
    if(q==2 ):
        if(a==1):
            print('COMPUTER WINS')
    if(q==3 ):
        if(a==2):
            print('COMPUTER WINS')
    if(q==a):
        print('TIE')


    b=input("\nWANNA PLAY AGAIN: \n1.'y' for YES \n2.'n' for NO\n -->")
    if(b=='y'):
        continue
    else:
        print("\nGAME OVER ")
        break
