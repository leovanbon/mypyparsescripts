# import sys
# from primePy import primes
# from Crypto.Util.number import inverse

# def decr(cipher, expo_key, mod):
#     print("fuck you")

#     with open(cipher, "rb") as cip:
#         c = cip.read()
    
#     for i in range(0, len(c), 8):
#         chunk = c[i: i+4]
#         pie = int.from_bytes(chunk, 'little')
#         flan = pow(pie, expo_key, mod)
#         print(flan.to_bytes(4, 'little').decode('utf-8', 'ignore'), end="")


# n1 = 4271010253
# p = (primes.factor(n1))
# q = n1//p
# phi = (p-1)*(q-1)
# n2 = 201326609
# decr("out.bin", inverse(n2,phi), n1)


# from Crypto.Cipher import AES

# key = bytes.fromhex("")
# iv = bytes(16)

# s = AES.new(key, AES.MODE_CBC, iv).decrypt(open("out.txt", "rb").read())

# print(s.split(b"\00", 1)[0])

# d = open('flag.enc' , 'rb').read()

# S, k, j = list(range(256)), d[-9:-1], 0
# for i in range(256):
#     j = (j + S[i] + k[i % 8]) % 256
#     S[i], S[j] = S[j], S[i]

# i = j = 0
# shit = bytearray()
# for b in d[:-13]:
#     i = (i + 1) % 256
#     j = (j + S[i]) % 256
#     S[i], S[j] = S[j], S[i]
#     shit.append(b ^ S[(S[i] + S[j]) % 256])

# print(shit)


# c = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# cipher = bytes.fromhex(c)

# from pwn import xor
# print(xor(cipher, b'myXORkey'))

# from hashlib import sha256
# from pathlib import Path
# from Crypto.Cipher import ARC4

# key = sha256(b"NEX0_Nexo").digest()
# ct = Path("flag.txt.emilia").read_bytes()

# pt = ARC4.new(key).decrypt(ct)
# print(pt.decode())

import base64, hashlib, itertools, string
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

data = base64.b64decode("""IlMxcfhkeRpZ6KtOd98d5Ag4BvoLStiOPGB1jrpVUyQZrs+ackvBlQMqrkdGz+AmiBV0k0T5cSBSxnsmpirMPCT6pgED2HpSI+suNmZcoC45/fGFDOYftTXv+ne8iqxa7YRzHF/cP+I6F5Ca3sDkok83e7KCVf3Z/NIWcallMv+kB0rNtMBBgNwEOBOgP6CScHZbAHd1e5W6ZJlhQpXGllBXe/VXTZuJqvKtaiIDWamMetVJqJRxggAhpplD5HwQ0rvnmrkiWABRjC+vf/6xDrMBQpMWPJDNTDsLecAG/T4MM4n//Vz84bQjGhgSsbVTYT8L5uhr2Zh+A7dfv29P2NuqqU0slSLmym+/r1zdiG3Hast1wDpx3FCvaf+PDcIjQR1B2FmpkRqwYsvX3bl8kfoc5XPhPMdQi8OxyxlCPUPixUTlhqi4kOsKHXOElfS6uWMMUtWgjj3A7lo7RKis9c8OZxRUsbjcHM1R46FscOcE3ABVCZ2/+iH09d2dwmhSwnYh3fFSkqY5rhsP/bcBqlr6y0Rvfquoa4XVrfxhXHmBb60GzdMKASCRHLiCv+IUet6IBfKSaD0UmGxwTxzPGgmplAp9NDj43p3zXrRIyQ9AzRcmgAJMM/Ixi4ya/gCeYL90Ous5PBfhDoHJZzrRqj7uU8hw0Vnw6apcVaLTWnGiU0ENE+g1pkHVqcvyR2RqhvceRtxHA7m1quw2UVdZI3CIG/g38Kd0wjw5DxHNJUSqvY5Wo+svxzeZgqsMMbFcIfqPi13G7F9IeGbhs/06Dje3ZvaDCADId9llt4cdIJdS+cjuqDc9NDwKR3+s+ab06P0f/yYYzKOGa16stv97xrs+VmJoS6xxksOL+cKiW6KJyepfcZAfJ4EIStVjj3RWVBIEtg8T2jWiXpuDmdlutwmB3ZTRHm++v5bIoaCv4JCDS0ns/oxkPEaja9qQwfIUYHLJEyB0lYjLhOPwZEJ7DZuQmPatqM4/QPwT7wvqWteYDaXoR6ZVbNFseXQBa9cqadCcktXzTC5I1YwBBTs1b/lc98wGI3pV+94038GyuRAINOuKKkid/RFtNSKjanws/Z6zm5KzsUrWu8eseSmZ0Jd7ii5rSct+HDNeCW9LLZLV/oBz0KyXk4KUcE87HB15qNvrbQD4UfzU1jGLHUz/TRoXF4CBvpKBWZ+jdCfoTU9I2biNcmzmG6YnN7NoZgUjj5KGmvhQEy0QyAKWgXSC2M4GsF0Go7+2Q60lttifG0qkF1KzM7BkjOtzwmZz1IbWGKGiSC9uxg6uU1EEU2cJHhvcuJxDOljYmcEcN3+KWYQxA29LEs+N9sALd5GwlKQp9KkMeDLvmRrY/kbMkSz7kOKJ5SEAE5KgCVgbwmvQPQz5Zivcdy8uRHRfvkYzw+ixChLtkoDxG4a5OkpuuyMjC3vh+lu0A4qoHeMUuek5YFvJKhxHBT2U+tBAhuHNLaBdsxhDN4rukqLe3eFIpc9iwXmPtsOes1ukmuv8b90eY5ljOlyhti8CppcwKOIqA1ENB5hcCIR4G802rGu4Abzg7/wauG1zqINq4y9/lmIAao7RXWZfVHuuAGC7FTQ0/mHZwp0XL5d01jQgT5VdxJcXmmuZiCB51VVkC1GKd3ZnVngmchK5jHjkm+BFWPJ89vBqeFgfX6CAxHQEGq4/kgkhd7r3DJIe6y0eVDePrPuIJSArr0njKIORxiTa1JWf/qwWNBCnFc6lBsvHhTnDLLNpzQ==
""")
iv = bytes(range(16))
expected = "f2571e71a503a7ff80a7a603ce0c1965"

for x in itertools.product(string.ascii_lowercase, repeat=4):
    word = ''.join(x)
    key = hashlib.sha256(word.encode()).digest()[:16]

    try:
        plain = unpad(AES.new(key, AES.MODE_CBC, iv).decrypt(data), 16).decode()

        if hashlib.md5(plain.encode()).hexdigest() == expected:
            print("Key word:", word)
            print(base64.b64decode(plain).decode())
            break
    except (ValueError, UnicodeDecodeError):
        pass