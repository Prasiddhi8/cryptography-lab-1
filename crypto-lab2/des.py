def permute(block, table):
    return [block[i - 1] for i in table]

def initial_permutation(block):
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    return permute(block, ip_table)

def final_permutation(block):
    fp_table = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25
    ]
    return permute(block, fp_table)

def hex_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:].zfill(64)
    return [int(bit) for bit in binary_string]

def binary_to_hex(bit_list):
    binary_string = ''.join(str(bit) for bit in bit_list)
    hex_string = hex(int(binary_string, 2))[2:].upper().zfill(16)
    return hex_string

# Example usage
if __name__ == "__main__":
    # Example 64-bit block in hexadecimal
    input_block_hex = '0002000000000001'  # Example 64-bit hexadecimal string

    # Convert the hexadecimal string to a list of bits
    bit_list = hex_to_binary(input_block_hex)
    
    # Apply initial permutation
    permuted_block = initial_permutation(bit_list)
    print("After Initial Permutation: ", binary_to_hex(permuted_block))

    # Apply final permutation
    final_permuted_block = final_permutation(permuted_block)
    print("After Final Permutation: ", binary_to_hex(final_permuted_block))
