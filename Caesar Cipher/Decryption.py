def decrypt(word,shift_number):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decipher_text = ""
    for letter in word:
        if letter in alphabet:
            x = alphabet.index(letter)
            x -= shift_number
            
            while x > 25 or x < 0:
                if x > 25:
                    x -= 26
                elif x < 0:
                    x += 26
            
            decipher_text += alphabet[x]
        else:
            decipher_text += letter

    return decipher_text