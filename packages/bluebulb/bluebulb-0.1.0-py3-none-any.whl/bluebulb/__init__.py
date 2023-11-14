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
def vernam():
    s = """
    def vernam_encrypt(plaintext, key):
        if len(plaintext) != len(key):
            raise ValueError("Plaintext and key must have the same length")
        
        ciphertext = ""
        
        for i in range(len(plaintext)):
            # XOR each character in plaintext with the corresponding character in the key
            ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
        
        return ciphertext

    def vernam_decrypt(ciphertext, key):
        if len(ciphertext) != len(key):
            raise ValueError("Ciphertext and key must have the same length")
        
        plaintext = ""
        
        for i in range(len(ciphertext)):
            # XOR each character in ciphertext with the corresponding character in the key
            plaintext += chr(ord(ciphertext[i]) ^ ord(key[i]))
        
        return plaintext

    # Example usage:
    plaintext = "Hello, World!"
    key = "RandomKey1234"  # Make sure the key is as long as the plaintext

    encrypted_text = vernam_encrypt(plaintext, key)
    decrypted_text = vernam_decrypt(encrypted_text, key)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)


    """
    print(s)
def vigenere():
    s = """
    def vigenere_encrypt(plaintext, key):
        encrypted_text = ""
        key_length = len(key)
        
        for i in range(len(plaintext)):
            char = plaintext[i]
            
            if char.isalpha():
                # Adjust the key to the current character's position and apply the shift
                shift = ord(key[i].upper()) - ord('A')
                
                if char.isupper():
                    encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
                else:
                    encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        
        return encrypted_text

    def vigenere_decrypt(ciphertext, key):
        decrypted_text = ""
        key_length = len(key)
        
        for i in range(len(ciphertext)):
            char = ciphertext[i]
            
            if char.isalpha():
                # Adjust the key to the current character's position and apply the reverse shift
                shift = ord(key[i].upper()) - ord('A')
                
                if char.isupper():
                    decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
                else:
                    decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
                
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
        
        return decrypted_text

    # Example usage:
    plaintext = "HelloWorld"
    key = "KEYKEYKEYY"  # The Vigenère key, same size as plaintext

    encrypted_text = vigenere_encrypt(plaintext, key)
    decrypted_text = vigenere_decrypt(encrypted_text, key)

    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)

    """
    print(s)
def dss():
    s = """
    import random

    p = int(input("p: "))
    q = int(input("q: "))
    x = int(input("Private_Key: "))
    M = int(input("Hashed_Message: "))

    h = random.randint(2, p - 2)
    g = int(h ** ((p - 1) / q))

    print("h:", h)
    print("g:", g)

    y = (g ** x) % p
    k = random.randint(1, q - 1)

    print("Public_Key: ", y)
    print("Random Integer: ", k)

    r = ((g ** k) % p) % q

    for i in range(1, q):
        if k * i % q == 1:
            s = (i * (M + x * r)) % q
            break

    dig_sign = [r, s]
    print("Digital_Signature: ", dig_sign)

    w = 0
    r, s = dig_sign[0], dig_sign[1]

    for i in range(2, 20):
        if (i * s) % q == 1:
            w = i
            break

    u1 = (M * w) % q
    u2 = (r * w) % q
    v = (((g ** u1) * (y ** u2)) % p) % q

    print('w:', w)
    print('u1:', u1)
    print('u2:', u2)
    print('v:', v)

    if v == r:
        print("Signature is Verified")
    else:
        print("Signature is not Verified")

    """
    print(s)
def expt_1():
    s = """
    # Write a program to check whether a given integer is odd or even

    def check(n):
        x = n^1
        if(x < n):
            print("Odd")
        else:
            print("Even")

    n = int(input())
    check(n)

    # Perform swapping between two integers and display the swapped values
    def swap(a, b):
        a = a ^ b
        b = a ^ b
        a = a ^ b
        print("", a, "\n", b)

    a, b = input().split()
    swap(int(a), int(b))

    # Write a program that contains a string (charpointer) with a value 'Hello World'.
    # The program should XOR each character in this string with 0, 127 and display the result

    def st(s):
        for i in s:
            ass = ord(i)
            print(i, "XOR 0 : ", ass ^ 0)
        for i in s:
            ass = ord(i)
            print(i, "XOR 127 : ", ass ^ 127)

    st("Hello World")

    # Prove the security feature when one-time padding operation is performed using logical XOR

    def encrypt(pt, k):
        cipher = bytearray()
        for i in range(len(pt)):
            cipher.append(pt[i] ^ k[i])
        return cipher

    def decrypt(cipher, k):
        decrypted = bytearray()
        for i in range(len(cipher)):
            decrypted.append(cipher[i] ^ k[i])
        return decrypted

    plaintext = "Hello, world"
    key = bytearray([127, 7, 4, 1, 15, 23, 90, 34, 43, 11, 12, 78])

    encrypted_data = encrypt(plaintext.encode(), key)
    print("Encrypted:", encrypted_data)

    decrypted_data = decrypt(encrypted_data, key)
    decrypted_message = decrypted_data.decode()
    print("Decrypted:", decrypted_message)

    # Analyse the frequency of matching number of bits between plain text and the key

    def count_matching_bits(text1, text2):
        count = 0
        for i in range(len(text1)):
            xor_result = text1[i] ^ text2[i]
            count += bin(xor_result).count('1')
        return count

    def main():
        plaintext = "Hello world"
        key = bytearray([0x4A, 0x12, 0x8F, 0x30, 0xAB, 0xE6, 0x59, 0x2D, 0x6F, 0x81, 0x

        if len(key) < len(plaintext):
            raise ValueError("Key length must be at least as long as plaintext")

        matching_bits_count = count_matching_bits(plaintext.encode(), key[:len(plaintext)])
        print(f"Number of matching bits: {matching_bits_count}")

    if __name__ == "__main__":
        main()

    # Analyse the frequency of matching number of bits between cipher text and the key

    def count_matching_bits(text1, text2):
        count = 0
        for i in range(len(text1)):
            xor_result = text1[i] ^ text2[i]
            count += bin(xor_result).count('1')
        return count

    def main():
        ciphertext = bytearray([0x1F, 0xDA, 0x59, 0xD6, 0x4F, 0x85, 0xBC, 0x0A, 0x12, 0
        key = bytearray([0x4A, 0xC7, 0x12, 0x8F, 0x30, 0xAB, 0xE6, 0x59, 0x2D, 0x6F, 0x

        # Ensure key length matches ciphertext length
        if len(key) < len(ciphertext):
            raise ValueError("Key length must be at least as long as ciphertext")

        matching_bits_count = count_matching_bits(ciphertext, key[:len(ciphertext)])
        print(f"Number of matching bits: {matching_bits_count}")

    if __name__ == "__main__":
        main()

    # Analyse the frequency of matching number of bits between cipher text and the plain text

    def count_matching_bits(text1, text2):
        count = 0
        for i in range(len(text1)):
            xor_result = text1[i] ^ text2[i]
            count += bin(xor_result).count('1')
        return count

    def main():
        plaintext = "Hello, world"  # The original plaintext message
        key = bytearray([0x4A, 0xC7, 0x12, 0x8F, 0x30, 0xAB, 0xE6, 0x59, 0x2D, 0x6F, 0x

        # Encrypt the plaintext
        ciphertext = encrypt(plaintext.encode(), key[:len(plaintext)])
        # Decrypt the ciphertext
        decrypted_data = decrypt(ciphertext, key[:len(plaintext)])

        matching_bits_count = count_matching_bits(decrypted_data, plaintext.encode())
        print(f"Number of matching bits between decrypted data and original plaintext: {matching_bits_count}")

    if __name__ == "__main__":
        main()

    """
    print(s)
