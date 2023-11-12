import secrets
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class SymmetricCipher:
    @staticmethod
    def generate_key():
        return secrets.token_bytes(32)  # 256 bits

    @staticmethod
    def generate_iv():
        return secrets.token_bytes(16)  # 128 bits

    @staticmethod
    def aes_encrypt(key, iv, plaintext):
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        # Ensure that the input is in bytes
        ciphertext = encryptor.update(plaintext.encode('utf-8')) + encryptor.finalize()
        return ciphertext

    @staticmethod
    def aes_decrypt(key, iv, ciphertext):
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode('utf-8')
