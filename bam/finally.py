import hashlib, hmac
from pwn import xor

sugar = bytes.fromhex("4C18217E0A6B2D72334F5561102A3C19")[::-1]

exe_bytes = open("cloudsync", "rb").read()
self_has = hashlib.sha256(exe_bytes).digest()

serial = b'ROUTER-61AAE6FC6A83FD56'
first_dish = hashlib.sha256(serial + sugar + self_has).digest()


dat = open("backup.dat", "rb").read()
ntwice = dat[5 : 0x15]
tag = dat[0x40:]

assert hmac.new(first_dish, dat[5:0x19+39], hashlib.sha256).digest() == tag, "HMAC not ok"
print("HMAC ok")


skibidi = dat[0x19 : 0x19 + 39]
bo_pi_xi = hashlib.sha256(first_dish[:16] + ntwice + b'\x00\x00\x00\x00').digest()
bo_pi_xi += hashlib.sha256(first_dish[:16] + ntwice + b'\x01\x00\x00\x00').digest()
print(xor(skibidi, bo_pi_xi))
