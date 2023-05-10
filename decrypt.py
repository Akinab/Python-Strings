def details ():
    Description = "Decryption"
    Date = "05-10-23"
    Plain_Text = "the quick brown fox jumps over the lazy dog."
    print ("\nDescription: {}\nDate: {}\nPlain_Text: {}".format (Description , Date, Plain_Text))
    
details ()

def decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text:
        if char == '*':
            decrypted_text += 'a'
        elif char == '&':
            decrypted_text += 'e'
        elif char == '#':
            decrypted_text += 'i'
        elif char == '+':
            decrypted_text += 'o'
        elif char == '!':
            decrypted_text += 'u'
        else:
            decrypted_text += char
    return decrypted_text
encrypted_text = input("Enter the encrypted text to be decrypted: ")