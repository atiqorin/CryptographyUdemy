ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def crack(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''
        
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]

        print('With key %s: the result is %s' % (key, plain_text))

def read_from_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

if __name__ == '__main__':
    crack(read_from_file('m.txt'))