def median(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)
    if(n%2==0):
        return (arr[n//2-1]+arr[n//2])/2
    else:
        return arr[(n)//2]

arr= input("Enter the list: ")
arr= arr.replace("[", "").replace("]", "").replace(" ","")
arr= arr.split(",")
for i in range(len(arr)):
    arr[i]= int(arr[i])
print(median(arr))