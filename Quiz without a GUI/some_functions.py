from quiz import quiz

def _init(init):
    if init=="Y":
        quiz_rules()
    elif init=="N":
        print("You are a dumb and lazy ASSHOLE!")
        print("\nThink Again!\nRun the code when you are up for the quiz")
    else:
        print("\nWarning!\nSucker you have to answer in \"Y\" or \"N\" only. Try again correctly!\n")
        init=input("Do you wanna test your knowledge with this Quiz? (Y/N):")
        _init(init)

def quiz_rules():
    print("Introduction!\nThis is your General Knowledge Quiz.\nThere are a total of 10 questions.\nEach question has 1 point assigned to it.\nSo the maximum score you can get is 10.")
    print("Type all your answers with correct spelling or you will not get the marks.\nAll The Best!")
    quiz()
