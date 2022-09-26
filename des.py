from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode
from json import dumps, loads

def des_encrypt(data: str, key: str) -> str:
    cipher = DES.new(key, DES.MODE_CBC)
    cipher_bytes = cipher.encrypt(pad(data, DES.block_size))
    init_vector = b64encode(cipher.iv).decode('utf-8')
    cipher_text = b64encode(cipher_bytes).decode('utf-8')
    encrypted = dumps({'init_vector':init_vector, 'ciphertext':cipher_text})
    return encrypted

def des_decrypt(encrypted: str, key: str) -> str:
    b64 = loads(encrypted)
    init_vector = b64decode(b64['init_vector'])
    cipher_text = b64decode(b64['ciphertext'])
    cipher = DES.new(key, DES.MODE_CBC, init_vector)
    plaintext = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return plaintext
