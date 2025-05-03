#symetric xor enctryption fuctions
def xor_encrypt(text, key):
    encrypted = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    return encrypted

def xor_decrypt(encrypted_text, key):
    return xor_encrypt(encrypted_text, key)
