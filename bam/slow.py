f = open("main", "rb").read()
arr = f[0x3020:0x3020 + 100000*4]

def check_var(a1):
    return ((a1 >> 25) | (a1 >> 9) & 0xFF80 | (a1 << 6) & 0x3F0000 | (a1 << 22)) & 0xFFFFFFFF 

import struct
a = list(struct.unpack(f'<{len(arr)//4}I', bytes(arr)))
a.sort(key=check_var)
brr = bytearray(struct.pack(f'<{len(a)}I', *a))

open("patched", 'wb').write(f[:0x15b0] + b'\x90'*0xf + f[0x15bf:0x3020] + bytes(brr) + f[0x176a0*4:])

from pwn import *
p = process("./patched")
print(p.recvline_contains(b"Flag is"))