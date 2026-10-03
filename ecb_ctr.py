from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PIL import Image
import os

img = Image.open("original.bmp")
header_size = 54
with open("original.bmp", "rb") as f:
    data = f.read()

header = data[:header_size]
pixels = data[header_size:]

pad_len = (16 - len(pixels) % 16) % 16
padded_pixels = pixels + b"\x00" * pad_len

key = os.urandom(16)

cipher_ecb = Cipher(algorithms.AES(key), modes.ECB())
encryptor_ecb = cipher_ecb.encryptor()
ecb_encrypted = encryptor_ecb.update(padded_pixels) + encryptor_ecb.finalize()

nonce = os.urandom(16)
cipher_ctr = Cipher(algorithms.AES(key), modes.CTR(nonce))
encryptor_ctr = cipher_ctr.encryptor()
ctr_encrypted = encryptor_ctr.update(padded_pixels) + encryptor_ctr.finalize()

with open("ecb_encrypted.bmp", "wb") as f:
    f.write(header + ecb_encrypted[:len(pixels)])

with open("ctr_encrypted.bmp", "wb") as f:
    f.write(header + ctr_encrypted[:len(pixels)])

print("ecb_encrypted.bmp and ctr_encrypted.bmp created")