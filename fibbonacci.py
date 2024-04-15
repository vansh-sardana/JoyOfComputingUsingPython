def fibbo(n):
    if(n<=1): return n
    return fibbo(n-1)+fibbo(n-2)

n= int(input("Enter the number: "))
print(fibbo(n))