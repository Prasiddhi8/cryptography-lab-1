def expansion_pbox(input_bits):
    
    
    # The Expansion P-box table
    expansion_table = [
        32,  1,  2,  3,  4,  5,
         4,  5,  6,  7,  8,  9,
         8,  9, 10, 11, 12, 13,
        12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25,
        24, 25, 26, 27, 28, 29,
        28, 29, 30, 31, 32,  1
    ]
    
    # Ensure input is exactly 32 bits
    if len(input_bits) != 32 or not set(input_bits).issubset({'0', '1'}):
        raise ValueError("Input must be a 32-bit string of '0's and '1's")
    
    # Apply the expansion table
    expanded_bits = ''.join(input_bits[i - 1] for i in expansion_table)
    
    return expanded_bits

def main():
    # Example 32-bit input
    input_bits = "11001100110011001100110011001100"
    
    print("Input (32 bits):")
    print(input_bits)
    
    # Perform expansion
    expanded_bits = expansion_pbox(input_bits)
    
    print("Expanded Output (48 bits):")
    print(expanded_bits)

if __name__ == "__main__":
    main()