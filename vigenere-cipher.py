def details ():
    Description = "Vigenere Cipher"
    Date = "05-11-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()
def vigenere_cipher(plaintext, keyword):
    key_nums = [ord(c) - 65 for c in keyword]
    ciphertext = []
    for i, c in enumerate(plaintext):
        shift = key_nums[i % len(keyword)]
        ciphertext.append(chr((ord(c) - 65 + shift) % 26 + 65))
    return ''.join(ciphertext)
plaintext = "THISISTHELASTTASKHOORDAY"
keyword = "KNIGHTS"
ciphertext = vigenere_cipher(plaintext, keyword)
statement = "THE CIPHER TEXT IS:"
