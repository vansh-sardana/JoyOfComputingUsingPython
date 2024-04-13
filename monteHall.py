import random

swap=0
dont_swap=0
n=3
while True:
    doors=[0]*n
    goatDoors= []
    x= random.randrange(n)
    doors[x]= "Tiger"

    for i in range(n):
        if(doors[i]==0):
            goatDoors.append(i)
            doors[i]="Goat"

    choice= int(input("Enter your choice(0 to 2): "))

    door_open= random.randrange(n)
    while(door_open==choice or doors[door_open]=="Tiger"):
        door_open= random.randrange(n)

    print("\nHint: the door ", door_open, "has a goat\n")
    c= int(input("Do you want to change your answer?(0 or 1): "))

    if(c):
        if doors[choice]=="Tiger":
            dont_swap+=1
            print("You lost")
        else:
            swap+=1
            print("You won")

    else:
        if doors[choice]=="Goat":
            dont_swap+=1
            print("You won")
        else:
            swap+=1
            print("You lost")

    c= input("Dou you want to play again(y/n)? ")
    if(c!='y'):
        print("Swap: ", swap)
        print("Dont Swap: ", dont_swap)
        break