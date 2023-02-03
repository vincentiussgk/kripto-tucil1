def onetimepad_encrypt(plaintext, key):
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
    

    if (len(plaintextrdy) != len(keyprep)):
        print ("Panjang alfabet kunci tidak sama dengan plaintext!")
    else:
        print(plaintextrdy)
        print(keyprep)

        plain_int = [ord(i) for i in plaintextrdy]
        key_int = [ord(i) for i in keyprep]

        cyphertext = ''
        for i in range (len(plaintextrdy)):
            charvalue = (plain_int[i] + key_int[i]) % 26
            cyphertext = cyphertext + chr(charvalue + 65)

        print("encrypt: ", cyphertext)


onetimepad_encrypt("onetimepad","tbfrgfarfm")

def onetimepad_decrypt(cyphertext, key):
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

    if (len(cyphertextrdy) != len(keyprep)):
        print ("Panjang alfabet kunci tidak sama dengan plaintext!")
    else:
        print(cyphertextrdy)
        print(keyprep)

        cyp_int = [ord(i) for i in cyphertextrdy]
        key_int = [ord(i) for i in keyprep]

        plaintext = ''
        for i in range (len(cyphertextrdy)):
            charvalue = (cyp_int[i] - key_int[i]) % 26
            plaintext = plaintext + chr(charvalue + 65)

        print("decrypt: ", plaintext)

onetimepad_decrypt("HOJKOREGFP","tbfrgfarfm")

