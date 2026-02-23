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

d = open('flag.enc' , 'rb').read()

S, k, j = list(range(256)), d[-9:-1], 0
for i in range(256):
    j = (j + S[i] + k[i % 8]) % 256
    S[i], S[j] = S[j], S[i]

i = j = 0
shit = bytearray()
for b in d[:-13]:
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    shit.append(b ^ S[(S[i] + S[j]) % 256])

print(shit)

