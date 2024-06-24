import random

def miller_rabin(n, k=5):
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n-1 as d * 2^r by factoring powers of 2 from n-1
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Helper function to perform modular exponentiation
    def modular_exponentiation(base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    # Perform k rounds of testing
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = modular_exponentiation(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

# Example usage:
n = 47
k = 5
print(f"{n} is {'a prime number' if miller_rabin(n, k) else 'not a prime number'}")