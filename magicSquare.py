'''A magic square is a square matrix of order n where sum of all rows, all columns, and all diagonals are equal and equal to n*(n^2+1)/2
@author Vansh_Sardana
'''

def mSquare(n):
    sq=[]
    for i in range(n):
        r=[]
        for j in range(n):
            r.append(0)
        sq.append(r)

    i=n//2; j=n-1
    cnt=1
    while (cnt<=n*n):
        if(i==-1 and j==n):
            i=0; j=n-2
        elif(i==-1):
            i=n-1
        elif(j==n):
            j=0
        
        if(sq[i][j]!=0):
            j-=2
            i+=1
        else:
            sq[i][j]=cnt
            cnt+=1
            i-=1;j+=1
    
    for row in sq:
        for ele in row:
            print(ele, end=" ")
        print()


mSquare(int(input()))