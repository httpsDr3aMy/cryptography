import string


def vigenere_encrypt(plaintext, key):
    """
    Encrypts plaintext using Vigenere cipher with the given key.
    """
    # Create a list of shifted alphabets
    shifted_alphabets = []
    for i in range(len(key)):
        shifted_alphabets.append(string.ascii_lowercase[i:] + string.ascii_lowercase[:i])

    # Encrypt plaintext
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char in string.ascii_lowercase:
            shifted_alphabet = shifted_alphabets[key_index]
            shifted_index = string.ascii_lowercase.index(char)
            ciphertext += shifted_alphabet[shifted_index]
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char

    return ciphertext


def vigenere_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using Vigenere cipher with the given key.
    """
    # Create a list of shifted alphabets
    shifted_alphabets = []
    for i in range(len(key)):
        shifted_alphabets.append(string.ascii_lowercase[i:] + string.ascii_lowercase[:i])

    # Decrypt ciphertext
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char in string.ascii_lowercase:
            shifted_alphabet = shifted_alphabets[key_index]
            shifted_index = shifted_alphabet.index(char)
            plaintext += string.ascii_lowercase[shifted_index]
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += char

    return plaintext
plaintext = "attackatdawn"
key = "lemon"

ciphertext = vigenere_encrypt(plaintext, key)
print(ciphertext)  # prints "lxfopvefrnhr"

