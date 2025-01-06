import string
from itertools import cycle

class VigenereAutokeyCipher:
    def __init__(self, key, abc=string.ascii_uppercase):
        self.key = key.upper()
        self.abc = abc.upper()

    def encode(self, text):
        result = []
        key = self.key + ''.join([t for t in text.upper() if t in self.abc])
        index = 0
        for c in text.upper():
            if c in self.abc:
                offset = self.abc.index(key[index])
                result.append(self.abc[(self.abc.index(c) + offset) % len(self.abc)])
                index += 1
            else:
                result.append(c)
        return ''.join(result)

    def decode(self, text):
        result = []
        key = self.key
        index = 0
        for c in text.upper():
            if c in self.abc:
                offset = self.abc.index(key[index])
                decoded = self.abc[(self.abc.index(c) - offset) % len(self.abc)]
                result.append(decoded)
                key += decoded
                index += 1
            else:
                result.append(c)
        return ''.join(result)

def caesar_cipher(text, shift, encrypt=True):
    """Implements Caesar cipher for encryption and decryption."""
    shift = shift if encrypt else -shift
    alphabet = string.ascii_uppercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.upper().translate(table)

def rot13(text):
    """Special case of Caesar cipher with a shift of 13."""
    return caesar_cipher(text, 13)

def vigenere_cipher(text, key, encrypt=True):
    """Implements Vigenère cipher for encryption and decryption."""
    alphabet = string.ascii_uppercase

    def compute_shift(c, encrypt):
        return alphabet.index(c) if encrypt else -alphabet.index(c)

    key_cycle = cycle(key.upper())
    result = []
    for char in text.upper():
        if char in alphabet:
            shift = compute_shift(next(key_cycle), encrypt)
            result.append(alphabet[(alphabet.index(char) + shift) % 26])
        else:
            result.append(char)
    return ''.join(result)

def autokey_cipher(text, key, encrypt=True):
    """Implements Autokey cipher for encryption and decryption."""
    text = text.upper()
    key = key.upper()
    alphabet = string.ascii_uppercase
    result = []
    full_key = key

    if encrypt:
        for char in text:
            if char in alphabet:
                offset = alphabet.index(full_key[0])
                full_key += char  # Append plaintext progressively to key
                result.append(alphabet[(alphabet.index(char) + offset) % 26])
                full_key = full_key[1:]  # Remove used key character
            else:
                result.append(char)
    else:
        for char in text:
            if char in alphabet:
                offset = alphabet.index(full_key[0])
                decoded_char = alphabet[(alphabet.index(char) - offset) % 26]
                full_key += decoded_char  # Append decoded character to key
                result.append(decoded_char)
                full_key = full_key[1:]  # Remove used key character
            else:
                result.append(char)

    return ''.join(result)

def beaufort_cipher(text, key):
    """Implements Beaufort cipher for symmetric encryption/decryption."""
    alphabet = string.ascii_uppercase
    text = text.upper().replace(' ', '')
    key = key.upper().replace(' ', '')
    key = (key * (len(text) // len(key) + 1))[:len(text)]
    result = []

    for t, k in zip(text, key):
        if t in alphabet:
            idx = (alphabet.index(k) - alphabet.index(t)) % 26
            result.append(alphabet[idx])
        else:
            result.append(t)
    return ''.join(result)

def create_playfair_matrix(key):
    """Creates a 5x5 matrix for Playfair cipher, merging J into I."""
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key = key.upper().replace(' ', '').replace('J', 'I')
    matrix = ''
    for char in key + alphabet:
        if char not in matrix:
            matrix += char
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_cipher(text, key, encrypt=True):
    """Implements Playfair cipher for encryption and decryption."""
    matrix = create_playfair_matrix(key)
    text = text.upper().replace(' ', '').replace('J', 'I')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    result = []
    for a, b in pairs:
        row1, col1 = next((r, c) for r, line in enumerate(matrix) for c, char in enumerate(line) if char == a)
        row2, col2 = next((r, c) for r, line in enumerate(matrix) for c, char in enumerate(line) if char == b)

        if row1 == row2:
            col1 = (col1 + 1) % 5 if encrypt else (col1 - 1) % 5
            col2 = (col2 + 1) % 5 if encrypt else (col2 - 1) % 5
        elif col1 == col2:
            row1 = (row1 + 1) % 5 if encrypt else (row1 - 1) % 5
            row2 = (row2 + 1) % 5 if encrypt else (row2 - 1) % 5
        else:
            col1, col2 = col2, col1

        result.append(matrix[row1][col1])
        result.append(matrix[row2][col2])

    decrypted_text = ''.join(result)
    if not encrypt and decrypted_text.endswith('X'):
        decrypted_text = decrypted_text[:-1]

    return decrypted_text

def menu():
    """Displays the main menu for cipher selection."""
    print("\nCryptography Machine")
    print("1. Caesar Cipher")
    print("2. ROT13 Cipher")
    print("3. Vigenère Cipher")
    print("4. Autokey Cipher")
    print("5. Beaufort Cipher")
    print("6. Playfair Cipher")
    print("7. Exit")
    return input("Select an option: ")

def main():
    while True:
        try:
            choice = menu()
            if choice == '1':
                text = input("Enter text: ")
                shift = int(input("Enter shift value (integer): "))
                operation = input("Encrypt or Decrypt (e/d): ").lower()
                if operation not in ['e', 'd']:
                    raise ValueError("Invalid choice for operation. Use 'e' for encrypt or 'd' for decrypt.")
                encrypt = operation == 'e'
                print("Result:", caesar_cipher(text, shift, encrypt))

            elif choice == '2':
                text = input("Enter text: ")
                print("Result:", rot13(text))

            elif choice == '3':
                text = input("Enter text: ")
                key = input("Enter key: ")
                operation = input("Encrypt or Decrypt (e/d): ").lower()
                if operation not in ['e', 'd']:
                    raise ValueError("Invalid choice for operation. Use 'e' for encrypt or 'd' for decrypt.")
                encrypt = operation == 'e'
                print("Result:", vigenere_cipher(text, key, encrypt))

            elif choice == '4':
                text = input("Enter text: ")
                key = input("Enter key: ")
                operation = input("Encrypt or Decrypt (e/d): ").lower()
                if operation not in ['e', 'd']:
                    raise ValueError("Invalid choice for operation. Use 'e' for encrypt or 'd' for decrypt.")
                encrypt = operation == 'e'
                print("Result:", autokey_cipher(text, key, encrypt))

            elif choice == '5':
                text = input("Enter text: ")
                key = input("Enter key: ")
                print("Result:", beaufort_cipher(text, key))

            elif choice == '6':
                text = input("Enter text: ")
                key = input("Enter key: ")
                operation = input("Encrypt or Decrypt (e/d): ").lower()
                if operation not in ['e', 'd']:
                    raise ValueError("Invalid choice for operation. Use 'e' for encrypt or 'd' for decrypt.")
                encrypt = operation == 'e'
                print("Result:", playfair_cipher(text, key, encrypt))

            elif choice == '7':
                print("Exiting Cryptography Machine. Goodbye!")
                break

            else:
                print("Invalid option. Please select a valid menu option.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

# Testing Script
import unittest

class TestCryptographyMachine(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("HELLO", 3, encrypt=True), "KHOOR")
        self.assertEqual(caesar_cipher("KHOOR", 3, encrypt=False), "HELLO")

    def test_rot13(self):
        self.assertEqual(rot13("HELLO"), "URYYB")
        self.assertEqual(rot13("URYYB"), "HELLO")

    def test_vigenere_cipher(self):
        self.assertEqual(vigenere_cipher("ATTACK", "LEMON", encrypt=True), "LXFOPV")
        self.assertEqual(vigenere_cipher("LXFOPV", "LEMON", encrypt=False), "ATTACK")

    def test_autokey_cipher(self):
        self.assertEqual(autokey_cipher("HELLO", "KEY", encrypt=True), "JVJAH")
        self.assertEqual(autokey_cipher("JVJAH", "KEY", encrypt=False), "HELLO")

    def test_beaufort_cipher(self):
        self.assertEqual(beaufort_cipher("HELLO", "KEY"), "DANZQ")
        self.assertEqual(beaufort_cipher("DANZQ", "KEY"), "HELLO")

    def test_playfair_cipher(self):
        self.assertEqual(playfair_cipher("HELLO", "KEY", encrypt=True), "DBNVMI")
        self.assertEqual(playfair_cipher("DBNVMI", "KEY", encrypt=False), "HELLO")

if __name__ == "__main__":
    unittest.main()
