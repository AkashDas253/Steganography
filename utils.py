
def xor_encrypt_decrypt(text, key):
    """Encrypts or decrypts text using XOR with the given key."""
    key_length = len(key)
    return ''.join(chr(ord(text[i]) ^ ord(key[i % key_length])) for i in range(len(text)))
