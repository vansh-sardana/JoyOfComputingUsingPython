import string
letters = string.ascii_letters
digits= string.digits
dict={}
data=""
secret=5
for i in range(len(letters)):
    dict[letters[i]]= letters[(i+secret)%len(letters)]

for i in range(len(digits)):
    dict[digits[i]]= digits[(i+secret)%len(digits)]

file2= open("./file2.txt", "w")

with open("./secret.txt") as file1:
    while True:
        chr = file1.read(1)
        if not chr:
            break
        if chr in dict:
            chr= dict[chr]
        file2.write(chr)

file2.close()