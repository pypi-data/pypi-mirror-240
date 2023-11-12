import base64
from .symmetric import SymmetricCipher
from .asymmetric import AsymmetricCipher

class Tanji:
    def __init__(self, secret_key=None):
        self.secret_key = secret_key
        self.private_key = None
        self.public_key = None
        self.iv = None

    def generate_key_pair(self):
        self.private_key, self.public_key = AsymmetricCipher.generate_key_pair()

    def encrypt_message(self, message):
        sym_key = SymmetricCipher.generate_key()
        self.iv = SymmetricCipher.generate_iv()

        ciphertext = SymmetricCipher.aes_encrypt(sym_key, self.iv, message)
        encrypted_sym_key = AsymmetricCipher.rsa_encrypt(sym_key, self.public_key)

        return base64.b64encode(encrypted_sym_key), base64.b64encode(ciphertext)

    def decrypt_message(self, encrypted_sym_key, ciphertext):
        # Decode base64 strings
        decoded_sym_key = base64.b64decode(encrypted_sym_key)
        decoded_ciphertext = base64.b64decode(ciphertext)

        # Decrypt the symmetric key
        sym_key = AsymmetricCipher.rsa_decrypt(decoded_sym_key, self.private_key)

        # Decrypt the message using the symmetric key and IV
        decrypted_message = SymmetricCipher.aes_decrypt(sym_key, self.iv, decoded_ciphertext)

        return decrypted_message
