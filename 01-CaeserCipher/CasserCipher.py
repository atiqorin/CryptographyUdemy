ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()
    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]

    return cipher_text

def decrypt(cipher_text):
    plain_text = ''
    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

    return plain_text

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == '__main__':
    KEY = int(read_from_file('key.txt'))
    m = read_from_file('m.txt')

    cipher_text = encrypt(m)
    write_to_file('m.txt', cipher_text)

    c = read_from_file('m.txt')

    print(decrypt(c))