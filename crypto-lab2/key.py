def permute(block, table):
    return [block[i - 1] for i in table]

def left_shift(block, num_shifts):
    return block[num_shifts:] + block[:num_shifts]

def key_generation(key):
    PC1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    
    PC2 = [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]
    
    LEFT_SHIFTS = [
        1, 1, 2, 2, 2, 2, 2, 2,
        1, 2, 2, 2, 2, 2, 2, 1
    ]
    
    # Step 1: Apply PC-1 permutation
    key_56 = permute(key, PC1)
    
    # Step 2: Split into two halves
    left_half = key_56[:28]
    right_half = key_56[28:]
    
    # Generate 16 subkeys
    subkeys = []
    for shift in LEFT_SHIFTS:
        # Step 3: Left shift both halves
        left_half = left_shift(left_half, shift)
        right_half = left_shift(right_half, shift)
        
        # Step 4: Combine halves and apply PC-2 permutation
        combined = left_half + right_half
        subkey = permute(combined, PC2)
        subkeys.append(subkey)
    
    return subkeys

def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:].zfill(64)
    return [int(bit) for bit in binary_string]

def binary_to_hex(bit_list):
    binary_string = ''.join(str(bit) for bit in bit_list)
    hex_string = hex(int(binary_string, 2))[2:].upper().zfill(16)
    return hex_string

def list_to_binary_string(bit_list):
    return ''.join(str(bit) for bit in bit_list)

# Example usage
if __name__ == "__main__":
    # Example 64-bit key in hexadecimal
    input_key_hex = '133457799BBCDFF1'  # Example 64-bit key in hexadecimal
    
    # Convert the hexadecimal key to a list of bits
    key_bits = hex_to_binary(input_key_hex)
    
    # Generate subkeys
    subkeys = key_generation(key_bits)
    
    # Print subkeys
    for i, subkey in enumerate(subkeys):
        print(f"Subkey {i+1:02d}: {list_to_binary_string(subkey)}")