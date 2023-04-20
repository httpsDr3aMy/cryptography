def char_to_num(char):
    return ord(char.lower()) - 97

def num_to_char(num):
    return chr(num + 97)

def encrypt(message, key):
    n = int(len(key)**0.5)
    message = [char_to_num(c) for c in message if c.isalpha()]
    # dopełnienie wiadomości zerami
    if len(message) % n != 0:
        message += [0] * (n - len(message) % n)
    # konwersja wiadomości na macierz
    message_matrix = [message[i:i+n] for i in range(0, len(message), n)]
    # mnożenie macierzy przez klucz
    encrypted_matrix = [[sum([key[i][j] * message_matrix[x][j] for j in range(n)]) % 26 for i in range(n)] for x in range(len(message_matrix))]
    # konwersja macierzy na zaszyfrowaną wiadomość
    encrypted_message = ''.join([num_to_char(encrypted_matrix[i][j]) for i in range(len(message_matrix)) for j in range(n)])
    return encrypted_message

def decrypt(message, key):
    n = int(len(key)**0.5)
    # obliczenie odwrotności modulo 26
    determinant = key[0][0]*key[1][1] - key[0][1]*key[1][0]
    det_inv = 0
    for i in range(26):
        if (determinant*i) % 26 == 1:
            det_inv = i
            break
    # obliczenie macierzy odwrotnej
    key_inv = [[0 for i in range(n)] for j in range(n)]
    key_inv[0][0] = key[1][1] * det_inv % 26
    key_inv[0][1] = (-key[0][1]) * det_inv % 26
    key_inv[1][0] = (-key[1][0]) * det_inv % 26
    key_inv[1][1] = key[0][0] * det_inv % 26
    # konwersja wiadomości na macierz
    message_matrix = [[char_to_num(c) for c in message[i:i+n]] for i in range(0, len(message), n)]
    # mnożenie macierzy przez macierz odwrotną
    decrypted_matrix = [[sum([key_inv[i][j] * message_matrix[x][j] for j in range(n)]) % 26 for i in range(n)] for x in range(len(message_matrix))]
    # konwersja macierzy na odszyfrowaną wiadomość
    decrypted_message = ''.join([num_to_char(decrypted_matrix[i][j]) for i in range(len(message_matrix)) for j in range(n)])
    return decrypted_message

encrypted_message = encrypt("Hello, World!", [[1, 2], [3, 4]])

#decrypted_message = decrypt(encrypted_message, [[1, 2], [3, 4]])

print(encrypted_message)

