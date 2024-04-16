import turtle, random
turtle.bgcolor("black")
t1= turtle.Turtle()
t1.setpos(-250,250)
t1.shape("turtle")
t1.color("black")
t1.penup()
i=0;j=0;k=0;d=20;e=0
turtle.colormode(255)
def move():
    global i,j,k,d
    if(i<=255-d):
        if(k<=255-d):
            k+=d
        elif(j<=255-d):
            j+=d
        else:
            i+=d
    else:
        i-=d;k=0;j=0
    t1.color((i,j,k))
    t1.forward(25)
    t1.dot()

def spiral(r, c):
    rs=0; cs=0; re=r-1; ce=c-1
    global colors
    while(rs<=re and cs<=ce):
        i=rs;j=cs
        while(j<=ce):
            move()
            j+=1
        rs+=1
        t1.right(90)
        j=ce; i=rs
        while(i<=re):
            move()            
            i+=1
        ce-=1

        i=re;j=ce
        t1.right(90)
        while(j>=cs):
            move()
            j-=1   
        re-=1
        t1.right(90)

        i=re;j=cs
        while(i>=rs):
            move()
            i-=1
        cs+=1
        t1.right(90)
spiral(20,20)



input()