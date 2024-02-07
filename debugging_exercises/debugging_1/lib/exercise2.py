print("ENCODING:")
def encode(text, key):
    cipher = make_cipher(key)
    print(f"* This is the cipher: {cipher}")
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
    print(f"* This is ciphered char: {ciphered_char}")
    print(f"* This is ciphertext char list: {ciphertext_chars}")
    result = "".join(ciphertext_chars)
    print(f"This is the encoded result: {result}")

    return "".join(ciphertext_chars)

print("DECODING:")
def decode(encrypted, key):
    cipher = make_cipher(key)
    print(f" * This is the cipher: {cipher}")
    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        plaintext_chars.append(plain_char)
    print(f"* This is the plain char list: {plain_char}")
    print(f"* This is the plaintext char list: {plaintext_chars}")
    result = "".join(plaintext_chars)
    print(result)
    return "".join(plaintext_chars)

print("MAKING THE CIPHER:")
def make_cipher(key):
    print(f"* This is the key: {key}")
    print(f"* This is the key in list form: {list(key)}")
    alphabet = [chr(i + 97) for i in range(0,26)]
    print(f"* This should present a list of the alphabet: {alphabet}")
    cipher_with_duplicates = list(key) + alphabet
    print(f"* This presents a list of the key and the alphabet: {cipher_with_duplicates}")

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])
    print(f"* This is the range: {range(0, len(cipher_with_duplicates))}")
    print(f"* This is the cipher: {cipher}")
    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")

