import hashlib
import time
from argon2 import PasswordHasher

password = b"sample_password_123"

start = time.perf_counter()
for i in range(100000):
    hashlib.sha256(password).hexdigest()
end = time.perf_counter()
print("SHA-256 (100000 iterations) time:", end - start, "seconds")

ph = PasswordHasher()
start = time.perf_counter()
ph.hash(password.decode())
end = time.perf_counter()
print("Argon2id (1 iteration) time:", end - start, "seconds")