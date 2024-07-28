from functions import play_game

print("Hello There! This is the Bidding Game.")
ans = input("Do you want to play the bidding game(yes/no): ").lower()
if ans == "yes":
    play_game()
else:
    print("Fine see you next time")
