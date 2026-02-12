import struct
from pwn import xor

#cip = "C@qpl==Bppl@<=pG<>@l>@Blsp<@l@AArqmGr=B@A>q@@B=GEsmC@ArBmAGlA=@q"
#print(''.join([chr(((b ^ 3) - 13) % 128) for b in bytearray(cip.encode('utf-8'))[::-1]]))

# cip = bytes.fromhex("f8 e0 e6 9e 7f 32 68 31 05 dc a1 aa aa 09 b3 d8 41 f0 36 8c ce c7 ac 66 91 4c 32 ff 05 e0 d9 91")
# print(xor(bytes([(x + 0x3b) & 0xFF for x in xor(bytes( [(y + 0x5a) & 0xFF for y in xor(cip, b'\x11\x33\x55\x77\x99\xbb\xdd')] ), b'\xef\xbe\xad\xde')]), b'\xde\xad\xbe\xef')  )

#  = bytearray.fromhex("52 df b3 60 f1 8b 1c b5 57 d1 9f 38 4b 29 d9 26 7f c9 a3 e9 53 18 4f b8 6a cb 87 58 5b 39 1e")
# print(bytes([((x >> (i % 8)) | (x << (8 - (i % 8)))) & 0xff for i, x in enumerate( xor(c[:0x1e], bytes(range(0x1e))) )]))

# c = b'\x74\x78\x4b\x65\x77\x48\x5c\x69\x68\x7e\x5c\x79\x77\x62\x46\x79\x77\x05\x46\x54\x73\x72\x59\x69\x68\x7e\x5c\x7e\x5a\x61\x57\x6a\x77\x66\x5a\x52\x02\x62\x5c\x79\x77\x5c\x00\x7c\x57\x0d\x0d\x4d'
# print(xor(c,len(c)))

# c = b'\x6f\x0d\x6e\x80\x10\x22\xf4\x70\xd5\x52\x83\x74\x25\x16\x47\x38'
# print(bytes([((((b-i)^ 0x5a) >> 4 | ((b-i)^ 0x5a) << 4)) & 0xff for i, b in enumerate(c)]))


# data = bytes.fromhex("""
# 39 00 00 00 9B FF FF FF 2C 00 00 00 C6 00 00 00
# 59 00 00 00 58 00 00 00 39 00 00 00 AB 00 00 00
# CE FF FF FF C6 00 00 00 8C 01 00 00 90 01 00 00
# DA FF FF FF 73 00 00 00 52 00 00 00 66 00 00 00
# """.replace('\n', '').replace(' ', ''))
# values = list(struct.unpack(f'<{len(data)//4}i', data))


# key = [0x88, 0x66, 0x44, 0x11, 0x77, 0x55, 0x22, 0x33]
# ciphe = bytes.fromhex("220c6a33204455fb390074013c4156d704316528205156d70b217c14255b6ce10837651234464e")
# roll = (8 - (len(ciphe) % 8)) % 8
# print(xor(ciphe, key[roll:] + key[:roll]))


# data= """
# 39 00 00 00 9B FF FF FF 2C 00 00 00 C6 00 00 00
# 59 00 00 00 58 00 00 00 39 00 00 00 AB 00 00 00
# CE FF FF FF C6 00 00 00 8C 01 00 00 90 01 00 00
# DA FF FF FF 73 00 00 00 52 00 00 00 66 00 00 00
# AB FF FF FF AF FF FF FF  D9 FF FF FF AD FF FF FF
# AE FF FF FF B0 FF FF FF  B2 FF FF FF E0 FF FF FF
# E2 FF FF FF E1 FF FF FF  4F 00 00 00 53 00 00 00
# 4C 00 00 00 53 00 00 00  4F 00 00 00 57 00 00 00
# 83 00 00 00 54 00 00 00  59 00 00 00 87 00 00 00
# 0C 00 00 00 13 00 00 00  3E 00 00 00 3B 00 00 00
# 3E 00 00 00 39 00 00 00  3A 00 00 00 38 00 00 00
# 0D 00 00 00 34 00 00 00  58 09 00 00 2E 09 00 00
# 20 0A 00 00 F3 12 00 00  F0 0A 00 00 52 14 00 00
# 94 0B 00 00 B4 14 00 00  56 0A 00 00 9A 0B 00 00
# 63 00 00 00 5F 00 00 00  8F 00 00 00 59 00 00 00
# 8C 00 00 00 89 00 00 00  8C 00 00 00 55 00 00 00
# """

# r = ([int.from_bytes(bytes.fromhex(data.replace('\n','').replace(' ',''))[i:i+4], 'little', signed=True) for i in range(0, len(bytes.fromhex(data.replace('\n','').replace(' ',''))), 4)])

# print(len(r))

# s = "" + chr(r[0]-9) + chr(-r[1]-1) + chr(r[2]+4) + chr(r[3]//2) + chr(r[4]-34) + chr(r[5]-40) + chr(r[6]+40) + chr(r[7]//3) + chr(-r[8]-1) + chr(r[9]//2) + chr(r[10]//4) + chr(r[11]//4) + chr(19-r[12]) + chr(r[13]-17) + chr(r[14]-30) + chr(r[15]) + ("".join(chr(-r[i]-1+i) for i in range(16,26))) + ("".join(chr(r[i]-i) for i in range(26,36))) + ("".join(chr(r[i]+i) for i in range(36,46))) + ("".join(chr(r[i]//i) for i in range(46,56))) + ("".join(chr(r[i]-100+i) for i in range(56,64)))

# enc = bytearray(b'\xae\x00\x00\x00\x6d\x00\x00\x00\x9b\x00\x00\x00\x92\x00\x00\x00\x13\x00\x00\x00\x2b\x00\x00\x00\xc6\x00\x00\x00\xc9\x00\x00\x00\xe5\x00\x00\x00\xfa\x00\x00\x00\x96\x00\x00\x00\x0b\x00\x00\x00\x64\x00\x00\x00\x31\x00\x00\x00\xb8\x00\x00\x00\x08\x00\x00\x00\xc8\x00\x00\x00\x48\x00\x00\x00\xd2\x00\x00\x00\x30\x00\x00\x00\x60\x00\x00\x00\x04\x00\x00\x00\xfa\x00\x00\x00\x7b\x00\x00\x00\x88\x00\x00\x00\xb0\x00\x00\x00\x2f\x00\x00\x00\x7c\x00\x00\x00\xb3\x00\x00\x00\xb3\x00\x00\x00\x58\x00\x00\x00\x61\x00\x00\x00')
# def shufflelelele(b):
#     crab_map = [1, 3, 6 , 0, 2, 7, 5, 4]
#     return sum((((((b - 0x22) & 0xff) ^ 99) >> i) & 1) << crab_map[i] for i in range(8))

# print(''.join(f"{shufflelelele(b):02x}" for b in enc[::4]))


# print((lambda x: [int(x[i:i+5], 2) for i in range(0, len(x), 5)])("".join(f"{bin(ord(c))[2:]}" for c in "Rootsquare")))

# little endian 
# print("".join([bytes.fromhex(f"{c:x}")[::-1].decode() for c in hehex]))


# one liner techniques so far:
# print("".join(some_generator))
# print(bytes([some_generator]))
# print((lambda x: something_with_x)(define_x))


# c = "Deim(yobzoRoA`m\u0089`ESf;xmOkh ]g}8VjFw[x-tG\u008dlaVCr"
# key=[-11, 34, -28, -8, -57, -8, 2, 3, 5, -17, -13, -18, -53, -5, 0, 3, -19, -16, -12, -6, -48, 10, 7, -19, -4, -1, -67, -19, -15, 9, -47, -14, -8, -27, 3, -19, 3, -59, 5, -30, 8, 33, 22, -6, -50, 0]
# c1 = [ord(c[i]) - key[i] for i in range(46)]
# c2 = c1[-2:] + c1[16:-2] + c1[:16]
# c3 = [0]*46
# for i in range(46):
#     if i % 3 == 1: c3[i] = c2[i]
#     else: c3[i] = c2[i] - (i//3)
# c4 = c3[-19:] + c3[:-19]
# print("".join([chr(x%256) for x in c4]))

# flag = [0]*28
# cip = bytearray.fromhex("636A7264625A76126D62116C127E75117E731277127372120000005C")
# key = [ord(c) for c in "BKSEC{CHAO_MUN9_D3N_R3V3RS3!!!}`"]
# for i in range(len(flag)):
#     for j in range(len(key)): #32
#         cip[i] = cip[i] ^ key[-j-1]
# print(cip)

print(hex(1234))

1909094399