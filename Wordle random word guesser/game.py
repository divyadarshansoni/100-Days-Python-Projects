def game(real_word):
    b=["-","-","-","-","-"]
    count=0
    for n in range(1,11):
        a=input("Your Guess: ")
        count=count+1
        for i in range(0,5):
            if a[i]==real_word[i]:
                b[i]=a[i].lower()
        print(b)
        places_filled=did_win(b)
        if places_filled == 5:
            print("Hurray!\nYou Won.")
            print("You completed the game in",count,"guesses")
            break


def did_win(b):
    z=0
    for i in range(0,5):
        if b[i]!="-":
            z=z+1
    print(z)
    return z
            
