def details ():
    Description = "Encryption"
    Date = "05-10-23"
    Plain_Text = "the quick brown fox jumps over the lazy dog."
    print ("\nDescription: {}\nDate: {}\nPlain_Text: {}".format (Description , Date, Plain_Text))
    
details ()

def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char == 'a':
            encrypted_text += '*'
        elif char == 'e':
            encrypted_text += '&'
        elif char == 'i':
            encrypted_text += '#'
        elif char == 'o':
            encrypted_text += '+'
        elif char == 'u':
            encrypted_text += '!'
        else:
            encrypted_text += char
    return encrypted_text

text = input("Copy and Paste the plain text to be encrypted: ")
encrypted_text = encrypt(text)
print("Encrypted Text:", encrypted_text)