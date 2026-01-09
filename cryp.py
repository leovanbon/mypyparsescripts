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


from Crypto.Cipher import AES

key = bytes.fromhex("")
iv = bytes(16)

s = AES.new(key, AES.MODE_CBC, iv).decrypt(open("out.txt", "rb").read())

print(s.split(b"\00", 1)[0])