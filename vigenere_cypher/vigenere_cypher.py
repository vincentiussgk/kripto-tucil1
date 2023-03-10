from textwrap import wrap

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()

    plaintextrdy = ''

    for i in range (len(plaintext)):
        if(plaintext[i].isalpha()):
            plaintextrdy += plaintext[i]

    key = key.upper()
    keyprep = ''

    for i in range (len(key)):
        if(key[i].isalpha()):
            keyprep += key[i]
    
    keyrdy = ''
    for i in range (len(plaintextrdy)):
        keyrdy += keyprep[i % len(keyprep)]

    plain_int = [ord(i) for i in plaintextrdy]
    key_int = [ord(i) for i in keyrdy]

    cyphertext = ''
    for i in range (len(plaintextrdy)):
        charvalue = (plain_int[i] + key_int[i]) % 26
        cyphertext = cyphertext + chr(charvalue + 65)

    cyphertextSeparated = wrap(cyphertext, 5)
    return (cyphertext, cyphertextSeparated)

def vigenere_decrypt(cyphertext, key):
    cyphertext = cyphertext.upper()

    cyphertextrdy = ''

    for i in range (len(cyphertext)):
        if(cyphertext[i].isalpha()):
            cyphertextrdy += cyphertext[i]

    key = key.upper()
    keyprep = ''

    for i in range (len(key)):
        if(key[i].isalpha()):
            keyprep += key[i]
    
    keyrdy = ''
    for i in range (len(cyphertextrdy)):
        keyrdy += keyprep[i % len(keyprep)]

    cyp_int = [ord(i) for i in cyphertextrdy]
    key_int = [ord(i) for i in keyrdy]

    plaintext = ''
    for i in range (len(cyphertextrdy)):
        charvalue = (cyp_int[i] - key_int[i]) % 26
        plaintext = plaintext + chr(charvalue + 65)

    plaintextSeparated = wrap(plaintext, 5)
    return (plaintext, plaintextSeparated)

