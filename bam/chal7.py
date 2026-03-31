def ror4(x, n): return ((x >> n) | (x << (32-n))) & 0xFFFFFFFF
def rol4(x, n): return ((x << n) | (x >> (32-n))) & 0xFFFFFFFF

expected_v18 = {}
for i in range(0, 8):   expected_v18[i] = (0x2b48b515d43f4140 >> (i*8)) & 0xFF
for i in range(8, 16):  expected_v18[i] = (0x35bcb75507c270f7 >> ((i-8)*8)) & 0xFF
for i in range(16, 24): expected_v18[i] = (0x841e959c29c8f1e7 >> ((i-16)*8)) & 0xFF
for i in range(24, 32): expected_v18[i] = (0x1e7c68fc9ce020c2 >> ((i-24)*8)) & 0xFF
for i in range(32, 37): expected_v18[i] = (0x000000daf7d998de >> ((i-32)*8)) & 0xFF
expected = [expected_v18[i] for i in range(37)]

v6 = 0x1337c0de ^ 0xc0def00d
v10 = 0; v9 = 0
flag_chars = []; all_ok = True

for i in range(37):
    tmp = (v6 + v10 - 0x61c88647) & 0xFFFFFFFF
    next_v6 = (rol4(tmp, 5) ^ ror4(tmp, 3)) & 0xFFFFFFFF
    
    r10d = (next_v6 >> 8) & 0xFFFFFFFF
    ecx_add = (((next_v6 >> 16) & 0xFFFFFFFF) + v9) & 0xFF
    A = (i*17 ^ next_v6 ^ r10d) & 0xFF
    needed = (expected[i] - ecx_add) & 0xFF

    flag_chars.append((A ^ needed) & 0xFF)
    
    v6 = next_v6
    v10 = (v10 + 0x45d9f3b) & 0xFFFFFFFF
    v9 = (v9 + 0xb) & 0xFFFFFFFF

flag_inner = ''.join(chr(c) for c in flag_chars)
print(f"gigem{{{flag_inner}}}")

