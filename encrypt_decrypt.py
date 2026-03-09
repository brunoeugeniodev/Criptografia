import os

BLOCK_SIZE = 16


# -------------------------
# PKCS7 PADDING
# -------------------------
def pkcs7_pad(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    padding = bytes([pad_len] * pad_len)
    return data + padding


def pkcs7_unpad(data):
    pad_len = data[-1]
    return data[:-pad_len]


# -------------------------
# KEY EXPANSION
# -------------------------
def expand_key(key):
    key = key.encode()

    if len(key) < BLOCK_SIZE:
        key = key.ljust(BLOCK_SIZE, b'\0')

    return key[:BLOCK_SIZE]


# -------------------------
# SIMPLE SBOX
# -------------------------
SBOX = [(i * 7) % 256 for i in range(256)]
INV_SBOX = [0]*256
for i,v in enumerate(SBOX):
    INV_SBOX[v] = i


# -------------------------
# BLOCK OPERATIONS
# -------------------------
def sub_bytes(block):
    return bytes([SBOX[b] for b in block])


def inv_sub_bytes(block):
    return bytes([INV_SBOX[b] for b in block])


def shift_rows(block):
    b = list(block)
    return bytes([
        b[0], b[5], b[10], b[15],
        b[4], b[9], b[14], b[3],
        b[8], b[13], b[2], b[7],
        b[12], b[1], b[6], b[11]
    ])


def inv_shift_rows(block):
    b = list(block)
    return bytes([
        b[0], b[13], b[10], b[7],
        b[4], b[1], b[14], b[11],
        b[8], b[5], b[2], b[15],
        b[12], b[9], b[6], b[3]
    ])


def xor_bytes(a, b):
    return bytes(i ^ j for i, j in zip(a, b))


# -------------------------
# ENCRYPT BLOCK
# -------------------------
def encrypt_block(block, key):

    state = xor_bytes(block, key)

    for _ in range(10):

        state = sub_bytes(state)
        state = shift_rows(state)
        state = xor_bytes(state, key)

    return state


# -------------------------
# DECRYPT BLOCK
# -------------------------
def decrypt_block(block, key):

    state = block

    for _ in range(10):

        state = xor_bytes(state, key)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)

    state = xor_bytes(state, key)

    return state


# -------------------------
# FILE ENCRYPTION
# -------------------------
def encrypt_file(input_file, output_file, key):

    key = expand_key(key)

    with open(input_file, "rb") as f:
        data = f.read()

    data = pkcs7_pad(data)

    encrypted = b''

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]
        encrypted += encrypt_block(block, key)

    with open(output_file, "wb") as f:
        f.write(encrypted)


# -------------------------
# FILE DECRYPTION
# -------------------------
def decrypt_file(input_file, output_file, key):

    key = expand_key(key)

    with open(input_file, "rb") as f:
        data = f.read()

    decrypted = b''

    for i in range(0, len(data), BLOCK_SIZE):

        block = data[i:i+BLOCK_SIZE]
        decrypted += decrypt_block(block, key)

    decrypted = pkcs7_unpad(decrypted)

    with open(output_file, "wb") as f:
        f.write(decrypted)


# -------------------------
# CLI
# -------------------------
def main():

    print("1 - Encrypt File")
    print("2 - Decrypt File")

    choice = input("Choice: ")

    key = input("Key: ")
    input_file = input("Input file: ")
    output_file = input("Output file: ")

    if choice == "1":
        encrypt_file(input_file, output_file, key)
        print("File encrypted successfully!")

    elif choice == "2":
        decrypt_file(input_file, output_file, key)
        print("File decrypted successfully!")

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()