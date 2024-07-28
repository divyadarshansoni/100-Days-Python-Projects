def review():
    print("Fuck u")

def quiz():
    score=0
    
    answer=input("Question 1: Who is the current Prime Minister of India: ")
    if answer.lower()=="narendra modi":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    
    answer=input("Question 2: Who is the current President of India: ")
    if answer.lower()=="droupadi murmu":
        print("Correct")
        score+=1
    else:
        print("Incorrect")

    answer=input("Question 3: Who is the current Chief Minister of Rajasthan: ")
    if answer.lower()=="bhajan lal sharma":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    
    answer=input("Question 4: Who is the writer of National Anthem of India: ")
    if answer.lower()=="rabindranath tagore":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    
    answer=input("Question 5: What is the full form of IIT: ")
    if answer.lower()=="indian institute of technology":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    
    answer=input("Question 6: When was IIT Bombay established: ")
    if answer.lower()=="1958":
        print("Correct")
        score+=1
    else:
        print("Incorrect")

    answer=input("Question 7: O3 is commonly known as: ")
    if answer.lower()=="ozone":
        print("Correct")
        score+=1
    else:
        print("Incorrect")

    answer=input("Question 8: Which national team is the current Fifa World Cup winner: ")
    if answer.lower()=="argentina":
        print("Correct")
        score+=1
    else:
        print("Incorrect")

    answer=input("Question 9: Who is GOAT in football: ")
    if answer.lower()=="lionel messi":
        print("Correct")
        score+=1
    else:
        print("Incorrect")
    
    answer=input("Question 10: The guy who sucks Messi's dick is: ")
    if answer.lower()=="cristiano ronaldo":
        print("Correct")
        score+=1
    else:
        print("Incorrect")

    print("Congratulations")
    print("You got",str(score),"questions right")
    print("This is",str(score*10),"percent correct")

    q=input("Do you want to review your answer against correct answers:(Y/N) ")
    if q=="Y":
        review()
    else:
        print("Good Day! See you next time.")