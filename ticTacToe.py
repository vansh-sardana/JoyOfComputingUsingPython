import numpy

board=numpy.array([["-","-","-"],["-","-","-"],["-","-","-"]])
turn = 0
sym1 = 'X'
sym2= '0'

def rows(symbol):
    for i in range(3):
        count=0
        for j in range(3):
            if(board[i][j]==symbol):
                count+=1
        if(count==3):
            return 1
    return 0

def cols(symbol):
    for j in range(3):
        count=0
        for i in range(3):
            if(board[i][j]==symbol):
                count+=1
        if(count==3):
            return 1
    return 0

def diag(symbol):
    i=0;j=0
    while(i<3 and j<3):
        if(board[i][j]!=symbol):
            return 0
        i+=1;j+=1
    i=2;j=2
    while(i>=0 and j>=0):
        if(board[i][j]!=symbol):
            return 0
        i-=1;j-=1
    return 1

def won(symbol):
    return rows(symbol) or cols(symbol) or diag(symbol)

def isSafe(r,c):
    if board[r][c]!="-":
        return False
    return True

def place(symbol):
    print(numpy.matrix(board))
    while True:
        r= int(input("Enter the row: (0,1,2): "))
        c= int(input("Enter the column: (0,1,2): "))
        if r>=0 and r<4 and c>=0 and c<4 and isSafe(r,c):
            board[r][c]=symbol
            break
        else:
            print("Invalid row or column entered")


def play(turn):
    try:
        for i in range(9):
            if(turn%2==0):
                symbol=sym1
            else:
                symbol=sym2
            print(f"\n{symbol}'s turn")
            place(symbol)
            
            if(won(symbol)):
                print(f'{symbol} won')
                return 1
            turn+=1

        print("\nIts a draw")
        
    except:
        print("Something Went Wrong")
        

play(turn)