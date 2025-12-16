from pwn import *

name = "khanh"
nem = bytes(name, 'utf-8')
lem = 5

ketamin = "a5 90 07 7f 0a 10 c9 ae a3 86 24 16 02 97 28 51 54 fb 08 1f 27 75 09 a7 e2 d5 b4 bb 1b f8 33 50 81 5f ef 0e 6f 2e 55 ab 4e e1 ee 40 8c d3 9c c5 9b b7 dc 7d 80 c2 45 99 30 89 dd 04 5d 41 e7 21 67 44 69 47 32 8b 2c d1 a0 5b b9 bd 84 78 cb 4f b6 13 1d ea be 15 8f 3a 18 98 3c e4 cc ac 4b df 9d 3d 6e 31 06 7a d8 95 b2 38 1c 6b a9 62 7e f7 60 5c 36 0c b0 9a ca d4 35 63 52 b1 a4 3e 0b 82 96 68 e5 6a d6 d2 f4 aa cd 1a 7b 91 e6 6c da 94 d0 56 f1 bc 4a 2a 19 01 c8 43 c4 1e 39 3f e9 fc 4d ce 00 c7 f5 eb f9 8e 93 c1 9f 22 87 70 23 b8 ff a1 d9 db 46 f0 c6 05 57 26 a6 17 59 c0 fd 88 53 5a 2b e8 2f 9e 49 11 de b3 4c 66 e0 34 8a 0d 20 ad fe 76 6d ed 12 ba 74 c3 64 bf 25 f3 29 71 e3 a2 b5 85 f2 af 58 fa 7c 5e 65 61 14 92 a8 3b 03 8d 42 2d 72 77 83 79 d7 73 f6 0f 48 ec cf 37"
ke = ketamin.split()
kem = bytearray([int(hexval, 16) for hexval in ke])


def fun1(name, len):
	for idx in range(256):
		kem[idx] = kem[idx] ^ name[idx % len]
		kem[idx] = ((kem[idx] << 4) + (kem[idx] >> 4)) % 256

fun1(nem,5)

def i_know_you(round):
	idx = (round * lem) % 0x100
	return (kem[idx] + 1) % 3

def main():
	host = "host8.dreamhack.games"
	port = 9978
	p = remote(host,port)
	p.sendlineafter(b"Enter name(4~20): ", nem)
	for i in range(100):
		print(i_know_you(i))
		p.sendlineafter(b"me: ", str(i_know_you(i)).encode())
	
	p.interactive()

if __name__ == "__main__":
	main()