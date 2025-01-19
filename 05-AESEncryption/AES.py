from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

key = b'mysecretpassword'

cipher = AES.new(key, AES.MODE_CBC)

plaintext = b'In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
iv = cipher.iv

decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
original_text = unpad(decrypt_cipher.decrypt(ciphertext), AES.block_size)

print(original_text.decode())

