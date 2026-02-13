def encrypt(text, key):
    return ''.join(
        chr((ord(char) - 65 + key) % 26 + 65) if char.isupper() else
        chr((ord(char) - 97 + key) % 26 + 97) if char.islower() else
        chr for char in text
    )
    
text = input("Enter The Message : ")
key = int(input("Enter The Shift Value : "))
encrypted = encrypt(text, key)
print(encrypted)

decrypted_text = encrypt(encrypted, -key)
print("Decrypted Text : ", decrypted_text)