import numpy as np

def mod_inv(a, m):
    # Find the modular inverse of a under modulo m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    # Find the matrix inverse in modulo arithmetic
    det = int(np.round(np.linalg.det(matrix)))  # Determinant
    det_inv = mod_inv(det % modulus, modulus)   # Modular inverse of determinant
    if det_inv is None:
        raise ValueError("The matrix is not invertible in the given modulus")

    # Calculate the adjugate matrix
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )

    return matrix_modulus_inv % modulus

def text_to_numbers(text):
    # Convert text to numbers (A=0, B=1, ..., Z=25)
    return [ord(char) - ord('A') for char in text]

def numbers_to_text(numbers):
    # Convert numbers back to text
    return ''.join(chr(num + ord('A')) for num in numbers)

def encrypt(plain_text, key_matrix):
    plain_numbers = text_to_numbers(plain_text)
    plain_matrix = np.array(plain_numbers).reshape(-1, key_matrix.shape[0])
    
    cipher_matrix = np.dot(plain_matrix, key_matrix) % 26
    cipher_numbers = cipher_matrix.flatten().tolist()
    
    return numbers_to_text(cipher_numbers)

def decrypt(cipher_text, key_matrix):
    cipher_numbers = text_to_numbers(cipher_text)
    cipher_matrix = np.array(cipher_numbers).reshape(-1, key_matrix.shape[0])
    
    inv_key_matrix = matrix_mod_inv(key_matrix, 26)
    plain_matrix = np.dot(cipher_matrix, inv_key_matrix) % 26
    plain_numbers = plain_matrix.flatten().tolist()
    
    return numbers_to_text(plain_numbers)

# Example usage
if __name__ == "__main__":
    # Your name (must be adjusted to fit the matrix size)
    name = "PRASIDDHI ACHARYA"
    # Ensure the length of the name matches the size of the key matrix
    while len(name) % 2 != 0:
        name += 'X'  # Padding with 'X' if necessary
    
    key_matrix = np.array([[3, 3], [2, 5]])
    
    encrypted_name = encrypt(name, key_matrix)
    decrypted_name = decrypt(encrypted_name, key_matrix)
    
    print(f"Original Name: {name}")
    print(f"Encrypted Name: {encrypted_name}")
    print(f"Decrypted Name: {decrypted_name}")