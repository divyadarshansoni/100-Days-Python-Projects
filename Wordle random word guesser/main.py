from _init import start_game

a = input("Do you want to play the word guessing game:(yes/no) ")

if a.lower()=="yes":
    start_game()
else:
    print("Fine run the code when you want to play.")