from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(key)
nonce = os.urandom(12)

message = b"Amount: 100 USD"
ciphertext = aesgcm.encrypt(nonce, message, None)

print("Original message:", message)
print("Ciphertext (hex) :", ciphertext.hex())

tampered_ciphertext = bytearray(ciphertext)
tampered_ciphertext[8] ^= 0x08

try:
    decrypted = aesgcm.decrypt(nonce, bytes(tampered_ciphertext), None)
    print("Tampered message successfully decrypted:", decrypted)
except Exception as e:
    print("ERROR: Message rejected, integrity check failed ->", type(e).__name__)