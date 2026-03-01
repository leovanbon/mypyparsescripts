import ctypes
libc = ctypes.CDLL("libc.so.6")
libc.srand(1909094399)

print(libc.rand())
print(libc.rand())

#1917

