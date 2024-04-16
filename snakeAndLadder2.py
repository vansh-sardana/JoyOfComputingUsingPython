import random
import turtle

turtle.bgpic("./snakeladder.png")
turtle.bgcolor("black")
s= -305+30.5
e= 305-30.5
w= 61

pMark1= turtle.Turtle()
pMark1.penup()
pMark1.color("red")
pMark1.shapesize(stretch_wid=3, stretch_len=3, outline=10) 
pMark1.setpos(s, s)
pMark2= turtle.Turtle()
pMark2.penup()
pMark2.pensize(8)
pMark2.color("blue")
pMark2.shapesize(stretch_wid=2.5, stretch_len=2.5, outline=10) 
pMark2.setpos(s,s)

end=100

turn = 0
score1=0
score2=0

def move1():
    global score1, s, pMark1
    if score1//10%2==1 and score1%10!=0:
        pMark1.setpos(e-(score1%10-1)*61, s+(score1//10)*61)
    elif score1//10%2==0 and score1%10!=0:
        pMark1.setpos(s+(score1%10-1)*61,s+((score1//10)*61))
    elif score1//10%2==1 and score1%10==0:
        pMark1.setpos(e, s+(score1//10-1)*61)
    else:
        pMark1.setpos(e-9*61, s+(score1//10-1)*61)

def move2():
    global score2, s, pMark2
    if score2//10%2==1 and score2%10!=0:
        pMark2.setpos(e-(score2%10-1)*61, s+(score2//10)*61)
    elif score2//10%2==0 and score2%10!=0:
        pMark2.setpos(s+(score2%10-1)*61,s+((score2//10)*61))
    elif score2//10%2==1 and score2%10==0:
        pMark2.setpos(e, s+(score2//10-1)*61)
    else:
        pMark2.setpos(e-9*61, s+(score2//10-1)*61)

def check_ladder(points): 
    match points:
        case 4:
            print("You made it to a ladder.")
            return 25
        case 13:
            print("You made it to a ladder.")
            return 46
        case 33:
            print("You made it to a ladder.")
            return 49
        case 42:
            print("You made it to a ladder.")
            return 63
        case 50:
            print("You made it to a ladder.")
            return 69
        case 62:
            print("You made it to a ladder.")
            return 81
        case 74:
            print("You made it to a ladder.")
            return 92
        case _:
            return points

def check_snake(points):
    match points:
        case 99:
            print("You hit a snake")
            return 41
        case 89:
            print("You hit a snake")
            return 53
        case 76:
            print("You hit a snake")
            return 58
        case 66:
            print("You hit a snake")
            return 45
        case 54:
            print("You hit a snake")
            return 31
        case 43:
            print("You hit a snake")
            return 18
        case 40:
            print("You hit a snake")
            return 3
        case 27:
            print("You hit a snake")
            return 5
        case _:
            return points

def play():
    print("Welcome to the Snake and Ladder")
    global turn, score1, score2, end
    p1 = input("Player 1, please enter your name: ")
    p2 = input("Player 2, please enter your name: ")
    while True:
        if(turn%2==0):
            print(f"{p1}, It's your turn ")
            c=int(input("Press 1 to play and any other key to quit: "))
            if not c==1:
                print(f"{p1} score: {score1}")
                print(f"{p2} score: {score2}")
                return
            dice= random.randint(1,6)
            print(f"The dice got a {dice}")
            score1+=dice
            move1()
            score1= check_ladder(score1)
            move1()
            score1= check_snake(score1)
            move1()
            if(score1>end):
                score1=end
            print(f"Your score {score1}\n")
            if(score1==end):
                print(f"{p1}, You won!!!!!")
                return
        else:
            print(f"{p2}, It's your turn ")
            c=int(input("Press 1 to play and any other key to quit: "))
            if not c==1:
                print(f"{p1} score: {score1}")
                print(f"{p2} score: {score2}")
                break
            dice= random.randint(1,6)
            print(f"The dice got a {dice}")
            score2+=dice
            move2()
            score2= check_ladder(score2)
            move2()
            score2= check_snake(score2)
            move2()
            if(score2>end):
                score2=end
            print(f"Your score {score2}\n")
            if(score2==end):
                print(f"{p2}, You won!!!!!")
                return
        turn+=1

play()

turtle.Screen().exitonclick()