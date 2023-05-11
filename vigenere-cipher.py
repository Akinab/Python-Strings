def details ():
    Description = "Vigenere Cipher"
    Date = "05-11-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()
def vigenere_cipher(plaintext, keyword):
    key_nums = [ord(c) - 65 for c in keyword]
    ciphertext = []