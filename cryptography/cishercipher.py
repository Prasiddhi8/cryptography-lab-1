def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
        else:
            result += char
    return result

# Your full name
full_name = "prasiddhi acharya"  # Replace with your full name
shift = 3  # Shift of 3 for Caesar Cipher

encrypted_name = caesar_cipher(full_name, shift)
decrypted_name = caesar_cipher(encrypted_name, -shift)

print(f"Original Name: {full_name}")
print(f"Encrypted Name: {encrypted_name}")
print(f"Decrypted Name: {decrypted_name}")