def prepare_input(text):
    # Convert the text to uppercase
    text = text.upper()
    # Replace 'J' with 'I' (Playfair cipher combines I and J)
    text = text.replace("J", "I")
    # Remove any characters that are not letters
    text = "".join([char for char in text if char.isalpha()])
    return text

def generate_key_matrix(key):
    # Create a key matrix with 5x5 dimension
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    # Generate the key
    key += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(dict.fromkeys(key))  # Remove duplicates
    row = 0
    col = 0
    # Fill the key matrix
    for char in key:
        key_matrix[row][col] = char
        col += 1
        if col == 5:
            col = 0
            row += 1
            if row == 5:
                break  # Break if key matrix is full
    return key_matrix

def find_position(key_matrix, char):
    # Find the position of the character in the key matrix
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j

def encrypt(message, key):
    # Prepare the input (uppercase, remove non-alphabetic characters)
    message = prepare_input(message)
    # Generate the key matrix
    key_matrix = generate_key_matrix(key)
    # Initialize variables for storing the encrypted text
    encrypted_text = ""
    # Encrypt the message
    for i in range(0, len(message), 2):
        char1 = message[i]
        char2 = message[i + 1] if i + 1 < len(message) else 'X'  # If the message length is odd, append 'X' to make it even
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)
        if row1 == row2:  # Same row
            encrypted_text += key_matrix[row1][(col1 + 1) % 5] + key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted_text += key_matrix[(row1 + 1) % 5][col1] + key_matrix[(row2 + 1) % 5][col2]
        else:  # Different row and column
            encrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return encrypted_text

def decrypt(ciphertext, key):
    # Generate the key matrix
    key_matrix = generate_key_matrix(key)
    # Initialize variables for storing the decrypted text
    decrypted_text = ""
    # Decrypt the message
    for i in range(0, len(ciphertext), 2):
        char1 = ciphertext[i]
        char2 = ciphertext[i + 1]
        row1, col1 = find_position(key_matrix, char1)
        row2, col2 = find_position(key_matrix, char2)
        if row1 == row2:  # Same row
            decrypted_text += key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            decrypted_text += key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
        else:  # Different row and column
            decrypted_text += key_matrix[row1][col2] + key_matrix[row2][col1]
    return decrypted_text

# Example usage:
message = "prasiddhi acharya"
key = "KEYWORD"
encrypted_message = encrypt(message, key)
print("Encrypted message:", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)