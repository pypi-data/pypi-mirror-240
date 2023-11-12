# Tanji Encryption Library 👩‍💻🔐

Tanji is a Python encryption library that provides a secure and flexible solution for encrypting and decrypting messages. It leverages both symmetric and asymmetric encryption techniques to ensure the confidentiality and integrity of your data.

## Features 🚀

- **Symmetric Encryption:** Utilizes the Advanced Encryption Standard (AES) algorithm for symmetric key encryption.
- **Asymmetric Encryption:** Employs RSA algorithm for secure asymmetric key encryption.
- **Base64 Encoding:** Efficiently encodes encrypted data using Base64 for safe transmission.
- **Key Pair Generation:** Automatically generates RSA key pairs for secure communication.
- **Random Initialization Vectors (IV):** Uses random IVs to enhance security.
- **Ease of Use:** Simple and straightforward interface for encrypting and decrypting messages.

## How Tanji Differs 🤔

- **Robust Security:** Tanji prioritizes the security of your data by combining symmetric and asymmetric encryption methods.
- **Key Pair Generation:** Automatically generates and manages RSA key pairs, simplifying the encryption process.
- **Dynamic Initialization Vectors:** Randomly generated IVs for each encryption enhance the resistance against cryptographic attacks.
- **Base64 Encoding:** Encoded data ensures compatibility and safe transmission across different systems.
- **Developer-Friendly:** Designed to be user-friendly and easily integrated into various Python projects.

## Getting Started 🏁

1. Install Tanji:

    ```bash
    pip install tanji
    ```

2. Use Tanji in your Python project:

    ```python
    from tanji.tanji import Tanji

    # Example Usage
    tanji = Tanji()
    encrypted_message, ciphertext = tanji.encrypt_message("Hello, Tanji!")
    decrypted_message = tanji.decrypt_message(encrypted_message, ciphertext)

    print("Original Message:", "Hello, Tanji!")
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", decrypted_message)
    ```

## Contributing 🤝

Contributions are welcome! Feel free to submit issues or pull requests.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
