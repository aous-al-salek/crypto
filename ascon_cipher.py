from ascon import encrypt
from ascon import decrypt
from Crypto.Random import get_random_bytes

def ascon128_encrypt(data: str, key: str) -> str:
    nonce = get_random_bytes(16)
    associateddata = get_random_bytes(32)
    encrypted = encrypt(key, nonce, associateddata, data, "Ascon-128")
    return encrypted

def ascon128_decrypt(encrypted: str, key: str) -> str:
    nonce = get_random_bytes(16)
    associateddata = get_random_bytes(32)
    plaintext = decrypt(key, nonce, associateddata, encrypted, "Ascon-128")
    return plaintext

def ascon128a_encrypt(data: str, key: str) -> str:
    nonce = get_random_bytes(16)
    associateddata = get_random_bytes(32)
    encrypted = encrypt(key, nonce, associateddata, data, "Ascon-128a")
    return encrypted

def ascon128a_decrypt(encrypted: str, key: str) -> str:
    nonce = get_random_bytes(16)
    associateddata = get_random_bytes(32)
    plaintext = decrypt(key, nonce, associateddata, encrypted, "Ascon-128a")
    return plaintext

def ascon80pq_encrypt(data: str, key: str) -> str:
    nonce = get_random_bytes(16)
    associateddata = get_random_bytes(32)
    encrypted = encrypt(key, nonce, associateddata, data, "Ascon-80pq")
    return encrypted

def ascon80pq_decrypt(encrypted: str, key: str) -> str:
    nonce = get_random_bytes(16)
    associateddata = get_random_bytes(32)
    plaintext = decrypt(key, nonce, associateddata, encrypted, "Ascon-80pq")
    return plaintext
