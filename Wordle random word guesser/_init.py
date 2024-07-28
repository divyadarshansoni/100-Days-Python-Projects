def random_word():
    import random
    list = ["track","beard","sixty","enjoy","dirty","birth","death","brake","mouth","sound","grasp","guess","shift","slice","bread","apple","fruit","teeth"]
    n = random.choice(list)
    return n

def start_game():
    from game import game
    print("Hello There!\nThese are the rules.\nThere is a system generated 5 letter word.")
    print("You will have to guess that word.\nIf the real word and your guess is same you win.")
    print("But if not then all the common letters will be highlighted if any.\nYou will get 10 guesses.")
    print("Also type 5 letter guesses only")
    print("All the Best")
    print("Alright type your first guess")
    real_word = random_word()
    game(real_word)