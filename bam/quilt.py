colo = bytes.fromhex("""
FF FF FF D3 D3 D3 A9 A9  A9 00 00 00 80 00 00 87
CE EB 00 00 FF 20 00 80  22 8B 22 32 CD 32 00 FF
FF 00 D7 FF FA E6 E6 80  00 80 CB C0 FF 2A 2A A5
FF 69 B4 FF A5 00 FF C0  CB AD D8 E6 00 80 80 F0
E6 8C 2E 8B 57 D2 B4 8C  7F FF D4 FF E4 E1 F0 80
80 98 FB 98 FF E4 C4 FF  FA CD 8A 2B E2 F4 A4 60
48 3D 8B DA 70 D6 00 BF  FF F5 F5 DC 40 E0 D0 FF
14 93 DC 14 3C 00 64 00  AD FF 2F FF 45 00 80 80
00 FF DA B9 00 FA 9A 46  82 B4 D8 BF D8 FF 63 47
4B 00 82 F0 FF FF 64 95  ED FF F5 EE 00 FF 7F F0
FF F0 FF B6 C1 77 88 99  F5 DE B3 FF A0 7A E9 96
7A 8F BC 8F 2F 4F 4F AA  B2 20 DB 70 93 00 8C FF
""")

cl = [colo[3*i:3*i+3] for i in range(len(colo)//3)]

bmp = open("quilt.bmp", "rb").read()[0x36:]
img = []
for i in range(16):
    for j in range(16):
        for k in range(64):
            if bmp[i*0xc000 + j*0x60 : i*0xc000 + j*0x60 + 3] == cl[k]: img.append(k)

order = [0]*256
for i in range(16):
    for j in range(16):
        if i & 1 == 0:
            order[(15-i)*16 + j] = img[i*16 + (15 - j)]
        else: order[(15-i)*16+j] = img[i*16+j] 

shitass = [0]*192
for i in range(64):
    v9 = (order[4*i] << 18) + (order[4*i + 1] << 12) + (order[4*i + 2] << 6) + (order[4*i + 3])
    shitass[3*i] = (v9 >> 16) & 0xff
    shitass[3*i+1] = (v9 >> 8) & 0xff
    shitass[3*i+2] = v9 & 0xff

print("".join(chr(c) for c in shitass))

