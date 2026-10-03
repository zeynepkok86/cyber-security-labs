from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

key = os.urandom(16)
nonce = os.urandom(16)

message = b"Amount: 100 USD"

cipher = Cipher(algorithms.AES(key), modes.CTR(nonce))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(message) + encryptor.finalize()

print("Original message :", message)
print("Ciphertext (hex) :", ciphertext.hex())

tampered_ciphertext = bytearray(ciphertext)
tampered_ciphertext[8] ^= 0x08

cipher2 = Cipher(algorithms.AES(key), modes.CTR(nonce))
decryptor = cipher2.decryptor()
decrypted = decryptor.update(bytes(tampered_ciphertext)) + decryptor.finalize()

print("Tampered ciphertext after decryption:", decrypted)