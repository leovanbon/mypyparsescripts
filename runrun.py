import itertools, struct, string

M = 0xffffffffffffffff

byte_330 = bytes.fromhex("DE AD BE EF CA FE BA BE")
byte_32C = bytes.fromhex("33 D5 F5 55 07 F8 45 17 D0 7E 23 27 4E 3C 79 EF 78")

alphabet = (
    string.ascii_letters.encode()
    + string.digits.encode()
    + b"_{}-@$!+*#%&/\\|()[]=<>?:.;,"
)

def chim(a2):
    a1 = [
        struct.unpack("<Q", struct.pack("<d", (a2[i] ^ byte_330[i]) / 256.0))[0]
        for i in range(8)
    ]

    v4 = 0x736F6D6570736575

    for i in range(8):
        v6 = (a1[i] ^ v4) & M
        v7 = ((0x9E3779B97F4A7C15 * v6) & M) ^ (((v6 << 17) | (v6 >> 47)) & M)
        v7 = ((v7 << 31) | (v7 >> 33)) & M
        v4 = (v7 ^ ((0xFF51AFD7ED558CCD * (v7 >> 33)) & M)) & M

    v14 = bytearray()
    v8 = 0

    for i in range(len(byte_32C)):
        v10 = (v8 ^ v4) & M
        v8 = (v8 + 0x6C62272E07BB0142) & M
        v11 = (0xBF58476D1CE4E5B9 * (((v10 << 13) | (v10 >> 51)) & M)) & M
        v4 = (v11 ^ (v11 >> 31)) & M
        v14.append(byte_32C[i] ^ (v4 & 0xff))

    return a2 + bytes(v14)



for guess in itertools.product(alphabet, repeat=4):
    if ord("}") in guess[:3]:
        continue

    a2 = b"HTB{" + bytes(guess)
    flag = chim(a2)

    if all(chr(c) in string.printable for c in flag):
        print(flag)