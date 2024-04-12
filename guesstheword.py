import random

words = [
    "Inception", "Interstellar", "Jurassic", "Transformers", "Inglourious", "Terminator", "Prometheus", "Black Panther", "Extraction", "Birdman",
    "Annihilation", "Godzilla", "Whiplash", "ShutterIsland", "Midsommar", "Annabelle", "Zombieland", "Moonlight", "Tombstone", "Unforgiven",
    "Snowpiercer", "Requiem", "Sunshine", "Prisoners", "Unbreakable", "SpiritedAway", "District9", "Cinderella", "Django", "Scream", "Skyfall",
    "Chappie", "Waterworld", "Blowout", "Predators", "Outbreak", "Unstoppable", "Serenity", "Memento", "Hunger", "MoulinRouge", "Moonrise",
    "Casablanca", "Amadeus", "Se7en", "Babel", "Gladiator", "Scarface", "Goodfellas", "Braveheart", "Fargo", "Aliens", "Ratatouille", "Titanic",
    "Gravity", "Warrior", "Seabiscuit", "Rocky", "Superbad", "Snatch", "Prometheus", "Moonlight", "Whiplash", "ShutterIsland", "Midsommar",
    "Annabelle", "Zombieland", "Tombstone", "Unforgiven", "Snowpiercer", "Requiem", "Sunshine", "Prisoners", "Unbreakable", "SpiritedAway",
    "District9", "Cinderella", "Django", "Scream", "Skyfall", "Chappie", "Waterworld", "Blowout", "Predators", "Outbreak", "Unstoppable",
    "Serenity", "Memento", "Hunger", "MoulinRouge", "Moonrise", "Casablanca", "Amadeus", "Se7en", "Babel", "Gladiator", "Scarface", "Goodfellas",
    "Braveheart", "Fargo", "Aliens", "Ratatouille", "Titanic", "Gravity", "Warrior", "Seabiscuit", "Rocky", "Superbad", "Snatch"
]


def chooseWord():
    return random.choice(words)


def randomize(word):
    l = len(word)
    return "".join(random.sample(word, len(word)))


def player(p, picked_word, score):
    print(p + ", it's your turn.")
    ans = input("What word do you think it is?: ")
    if ans.lower() == picked_word.lower():
        score += 1
        print("Congratulations! You guessed correctly. Your score is ", score)
    else:
        print("Oh no! That's not the word. Your score is ", score)
    return score


def play():
    print("Welcome to the game")
    print("Let's play a word guessing game!")
    p1 = input("Player 1, please enter your name: ")
    p2 = input("Player 2, please enter your name: ")
    turn = 0
    score1 = 0
    score2 = 0
    while True:
        turn += 1
        picked_word = chooseWord()
        ques = randomize(picked_word.lower())
        print("Guess the word from: ", ques)
        if turn % 2 == 0:
            score1 = player(p1, picked_word, score1)
        else:
            score2 = player(p2, picked_word, score2)

        c = input("Do you want to continue playing? (yes/no): ")
        if c.lower() != 'yes':
            print("Score of player ", p1, "is ", score1)
            print("Score of player ", p2, "is ", score2)
            if score1 > score2:
                print("Player ", p1, "Wins!")
            elif score1 < score2:
                print("Player ", p2, "Wins!")
            else:
                print("It's a tie!")
            break


play()
