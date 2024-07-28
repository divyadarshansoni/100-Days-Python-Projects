import random
from functions import places_left, check, p_hangman, did_win, already

answers = ["brake","track","mouth","enjoy","apple",
           "zebra","queue","water","train","prick","speed","forty","grain"]


print("Hello there lets play the game Hangman!")
print('''
    ___________
    |        |
    |        |
    |        O      
    |       /|\\
    |       / \\
    |  
    |
                             ''')
g = input("Do you want to play: (yes/no) ").lower()
if g == "yes":
    print("In this game you will have to guess characters(a-z).\nIf you are able to guess the 5 letter word before the person is hanged you win")
    print("Right now this is the visual")
    print('''
    ___________
    |        
    |        
    |             
    |       
    |       
    |  
    |
                             ''')
    
    guess=["_","_","_","_","_"]

    the_answer = random.choice(answers)

    d = 0
    all = []
    while(d < 7):
        b = input("Guess a character: ").lower()
        if already(all,b) == 0:
            all.append(b)
        else:
            print("Already guessed but you will not lose a life.\nBe careful!")
            continue
        c = check(the_answer,b,guess)
        print(f"There are {places_left(the_answer,guess)} places left")
        if c > 0:
            print(guess)
            p_hangman(d)
        else:
            print("No matches!")
            print(guess)
            d += 1
            p_hangman(d)
            

        z = did_win(the_answer,guess)
        if z == 0:
            print("You win!")
            print("You are a Super Hero!")
            break

else:
    print("Okay then see you later")
