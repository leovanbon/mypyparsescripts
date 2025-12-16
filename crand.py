import ctypes
from pwn import *

libc = ctypes.CDLL("libc.so.6")
libc.srand(0xbeef)

for i in range(5):
    print(libc.rand())