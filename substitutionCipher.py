import string
letters = string.ascii_letters
digits= string.digits
dict={}
data=""
secret=5
for i in range(len(letters)):
    dict[letters[i]]= letters[i-secret]

for i in range(len(digits)):
    dict[digits[i]]= digits[i-secret]

print(dict)

with open("./file1.txt") as f:
    while True:
        chr = f.read(1)
        if not chr:
            print("End of file")
            break
        if chr in dict:
            newChr= dict[chr]
            data+=newChr
        else:
            data+=chr

with open("./secret.txt", "w") as f:
    f.write(data)

print("We are Done with Substitution Cipher")
