def start_game():
    print("Hello There\nYou fucking know how to play Rock Paper Scissor")
    print("Lets play then")
    game()

def computer_selects():
    import random
    n=random.randint(0,2)
    if n==0:
        return "rock"
    elif n==1:
        return "paper"
    else:
        return "scissor"
    
def who_wins(your,computer):
    if your=="rock" and computer=="scissor":
        print("You win")    
    elif your=="scissor" and computer=="paper":
        print("You win")    
    elif your=="paper" and computer=="rock":
        print("You win")
    else:
        print("computer wins")

def game():
    ans=input("Should we start:(yes/no) ").lower()
    while ans=="yes":

        your_selection=input("Your selection:(Rock/Paper/Scissor) ").lower()

        computer_selection=computer_selects()
        print("Computer selects",computer_selection)

        if your_selection == computer_selection:
            print("Oh it's a tie")
        else:
            who_wins(your_selection,computer_selection)
            

        ans=input("Do you want to continue:(yes/no) ").lower()
    
    print("Goodbye Then!")




