from pwn import xor

key = [0x88, 0x66, 0x44, 0x11, 0x77, 0x55, 0x22, 0x33]
ciphe = bytes.fromhex("220c6a33204455fb390074013c4156d704316528205156d70b217c14255b6ce10837651234464e")
roll = (8 - (len(ciphe) % 8)) % 8

print(xor(ciphe, key[roll:] + key[:roll]))


