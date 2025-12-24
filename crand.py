import ctypes
libc = ctypes.CDLL("libc.so.6")
libc.srand(0xbeef)

with open("flag.bmp.enc", 'rb') as data, open("flag.bmp", 'wb') as flag:
    i = 0
    while(True):
        cur = data.read(1)
        if (not cur): break
        curr_by = int.from_bytes(cur)
        r = libc.rand() % 256

        if i % 3 == 2:
            dec = (curr_by + 0x18) ^ r
        elif i % 3 == 0:
            dec = ((curr_by >> 4 | curr_by << 4) - r) % 256
            dec = dec >> 1 | dec << 7
        else:
            r = r % 8
            dec = curr_by << r | curr_by >> (8-r)

        flag.write(bytes([dec % 256]))
        i = i + 1
        