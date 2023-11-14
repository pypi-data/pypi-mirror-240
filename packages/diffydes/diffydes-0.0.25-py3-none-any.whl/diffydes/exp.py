def odd_even(): 
    odd_even = """
n = int(input("Enter the nubmer: "))

if n^1 == n+1: 
    print("Even")
else: 
    print("Odd")"""
    print(odd_even)


def swap(): 
    swap_num = """
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("\nBefore Swap!")
print("Num1: ", num1) 
print("Num2: ", num2) 

num1 = num1 + num2
num2 = num1 - num2 
num1 = num1 - num2

print("\nAfter Swap!")
print("Num1: ", num1) 
print("Num2: ", num2) """
    print(swap_num)


def xor_hello_world(): 
    char_pointer = """
def xor_with_value(char_pointer, value):
    result = ''.join(chr(ord(char) ^ value) for char in char_pointer)
    return result

if __name__ == "__main__":
    char_pointer = "Hello World"

    print("Original string:", char_pointer)

    xor_with_0 = xor_with_value(char_pointer, 0)
    print("XOR with 0:", xor_with_0)

    xor_with_127 = xor_with_value(char_pointer, 127)
    print("XOR with 127:", xor_with_127)"""
    print(char_pointer)


def one_time_pad(): 
    one_time_pad = """
def one_time_pad_encrypt(plaintext, key):

    ciphertext = ""
    key = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i]))
    return ciphertext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
print(f"Encrypted Text: {one_time_pad_encrypt(plaintext, key)}")
"""
    print(one_time_pad)


def frequency():
    frequency_analysis = """
def frequency_analysis(ciphertext):
    freq = {}
    for char in ciphertext:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

ciphertext = input("Enter the ciphertext: ")
print(frequency_analysis(ciphertext))"""
    print(frequency_analysis)


def affine():
    affine_cipher = """
from math import gcd

def affine_cipher_encrypt(plaintext, a, b):
    ciphertext = ""
    for char in plaintext:
        char_index = ord(char.upper()) - 65
        transformed_index = (a * char_index + b) % 26
        transformed_char = chr(transformed_index + 65)
        ciphertext += transformed_char
    return ciphertext

def affine_cipher_decrypt(ciphertext, a, b):
    plaintext = ""
    a_inverse = None

    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break

    for char in ciphertext:
        char_index = ord(char.upper()) - 65
        transformed_index = (a_inverse * (char_index - b)) % 26
        transformed_char = chr(transformed_index + 65)
        plaintext += transformed_char
    return plaintext

def check_alpha(a):
    if gcd(a, 26) == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    a = int(input("Enter value between 1 and 25 - a: "))

    while not check_alpha(a):
        a = int(input("Please try again\nEnter value between 1 and 25 - a: "))
    b = int(input("Enter value between 0 and 25 - b: "))

    ciphertext = affine_cipher_encrypt(plaintext, a, b)

    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted plaintext: {affine_cipher_decrypt(ciphertext, a, b)}")

    # Optional - formatting
    decryptedtext = affine_cipher_decrypt(ciphertext, a, b)
    trans_table = str.maketrans(decryptedtext, plaintext)
    print(decryptedtext.translate(trans_table))"""
    print(affine_cipher)


def ccipher():
    ccipher = """
def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        x = ord(char) - ord('a')
        cipher_char = chr((x + shift) % 26 + ord('a'))
        cipher_text += cipher_char
    return cipher_text

def caesar_decipher(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        x = ord(char) - ord('a')
        plain_char = chr((x - shift + 26) % 26 + ord('a'))
        plain_text += plain_char
    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    shift = int(input("Enter shift value: "))

    cipher_text = caesar_cipher(plain_text, shift)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {caesar_decipher(cipher_text, shift)}")"""
    print(ccipher)


def vernam():
    vernam_cipher = """
def vernam_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

def vernam_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ ord(key[i % len(key)]))
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    ciphertext = vernam_encrypt(plaintext, key)

    print(f"Ciphertext: {list(ciphertext)}")
    print(f"Decrypted plaintext: {vernam_decrypt(ciphertext, key)}")"""
    print(vernam_cipher) 


def vignere(): 
    vignere_cipher = """
def vigenere_cipher(plain_text, key):
    cipher_text = ""
    key = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    for idx, char in enumerate(plain_text):
        x = ord(char) - ord('a')
        k = ord(key[idx]) - ord('a')
        cipher_char = chr((x + k) % 26 + ord('a'))
        cipher_text += cipher_char
    return cipher_text

def vigenere_decipher(cipher_text, key):
    plain_text = ""
    key = (key * (len(cipher_text) // len(key) + 1))[:len(cipher_text)]
    for idx, char in enumerate(cipher_text):
        x = ord(char) - ord('a')
        k = ord(key[idx]) - ord('a')
        plain_char = chr((x - k + 26) % 26 + ord('a'))
        plain_text += plain_char
    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    key = input("Enter key: ")

    cipher_text = vigenere_cipher(plain_text, key)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {vigenere_decipher(cipher_text, key)}")
"""
    print(vignere_cipher)


def columar(): 
    columnar_cipher = """
def encrypt(message, key):
    # Remove any spaces from the message
    message = message.replace(" ", "")
    
    # Calculate the number of rows required
    rows = len(message) // len(key)
    if len(message) % len(key) != 0:
        rows += 1
    
    # Add padding to the message if necessary
    padding = len(key) - len(message) % len(key)
    message += "X" * padding
    
    # Create the matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(len(key)):
            if i * len(key) + j < len(message):
                row.append(message[i * len(key) + j])
            else:
                row.append("X")
        matrix.append(row)
    
    # Sort the key and get the column order
    sorted_key = sorted(key)
    column_order = [key.index(x) for x in sorted_key]
    
    # Build the ciphertext
    ciphertext = ""
    for i in range(len(key)):
        for j in range(rows):
            ciphertext += matrix[j][column_order.index(i)]
    
    return ciphertext

def decrypt(ciphertext, key):
    # Calculate the number of rows required
    rows = len(ciphertext) // len(key)
    
    # Create the matrix
    matrix = []
    for i in range(rows):
        row = []
        for j in range(len(key)):
            row.append("")
        matrix.append(row)
    
    # Sort the key and get the column order
    sorted_key = sorted(key)
    column_order = [key.index(x) for x in sorted_key]
    
    # Fill in the matrix
    index = 0
    for i in range(len(key)):
        for j in range(rows):
            matrix[j][column_order[i]] = ciphertext[index]
            index += 1
    
    # Build the plaintext
    plaintext = ""
    for i in range(rows):
        for j in range(len(key)):
            plaintext += matrix[i][j]
    
    # Remove any padding from the plaintext
    plaintext = plaintext.replace("X", "")
    
    return plaintext

if __name__ == "__main__":
    message = input("Enter message: ")
    key = input("Enter key: ")
    
    ciphertext = encrypt(message, key)
    
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted plaintext: {decrypt(ciphertext, key)}")"""
    print(columnar_cipher)


def railfence(): 
    railfence_cipher = """
def rail_fence_encrypt(plain_text, num_rails):
    # Create a list of empty strings for each rail
    rails = ['' for _ in range(num_rails)]

    # Distribute the characters of the plain text to the rails in a round-robin fashion
    for i, char in enumerate(plain_text):
        rails[i % num_rails] += char

    # Concatenate the rails to form the cipher text
    cipher_text = ''.join(rails)
    return cipher_text

def rail_fence_decrypt(cipher_text, num_rails):
    # Calculate the length of each rail
    rail_lengths = [len(cipher_text) // num_rails + (1 if i < len(cipher_text) % num_rails else 0) for i in range(num_rails)]

    # Distribute the characters of the cipher text to the rails
    rails = []
    start = 0
    for length in rail_lengths:
        rails.append(cipher_text[start:start+length])
        start += length

    # Collect the characters from the rails in a round-robin fashion to form the plain text
    plain_text = ''
    for i in range(len(cipher_text)):
        rail = i % num_rails
        plain_text += rails[rail][0]
        rails[rail] = rails[rail][1:]

    return plain_text

if __name__ == "__main__":
    plain_text = input("Enter plain text: ")
    num_rails = int(input("Enter number of rails: "))

    cipher_text = rail_fence_encrypt(plain_text, num_rails)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {rail_fence_decrypt(cipher_text, num_rails)}")"""
    print(railfence_cipher)


def des(): 
    symmetric_des = """
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes # pip install pycryptodome

def des_encrypt(plain_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    cipher_text = cipher.encrypt(pad(plain_text, DES.block_size))
    return cipher_text

def des_decrypt(cipher_text, key):
    cipher = DES.new(key, DES.MODE_ECB)
    plain_text = unpad(cipher.decrypt(cipher_text), DES.block_size)
    return plain_text


key = get_random_bytes(8)  # DES key - 8 bytes

plain_text = b"Hello, World!"
cipher_text = des_encrypt(plain_text, key)

print("Cipher text:", cipher_text)
print("Decrypted text:", des_decrypt(cipher_text, key))"""
    print(symmetric_des)

def rsa(): 
    asymmetric_rsa = """
import random
import math
from sympy import mod_inverse, isprime # pip install sympy

def encrypt(message, e, n):
    return (message ** e) % n

def decrypt(cipher, d, n):
    return (cipher ** d) % n


p = int(input("Enter a prime number p: "))
q = int(input("Enter another prime number q: "))

n = p * q

z = (p - 1) * (q - 1)

e = random.randint(2, z - 1)

while not isprime(e):
    e = random.randint(2, z - 1)


d = mod_inverse(e, z)

message = int(input("Enter a message [Number] "))
print()

while math.gcd(message, n) != 1:
    print("Please choose another message.")
    message = int(input("Enter a message [Number] "))

cipher_text = encrypt(message, e, n)

decrypted_message = decrypt(cipher_text, d, n)

print(f"Original Message: {message}")
print(f"Cipher Text: {cipher_text}")
print(f"Decrypted Message: {decrypted_message}")"""
    print(asymmetric_rsa)


def hellman():
    hellman = """
def diffie_hellman_key_exchange():
    # Publicly agreed upon prime number and base
    p = 23
    g = 5

    # Secret keys for Alice and Bob
    a = int(input("Enter a secret key for Alice: "))
    b = int(input("Enter a secret key for Bob: "))

    # Calculate public keys for Alice and Bob
    A = int(g ** a % p)
    B = int(g ** b % p)

    # Calculate shared secret
    K_Alice = int(B ** a % p)
    K_Bob = int(A ** b % p)

    # Verify that both parties have the same shared secret
    assert K_Alice == K_Bob, "Shared secrets are not equal"

    return K_Alice

def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        x = ord(char) - ord('a')
        cipher_char = chr((x + shift) % 26 + ord('a'))
        cipher_text += cipher_char
    return cipher_text

def caesar_decipher(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        x = ord(char) - ord('a')
        plain_char = chr((x - shift + 26) % 26 + ord('a'))
        plain_text += plain_char
    return plain_text



if _name_ == "_main_":
    plain_text = input("Enter plain text: ")

    shared_secret = diffie_hellman_key_exchange()
    shift = shared_secret % 26

    cipher_text = caesar_cipher(plain_text, shift)

    print(f"Cipher text: {cipher_text}")
    print(f"Decrypted plain text: {caesar_decipher(cipher_text, shift)}")"""
    print(hellman)


def dss(): 
    signature_dss = """
from cryptography.hazmat.backends import default_backend # pip install cryptography
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization

def generate_key_pair():
    private_key = dsa.generate_private_key(
        key_size=1024,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode('utf-8'),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode('utf-8'),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False

if __name__ == "__main__":
    private_key, public_key = generate_key_pair()     # Generate key pair

    message = "Hello, this is a test message." # Message to be signed

    signature = sign_message(private_key, message) # Sign the message

    if verify_signature(public_key, message, signature): # Verify the signature
        print("Signature is valid.")
    else:
        print("Signature is not valid.")"""
    print(signature_dss)


def playfair():
    playfair_cipher = """
!pip install FamousCipherAlgorithms

import FamousCipherAlgorithms as FCA
from  FamousCipherAlgorithms import Playfair

msg = "Hello World"
key = "Key"

cipher = Playfair(key)
encryption = cipher.encrypt(msg)
print(f"Cipher Text : {encryption}")

decryption = cipher.decrypt(encryption)
print(f"Plain Text : {decryption}")

print(*cipher.coder_table,sep="\n")"""
    print(playfair_cipher)


def dir(): 
    print("Odd or Even - odd_even()")
    print("Swapping numbers - swap()")
    print("XOR Character String - xor_hello_world()")
    print("Security Feature using One time padding - one_time_pad()")
    print("Frequency Analysis - frequency()")
    print("Affine Cipher - affine()")
    print("Caesar Cipher - ccipher()")
    print("Vernam Cipher - vernam()")
    print("Vignere Cipher - vignere()")
    print("Columnar Cipher - columnar()")
    print("RailFence Cipher - railfence()")
    print("Symmetric Cipher DES - des()")
    print("Asymmetric Cipher RSA - rsa()")
    print("Diffie Hellman cipher - hellman()")
    print("Digital Signature Standards DSS - dss()")
    print("PlayFair Cipher - playfair()")