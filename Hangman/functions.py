def places_left(word,guess):
    places_left = 5
    for i in range(0,5):
        if guess[i] == word[i]:
            places_left -= 1
    return places_left

def check(word,b,guess):
    a = 0
    for i in range(0,5):
        if b == word[i]:
            guess[i] = word[i]
            a +=1
    return a

def p_hangman(a):
    if a == 0:
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
    elif a == 1:
        print('''
    ___________
    |        |
    |        |
    |              
    |       
    |       
    |  
    |
                             ''')
    elif a == 2:
        print('''
    ___________
    |        |
    |        |
    |        O      
    |       
    |       
    |  
    |
                             ''')
    elif a == 3:
        print('''
    ___________
    |        |
    |        |
    |        O      
    |       /
    |       
    |  
    |
                             ''')
    elif a == 4:
        print('''
    ___________
    |        |
    |        |
    |        O      
    |       /|
    |       
    |  
    |
                             ''')
    elif a == 5:
        print('''
    ___________
    |        |
    |        |
    |        O      
    |       /|\\
    |       
    |  
    |
                             ''')
    elif a == 6:
        print('''
    ___________
    |        |
    |        |
    |        O      
    |       /|\\
    |       / 
    |  
    |
                             ''')
    else:
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
        print("Game Over")
        print("Better luck next time")
        
def did_win(word,guess):
    z = 0
    for i in range(0,5):
        if word[i] != guess[i]:
            z = 1
    return z

def already(word,b):
    for i in word:
        if b == i:
            return 1
    return 0    