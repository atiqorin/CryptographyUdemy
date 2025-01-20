import matplotlib.pyplot as plt
ALPHABET = ' .,;-!@()0123456789abcdefghijklmnopqrstuvwxyz'


def encrypt(plain_text, key):
    plain_text = plain_text.lower()
    key = key.lower()

    cipher_text = ''
    key_index = 0

    for character in plain_text:
        index = (ALPHABET.find(character)+ALPHABET.find(key[key_index])) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]

        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0

    return cipher_text


def decrypt(cipher_text, key):

    cipher_text = cipher_text.lower()
    key = key.lower()

    plain_text = ''
    key_index = 0

    for character in cipher_text:
        index = (ALPHABET.find(character)-ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]

        key_index = key_index + 1

        if key_index == len(key):
            key_index = 0

    return plain_text


def frequency_analysis(text):
    text = text.lower()

    letter_frequency = {}

    for letter in ALPHABET:
        letter_frequency[letter] = 0

    for letter in text:
        if letter in ALPHABET:
            letter_frequency[letter] += 1

    return letter_frequency


def plot_distribution(letter_frequency):
    plt.bar(letter_frequency.keys(), letter_frequency.values())
    plt.show()



def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()
    

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


if __name__ == '__main__':
    KEY = read_from_file('key.md')
    m = read_from_file('m.md')

    cipher_text = encrypt(m, KEY)
    print("encrypted message: %s" % cipher_text)
    write_to_file('m.md', cipher_text)
    plot_distribution(frequency_analysis(cipher_text))

    c = read_from_file('m.md')
    print(decrypt(c, KEY))
