import string

def atbash_encode(text):
    """
    Koduje tekst z użyciem szyfru Atbash.
    """
    plain = string.ascii_lowercase
    cipher = plain[::-1]
    trans = str.maketrans(plain, cipher)
    return text.lower().translate(trans)

def atbash_decode(ciphertext):
    """
    Dekoduje tekst z użyciem szyfru Atbash.
    """
    plain = string.ascii_lowercase
    cipher = plain[::-1]
    trans = str.maketrans(cipher, plain)
    return ciphertext.lower().translate(trans)

# Przykładowe użycie:

text = str(input('Wprowadź tekst: '))
cipher = atbash_encode(text)
print('Zaszyfrowane: '+str(atbash_encode(text))) # zwyzy nz prgz
plain = atbash_decode(cipher)
print('Deszyfrowane: '+str(atbash_decode(cipher))) # ala ma kota
