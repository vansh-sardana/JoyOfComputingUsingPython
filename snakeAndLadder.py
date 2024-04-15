from PIL import Image
import random

end=100

turn = 0
s1=0
s2=0

def show_board():
    img= Image.open("./snakeladder.png")
    img.show()

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
    global turn, s1, s2, end
    p1 = input("Player 1, please enter your name: ")
    p2 = input("Player 2, please enter your name: ")
    while True:
        if(turn%2==0):
            print(f"{p1}, It's your turn ")
            c=int(input("Press 1 to play and any other key to quit: "))
            if not c==1:
                print(f"{p1} score: {s1}")
                print(f"{p2} score: {s2}")
                return
            dice= random.randint(1,6)
            print(f"The dice got a {dice}")
            s1+=dice
            s1= check_ladder(s1)
            s1= check_snake(s1)
            if(s1>end):
                s1=end
            print(f"Your score {s1}\n")
            if(s1==end):
                print(f"{p1}, You won!!!!!")
                return
        else:
            print(f"{p2}, It's your turn ")
            c=int(input("Press 1 to play and any other key to quit: "))
            if not c==1:
                print(f"{p1} score: {s1}")
                print(f"{p2} score: {s2}")
                break
            dice= random.randint(1,6)
            print(f"The dice got a {dice}")
            s2+=dice
            s2= check_ladder(s2)
            s2= check_snake(s2)
            if(s2>end):
                s2=end
            print(f"Your score {s2}\n")
            if(s2==end):
                print(f"{p2}, You won!!!!!")
                return
        turn+=1
show_board()
play()