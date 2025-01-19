from random import randint
import matplotlib.pyplot as plt

ALPHABET = ' .,;-!@()0123456789abcdefghijklmnopqrstuvwxyz'


def encrypt(text, key):

    text = text.lower()
    cipher_text = ''

    for index, char in enumerate(text):
        key_index = key[index]
        key_val = (ALPHABET.find(key_index) + len(ALPHABET)) % len(ALPHABET)
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_val) % len(ALPHABET)]

    return cipher_text


def decrypt(cipher_text, key):

    plain = ''

    for index, char in enumerate(cipher_text):
        key_index = key[index]
        key_val = (ALPHABET.find(key_index) + len(ALPHABET)) % len(ALPHABET)
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_val) % len(ALPHABET)]

    return plain


def random_sequence(text):

    random = []

    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET)-1))
    key = ''
    for i in range(len(random)):
        key += ALPHABET[random[i]]
    return key


def frequency_analysis(text):
    text = text.upper()

    letter_frequency = {}

    for letter in ALPHABET:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1

    return letter_frequency


def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


def plot_distribution(letter_frequency):
    plt.bar(letter_frequency.keys(), letter_frequency.values())
    plt.show()


if __name__ == '__main__':
    message = read_from_file('m.md')

    random_seq = random_sequence(message)
    write_to_file('key.md', random_seq)
    KEY = read_from_file('key.md')

    print("Original message: %s" % message.lower())
    cipher_text = encrypt(message, KEY)
    write_to_file('m.md', cipher_text)
    print("Encrypted message: %s" % cipher_text)
    c = read_from_file('m.md')
    decrypted_text = decrypt(c, KEY)
    print("Decrypted message: %s" % decrypted_text)
    plot_distribution(frequency_analysis(cipher_text))
