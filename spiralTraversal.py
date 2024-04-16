import numpy

def spiral(arr, r, c):
    rs=0; cs=0; re=r-1; ce=c-1

    while(rs<=re and cs<=ce):
        i=rs;j=cs
        while(j<=ce):
            print(arr[i][j], end=" ")
            j+=1
        rs+=1
        
        j=ce; i=rs
        while(i<=re):
            print(arr[i][j], end=" ")
            i+=1
        ce-=1

        i=re;j=ce
        while(j>=cs):
            print(arr[i][j], end=" ")
            j-=1   
        re-=1

        i=re;j=cs
        while(i>=rs):
            print(arr[i][j], end=" ")
            i-=1
        cs+=1


cnt=0
arr= []
for i in range(5):
    arr.append([])
    for j in range(5):
        arr[i].append(cnt)
        cnt+=1
print(numpy.matrix(arr))
spiral(arr, 5,5)