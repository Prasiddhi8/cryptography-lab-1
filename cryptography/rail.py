def encrypt_rail_fence(text, rails):
    fence = [['\n' for _ in range(len(text))] for _ in range(rails)]
    direction_down = False
    row, col = 0, 0
    for char in text:
        if row == 0 or row == rails - 1:
            direction_down = not direction_down
        fence[row][col] = char
        col += 1
        if direction_down:
            row += 1
        else:
            row -= 1
    encrypted_text = []
    for i in range(rails):
        for j in range(len(text)):
            if fence[i][j] != '\n':
                encrypted_text.append(fence[i][j])
    return ''.join(encrypted_text)


def decrypt_rail_fence(ciphertext, rails):
    fence = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    direction_down = None
    row, col = 0, 0
    for char in ciphertext:
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        fence[row][col] = '*'
        col += 1
        if direction_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if fence[i][j] == '*' and index < len(ciphertext):
                fence[i][j] = ciphertext[index]
                index += 1
    row, col = 0, 0
    decrypted_text = []
    for _ in range(len(ciphertext)):
        if row == 0:
            direction_down = True
        if row == rails - 1:
            direction_down = False
        if fence[row][col] != '\n':
            decrypted_text.append(fence[row][col])
        col += 1
        if direction_down:
            row += 1
        else:
            row -= 1
    return ''.join(decrypted_text)


# Example usage:
text = "prasiddhi acharya"
rails = 3
encrypted_text = encrypt_rail_fence(text, rails)
print("Encrypted message:", encrypted_text)
decrypted_text = decrypt_rail_fence(encrypted_text, rails)
print("Decrypted message:", decrypted_text)