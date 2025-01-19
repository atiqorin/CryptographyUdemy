from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

key = b'mysecret'
key2 = get_random_bytes(8)
print(key2)

cipher = DES.new(key, DES.MODE_CBC)
print(cipher.iv)
print(DES.block_size)

plain = b"The boy's name wasSantiago. Dusk was falling as the boy arrived with his herd at an abandoned church. The roof had fallen in long ago, and an enormous sycamore had grown on the spot where the sacristy had once stood."
print(pad(plain, DES.block_size))

ciphertext = cipher.encrypt(pad(plain, DES.block_size))
print("encrypted message: %s" % ciphertext)
iv = cipher.iv

decrypt_cipher = DES.new(key, DES.MODE_CBC, iv)
original_test = unpad(decrypt_cipher.decrypt(ciphertext), DES.block_size)

print(original_test.decode())
