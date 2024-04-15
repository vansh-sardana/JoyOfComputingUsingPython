def binarySearch(arr, n, s, e):
    if(s>e): return -1

    mid= s+(e-s)//2

    if(arr[mid]==n): return mid
    elif(arr[mid]>n): return binarySearch(arr, n, s, mid-1)
    else: return binarySearch(arr, n, mid+1, e)

arr= [12,14,15,16,18,22,26,67,346,473]
n= int(input("Enter the number you want to search: "))
print(binarySearch(arr, n, 0, len(arr)-1))