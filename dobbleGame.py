'''
Here we have to generate two lists with only one same symbol
@author - Vansh Sardana
'''
import string, random

def generateLists(n):
    l1=[0]*n
    l2=[0]*n
    u= list(string.ascii_letters)
    sameL= random.choice(u)
    u.remove(sameL)
    pos1= random.randrange(n)
    pos2= random.randrange(n)
    l1[pos1]=sameL
    l2[pos2]=sameL
    if(pos1!=pos2):
        l1[pos2]= random.choice(u)
        u.remove(l1[pos2])
        l2[pos1]= random.choice(u)
        u.remove(l2[pos1])
    for i in range(n):
        if(i!=pos1 and i!=pos2):
            l1[i]=random.choice(u)
            u.remove(l1[i])
            l2[i]=random.choice(u)
            u.remove(l2[i])
    
    print(l1)
    print(l2)


generateLists(int(input("Enter the length of sequence(Max len= 26)")))