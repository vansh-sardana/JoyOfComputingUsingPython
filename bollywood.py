import random
import os

bollywood_movies = [
    "Sholay",
    "Dilwale Dulhania Le Jayenge",
    "Lagaan",
    "3 Idiots",
    "Mughal-E-Azam",
    "Mother India",
    "Pyaasa",
    "Shree 420",
    "Mera Naam Joker",
    "Andaz Apna Apna",
    "Padosan",
    "Anand",
    "Amar Akbar Anthony",
    "Deewaar",
    "Don",
    "Gol Maal",
    "Chupke Chupke",
    "Mera Gaon Mera Desh",
    "Aradhana",
    "Bobby",
    "Sholay",
    "Gadar: Ek Prem Katha",
    "Kabhie Kabhie",
    "Masoom",
    "Mr. India",
    "Chupke Chupke",
    "Ganga Jamuna",
    "Dil Se..",
    "Dil Chahta Hai",
    "Dil To Pagal Hai",
    "Devdas",
    "Hum Dil De Chuke Sanam",
    "Kal Ho Naa Ho",
    "Kuch Kuch Hota Hai",
    "Kabhi Khushi Kabhie Gham...",
    "Lagaan",
    "Devdas",
    "Koi... Mil Gaya",
    "Kaho Naa... Pyaar Hai",
    "Mohabbatein",
    "Kabhi Alvida Naa Kehna",
    "Jab We Met",
    "Veer-Zaara",
    "Krrish",
    "Om Shanti Om",
    "Main Hoon Na",
    "Ghajini",
    "3 Idiots",
    "PK",
    "Bajrangi Bhaijaan",
    "Dangal",
    "Sultan",
    "Baahubali: The Beginning",
    "Baahubali 2: The Conclusion",
    "Chak De! India",
    "Singham",
    "Raazi",
    "Uri: The Surgical Strike",
    "Gully Boy",
    "Dil Dhadakne Do",
    "Zindagi Na Milegi Dobara",
    "Barfi!",
    "Bhaag Milkha Bhaag",
    "Queen",
    "Padmaavat",
    "Pad Man",
    "M.S. Dhoni: The Untold Story",
    "Mary Kom",
    "Bajirao Mastani",
    "Ra.One",
    "Fan",
    "Jodhaa Akbar",
    "My Name Is Khan",
    "Bhool Bhulaiyaa",
    "Golmaal: Fun Unlimited",
    "Dhamaal",
    "Welcome",
    "No Entry",
    "Singh Is Kinng",
    "Chennai Express",
    "Golmaal Returns",
    "Golmaal 3",
    "Housefull",
    "Housefull 2",
    "Housefull 3",
    "Total Dhamaal",
    "Simmba",
    "Zero",
    "War",
    "Sooryavanshi",
    "Bunty Aur Babli 2",
    "Laal Singh Chaddha",
    "83",
    "Radhe",
    "Shershaah",
    "Jersey",
    "Ludo",
    "Sadak 2",
    "Thalaivi",
    "Gangubai Kathiawadi",
    "Prithviraj",
    "Brahmastra",
    "Atrangi Re",
    "Heropanti 2",
    "Pathan",
    "Rashmi Rocket",
    "KGF: Chapter 2",
    "RRR"
]

def chooseMovie():
    return random.choice(bollywood_movies)


def turnSecret(word):
    cnt=0
    vowels= ['a','e','i','o','u']
    temp=""
    for i in word:
        if(not('a'<=i<='z') or i in vowels or i==" "):
            temp+=i
        else:
            temp+="*"
            cnt+=1
    return [temp,cnt]

def check(ch, word):
    for i in word:
        if(i==ch):
            return 1
    return 0

def putAns2ques(ques, picked_movie, ch, cnt):
    temp= ""
    for i in range(len(picked_movie)):
        if(ques[i]=="*"):
            if(picked_movie[i]==ch):
                cnt-=1
                temp+=ch
            else:
                temp+="*"
        else:
            temp+=ques[i]
    return [temp,cnt]

def player( picked_movie, ques, life, cnt):
    print(ques)
    ans = input("Guess a character: ")
    ch= ans[0].lower()
    
    if(check(ch, picked_movie)):
        print("Congratulations! You guessed correctly. ")
        [ques, cnt]= putAns2ques(ques, picked_movie, ch,cnt)
    else:
        life= life[1:]
        print("Oh no! That's not the correct letter. ")
    return [ques, life, cnt]


def play():
    print("Welcome to the game")
    print("Let's play a word guessing game!")
    p1 = input("Player, please enter your name: ")
    score = 0
    totalPlay=0
    while True:
        try:
            clear_terminal()
            totalPlay+=1
            life= 'BOLLYWOOD'
            picked_movie = chooseMovie().lower()
            [ques,cnt] = turnSecret(picked_movie)
            print("Guess the word from: ")
            while(1):
                print("LIFE: ", life)
                [ques,life,cnt] = player(picked_movie, ques, life, cnt)
                if(cnt<=0):
                    print("You Won")
                    print("The movie was ", ques)
                    break
                if (not len(life)):
                    print("You Lost")
                    print("The Movie was ", picked_movie)
                    break
            c= int(input("Do you want to play again? (0/1): "))
            if(not c):
                break
        except:
            print("error")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_terminal()


play()
