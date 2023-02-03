from textwrap import wrap

def keyprep(key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    keyclean = ''
    keyprep = []
    key = key.upper()
    
    for i in range (len(key)):
        if(key[i].isalpha()) and (key[i] != "J"):
            keyclean += key[i]

    for i in range (len(keyclean)):
        temp = keyclean[i]
        if temp not in keyprep:
            keyprep += temp
    
    for i in range (len(alphabet)):
        temp = alphabet[i]
        if temp not in keyprep:
            keyprep.append(temp)
    print(keyprep)
    return keyprep

def bigram_cleaning(plaintext):
    plaintext = plaintext.upper()
    plaintextrdy = ''
    plaintextclean = ''
    
    for i in range (len(plaintext)):
        if(plaintext[i].isalpha()):
            plaintextrdy += plaintext[i]

    plaintextrdy = plaintextrdy.replace("J","I")

    if(len(plaintextrdy)<2):
        return plaintextrdy

    for i in range (len(plaintextrdy)-1):
        plaintextclean += plaintextrdy[i]
        if plaintextrdy[i] == plaintextrdy[i+1]:
            plaintextclean += 'X'
    
    plaintextclean += plaintextrdy[-1]

    if (len(plaintextclean)%2 == 1):
        plaintextclean += 'X'
    
    print(plaintextclean)
    return plaintextclean    

def bigram(text):
    text = text.upper()
    text_clean1 = ''

    for i in range (len(text)):
        if(text[i].isalpha()):
            text_clean1 += text[i]

    textprep = [text_clean1[i:i + 2] for i in range(0, len(text_clean1), 2)]
    print(textprep)
    return textprep

def playfair_encrypt(plaintext, key):
    keytable = keyprep(key)
    plaintext = bigram_cleaning(plaintext)
    cyphertext = ''

    matrix = [keytable[i:i + 5] for i in range(0, len(keytable), 5)]

    for (i, j) in bigram(plaintext):
        i_temp_x = 0
        i_temp_y = 0
        j_temp_x = 0
        j_temp_y = 0
        current_x = 0
        current_y = 0
        for a in matrix:
            for b in a:
                if (i == b):
                    i_temp_x = current_x
                    i_temp_y = current_y % 5
                current_y += 1
            current_x += 1

        current_x = 0
        current_y = 0
        for a in matrix:
            for b in a:
                if (j == b):
                    j_temp_x = current_x
                    j_temp_y = current_y % 5
                current_y += 1
            current_x += 1

        print(i_temp_x, i_temp_y)
        print(j_temp_x, j_temp_y)
        
        if (i_temp_x == j_temp_x):
            cyphertext += matrix[i_temp_x][(i_temp_y + 1) % 5]
            cyphertext += matrix[j_temp_x][(j_temp_y + 1) % 5]
        elif (i_temp_y == j_temp_y):
            cyphertext += matrix[(i_temp_x + 1) % 5][i_temp_y]
            cyphertext += matrix[(j_temp_x + 1) % 5][j_temp_y]
        else:
            cyphertext += matrix[i_temp_x][j_temp_y]
            cyphertext += matrix[j_temp_x][i_temp_y]

    cyphertextSeparated = wrap(cyphertext, 5)
    return (cyphertext, cyphertextSeparated)

def playfair_decrypt(cyphertext, key):
    keytable = keyprep(key)
    cyphertext = bigram_cleaning(cyphertext)
    plaintext = ''

    matrix = [keytable[i:i + 5] for i in range(0, len(keytable), 5)]

    for (i, j) in bigram(cyphertext):
        i_temp_x = 0
        i_temp_y = 0
        j_temp_x = 0
        j_temp_y = 0
        current_x = 0
        current_y = 0
        for a in matrix:
            for b in a:
                if (i == b):
                    i_temp_x = current_x
                    i_temp_y = current_y % 5
                current_y += 1
            current_x += 1

        current_x = 0
        current_y = 0
        for a in matrix:
            for b in a:
                if (j == b):
                    j_temp_x = current_x
                    j_temp_y = current_y % 5
                current_y += 1
            current_x += 1

        print(i_temp_x, i_temp_y)
        print(j_temp_x, j_temp_y)

        if (i_temp_x == j_temp_x):
            plaintext += matrix[i_temp_x][(i_temp_y - 1) % 5]
            plaintext += matrix[j_temp_x][(j_temp_y - 1) % 5]
        elif (i_temp_y == j_temp_y):
            plaintext += matrix[(i_temp_x - 1) % 5][i_temp_y]
            plaintext += matrix[(j_temp_x - 1) % 5][j_temp_y]
        else:
            plaintext += matrix[i_temp_x][j_temp_y]
            plaintext += matrix[j_temp_x][i_temp_y]

    plaintextclean = ''
    for i in range (len(plaintext)):
        if(plaintext[i] != "X"):
            plaintextclean += plaintext[i]
    
    plaintextcleanSeparated = wrap(plaintext, 5)
    return (plaintext, plaintextcleanSeparated)

playfair_encrypt("temui ibu nanti malam", "JALAN GANESHA SEPULUH")

playfair_decrypt("ZBRSFYKUPGLGRKVSNLQV", "JALAN GANESHA SEPULUH")
