from scipy import stats
from statistics import mean
from random import randint

arr= [randint(1,100) for _ in range(100)]

#trimmed mean using scipy
print("Trimmed Mean using scipy: ",stats.trim_mean(arr, 0.1))

#normal mean
print("Mean using statistics: ", mean(arr))

#calculating trimmed mean maually
arr.sort()
a= int(0.1*len(arr))
arr= arr[a:]
arr= arr[:len(arr)-a]
print("Trimmed mean manually",mean(arr))