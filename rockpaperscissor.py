import random
options= ["rock", "paper","scissors"]
op1= (random.sample(options,3))
op2= (random.sample(options,3))

def play():
    s1=0;s2=0
    while True:
        p1= int(input("Player 1, Enter your choice (0/1/2)"))
        p2= int(input("Player 2, Enter your choice (0/1/2)"))
        print("Player 1: ",op1)
        print("Player 2: ",op2)

        print("Player 1 chose", op1[p1])
        print("Player 2 chose", op2[p2])
        if(op1[p1]==op2[p2]):
            print("Its a draw")
        elif(op1[p1]=='rock' and op2[p2]=='scissors') or (op1[p1]=='paper' and op2[p2]=='rock') or (op1[p1]=='scissors' and op2[p2]=='paper'):
            print("Player 1 wins!")
            s1+=1
        else:
            print("Player 2 wins!")
            s2+=1
        print("Score of player 1: ",s1)
        print("Score of player 2: ",s2)
        
        c=input("Do you want to play again?(y/n) :")
        if(c.lower()!='y'):
            break


play()