def details ():
    Description = "Encryption"
    Date = "05-10-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
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

text = input("Enter the plain text to be encrypted: ")
encrypted_text = encrypt(text)