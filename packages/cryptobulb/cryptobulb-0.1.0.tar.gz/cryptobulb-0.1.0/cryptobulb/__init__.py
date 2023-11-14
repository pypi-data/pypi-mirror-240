def rsa():
    s = """
    import random

    # Generate random prime numbers
    def generate_prime(bits):
        while True:
            n = random.getrandbits(bits)
            if n % 2 != 0 and is_prime(n):
                return n

    # Check if a number is prime
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    # Calculate the greatest common divisor (GCD) of two numbers
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    # Extended Euclidean Algorithm to find modular multiplicative inverse
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            gcd_val, x, y = extended_gcd(b % a, a)
            return (gcd_val, y - (b // a) * x, x)

    # Generate RSA key pair
    def generate_keypair(bits):
        p = generate_prime(bits)
        q = generate_prime(bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537  # Common choice for the public exponent
        gcd_val, d, _ = extended_gcd(e, phi)
        while d < 0:
            d += phi
        return ((n, e), (n, d))

    # Encrypt a message using RSA
    def encrypt(public_key, plaintext):
        n, e = public_key
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

    # Decrypt a message using RSA
    def decrypt(private_key, ciphertext):
        n, d = private_key
        plaintext = [chr(pow(char, d, n)) for char in ciphertext]
        return ''.join(plaintext)

    # Example usage
    if __name__ == "__main__":
        bits = 128  # Adjust the key size as needed
        public_key, private_key = generate_keypair(bits)
        message = "Hello, RSA Encryption!"
        print("Original message:", message)
        encrypted_message = encrypt(public_key, message)
        print("Encrypted message:", encrypted_message)
        decrypted_message = decrypt(private_key, encrypted_message)
        print("Decrypted message:", decrypted_message)

        """
    print(s)
    
def des():
    s = """
    # Initial permutation (IP) table
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    # Inverse initial permutation (IP^-1) table
    IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
    # Expansion (E) table
    E = [4, 1, 2, 3, 2, 3, 4, 1]
    # P4 permutation table
    P4 = [2, 4, 3, 1]
    # P8 permutation table
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]
    # S-boxes
    S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
    S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
    # Key generation: Permuted Choice 1 (PC-1) table
    PC1 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    # Key generation: Permuted Choice 2 (PC-2) table
    PC2 = [6, 3, 7, 4, 8, 5, 10, 9]

    def permute(input_block, permutation_table):
        return [input_block[i - 1] for i in permutation_table]

    def left_shift(bits, n):
        return bits[n:] + bits[:n]

    def generate_subkeys(key):
        key = permute(key, PC1)
        subkeys = []
        for i in range(3):
            key = left_shift(key[:5], 1) + left_shift(key[5:], 1)
            subkey = permute(key, PC2)
            subkeys.append(subkey)
        return subkeys

    def apply_sbox(input_block, sbox):
        row = int(input_block[0] + input_block[3], 2)
        col = int(input_block[1] + input_block[2], 2)
        return format(sbox[row][col], '02b')

    def f_function(r_block, subkey):
        expanded_r = permute(r_block, E)
        xor_result = int(''.join(expanded_r), 2) ^ int(''.join(subkey), 2)
        xor_result = format(xor_result, '08b')
        left_half = xor_result[:4]
        right_half = xor_result[4:]
        s0_input = apply_sbox(left_half, S0)
        s1_input = apply_sbox(right_half, S1)
        return permute(s0_input + s1_input, P4)

    def simplified_des_encrypt(plain_text, key):
        key = [int(bit) for bit in key]
        subkeys = generate_subkeys(key)
        # Initial permutation (IP)
        plain_text = permute(plain_text, IP)
        left_block = plain_text[:4]
        right_block = plain_text[4:]
        for i in range(3):
            f_result = f_function(right_block, subkeys[i])
            new_right_block = [int(left_block[j]) ^ int(f_result[j]) for j in range(4)]
            left_block = right_block
            right_block = new_right_block
        cipher_text = permute(right_block + left_block, IP_INV)
        return ''.join(map(str, cipher_text))

    def simplified_des_decrypt(cipher_text, key):
        key = [int(bit) for bit in key]
        subkeys = generate_subkeys(key)
        # Initial permutation (IP)
        cipher_text = permute(cipher_text, IP)
        left_block = cipher_text[:4]
        right_block = cipher_text[4:]
        for i in range(3):
            f_result = f_function(right_block, subkeys[2 - i])
            new_right_block = [int(left_block[j]) ^ int(f_result[j]) for j in range(4)]
            left_block = right_block
            right_block = new_right_block
        plain_text = permute(right_block + left_block, IP_INV)
        return ''.join(map(str, plain_text))

    # Example usage
    plain_text = "10101010"  # 8-bit plaintext
    key = "1010000010"  # 10-bit key
    cipher_text = simplified_des_encrypt(plain_text, key)
    print("Encrypted:", cipher_text)
    decrypted_text = simplified_des_decrypt(cipher_text, key)
    print("Decrypted:", decrypted_text)

    """
    print(s)

def rail():
    s = """
    def rail_fence_cipher_encrypt(plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_num = 0
        direction = 1
        
        for char in plain_text:
            rails[rail_num].append(char)
            
            if rail_num == 0:
                direction = 1
            elif rail_num == num_rails - 1:
                direction = -1
                
            rail_num += direction
            
        ciphertext = ''.join(''.join(rail) for rail in rails)
        return ciphertext

    def rail_fence_cipher_decrypt(ciphertext, num_rails):
        rails = [[' ' for _ in range(len(ciphertext))] for _ in range(num_rails)]
        rail_num = 0
        direction = 1
        
        for i in range(len(ciphertext)):
            rails[rail_num][i] = '*'
            
            if rail_num == 0:
                direction = 1
            elif rail_num == num_rails - 1:
                direction = -1
                
            rail_num += direction
        
        index = 0
        
        for i in range(num_rails):
            for j in range(len(ciphertext)):
                if rails[i][j] == '*' and index < len(ciphertext):
                    rails[i][j] = ciphertext[index]
                    index += 1
                    
        rail_num = 0
        direction = 1
        decrypted_text = ''
        
        for i in range(len(ciphertext)):
            decrypted_text += rails[rail_num][i]
            
            if rail_num == 0:
                direction = 1
            elif rail_num == num_rails - 1:
                direction = -1
                
            rail_num += direction
            
        return decrypted_text

    plaintext = "Hello, Rail Fence Cipher!"
    num_rails = 3

    cipher_text = rail_fence_cipher_encrypt(plaintext, num_rails)
    print("Ciphertext:", cipher_text)

    decrypted_text = rail_fence_cipher_decrypt(cipher_text, num_rails)
    print("Decrypted Text:", decrypted_text)


    """
    print(s)
def affine():
    s = """
    # Affine Cipher
    def plain_cipher(plain, b):
        ct = ""
        plain = plain.upper()
        
        for i in plain:
            x = ord(i) - 65
            o2 = (5 * x) + b
            mo = (o2 % 26)
            ct = ct + chr(mo + 65)
            
        return ct

    def cipher_plain(ct):
        pt = ""
        ct = ct.upper()
        
        for i in ct:
            y = ord(i) - 65
            o2 = 21 * (y - 8)
            mo = (o2 % 26)
            pt = pt + chr(mo + 65)
            
        return pt

    print("Cipher Text : ", end=" ")
    ct = plain_cipher('karunyainstitute', 8)
    print(ct)

    print("\nPlain text : ", cipher_plain(ct), end=" ")


    """
    print(s)