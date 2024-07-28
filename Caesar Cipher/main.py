from Encryption import encrypt
from Decryption import decrypt

print("Hello There")

def main():
    a = input("Do you want to encrypt or decrypt[Type e for encryption and d for decryption]: ").lower()

    if a == 'e':
        word = input("Type what you want to encrypt without any spaces: ").lower()
        shift_number = int(input("Type the number by which you want to shift: "))
        encrypted_word = encrypt(word, shift_number)
        print(encrypted_word)
    elif a == 'd':
        word = input("Type what you want to decrypt without any spaces: ").lower()
        shift_number = int(input("Type the number by which it was shifted: "))
        decrypted_word = decrypt(word,shift_number)
        print(decrypted_word)
    
    b = input("Do you want to continue(yes/no): ").lower()
    if b == "yes":
        main()
    elif b == "no":
        print("See You next time")
    else:
        print("your input was not what I expected.\nSo am just going to close the program.")

main()