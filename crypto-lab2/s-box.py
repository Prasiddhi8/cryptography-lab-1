def sbox1(input_bits):
    s1 = [
        [14,  4, 13,  1,  2, 15, 11,  8,  3, 10,  6, 12,  5,  9,  0,  7],
        [ 0, 15,  7,  4, 14,  2, 13,  1, 10,  6, 12, 11,  9,  5,  3,  8],
        [ 4,  1, 14,  8, 13,  6,  2, 11, 15, 12,  9,  7,  3, 10,  5,  0],
        [15, 12,  8,  2,  4,  9,  1,  7,  5, 11,  3, 14, 10,  0,  6, 13]
    ]
    
    # Calculate row and column from the 6-bit input
    row = int(f"{input_bits[0]}{input_bits[5]}", 2)
    column = int(f"{input_bits[1]}{input_bits[2]}{input_bits[3]}{input_bits[4]}", 2)
    
    # Get the value from the S-box
    sbox_value = s1[row][column]
    
    # Convert the S-box value to a 4-bit binary string
    sbox_output = bin(sbox_value)[2:].zfill(4)
    
    return sbox_output

def binary_string_to_list(binary_string):
    return [int(bit) for bit in binary_string]

# Example usage
if __name__ == "__main__":
    # Example 6-bit input in binary
    input_bits = '100011'  # Example 6-bit binary string
    
    # Convert the binary string to a list of integers
    bit_list = binary_string_to_list(input_bits)
    
    # Apply S-box 1
    sbox_output = sbox1(bit_list)
    print("S-box 1 Output (Binary): ", sbox_output)
    print("S-box 1 Output (Decimal): ", int(sbox_output, 2))