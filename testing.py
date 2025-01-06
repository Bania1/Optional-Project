import re

def generate_table(key=''):
    """Generates a Polybius square for the Four-Square Cipher."""
    alphabet = 'ABCDEFGHIJKLMNOPRSTUVWXYZ'  # Omits 'Q'
    table = [[0] * 5 for _ in range(5)]
    key = re.sub(r'[\W]', '', key).upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key[1:]
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]
    return table


def position(table, char):
    """Finds the position of a character in the table."""
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    return None, None


def four_square_encrypt(keys, plaintext):
    """Encrypts the plaintext using the Four-Square Cipher."""
    plaintext = re.sub(r'[\W]', '', plaintext).upper().replace('Q', '')
    if len(plaintext) % 2 != 0:
        plaintext += 'X'  # Padding if odd length

    square1 = generate_table(keys[0])  # Top-right
    square2 = generate_table(keys[1])  # Bottom-left
    alphabet = generate_table('')  # Default alphabet matrix

    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = position(alphabet, a)
        row2, col2 = position(alphabet, b)
        if row1 is not None and row2 is not None:
            ciphertext += square1[row1][col2] + square2[row2][col1]
    return ciphertext


def four_square_decrypt(keys, ciphertext):
    """Decrypts the ciphertext using the Four-Square Cipher."""
    ciphertext = re.sub(r'[\W]', '', ciphertext).upper()

    square1 = generate_table(keys[0])  # Top-right
    square2 = generate_table(keys[1])  # Bottom-left
    alphabet = generate_table('')  # Default alphabet matrix

    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = position(square1, a)
        row2, col2 = position(square2, b)
        if row1 is not None and row2 is not None:
            plaintext += alphabet[row1][col2] + alphabet[row2][col1]
    return plaintext.lower()


def menu():
    """Displays the main menu for cipher selection."""
    print("\nCryptography Machine")
    print("1. Four-Square Cipher")
    print("2. Exit")
    return input("Select an option: ")


def main():
    while True:
        try:
            choice = menu()
            if choice == '1':
                text = input("Enter text: ")
                key1 = input("Enter first key: ")
                key2 = input("Enter second key: ")
                keys = [key1, key2]
                operation = input("Encrypt or Decrypt (e/d): ").lower()
                if operation not in ['e', 'd']:
                    raise ValueError("Invalid choice for operation. Use 'e' for encrypt or 'd' for decrypt.")
                if operation == 'e':
                    print("Result:", four_square_encrypt(keys, text))
                elif operation == 'd':
                    print("Result:", four_square_decrypt(keys, text))
            elif choice == '2':
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
