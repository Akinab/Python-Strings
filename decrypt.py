def details ():
    Description = "Decryption"
    Date = "05-10-23"
    Plain_Text = "the quick brown fox jumps over the lazy dog."
    print ("\nDescription: {}\nDate: {}\nPlain_Text: {}".format (Description , Date, Plain_Text))
    
details ()

def decrypt(encrypted_text):
    decrypted_text = ""
    for char in encrypted_text: