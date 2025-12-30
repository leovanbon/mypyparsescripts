import re
from pwn import *

p = remote("host8.dreamhack.games", 10620)

for i in range(10):
    p.recvuntil(b']:')
    monster = p.recvuntil(b'Cast your spell!: ').decode()

    in4 = [int(s) for s in re.findall(r'\d+', monster)]
    print(in4)
    by=0
    for j in [0,6,5,4,3,2,1]:
        by = by + in4[j]
        by = by << 8
    by = by >> 8
    spell = ""

    for chr in f"{by:b}":
        if chr == '1': spell = spell + 'A'
        spell = spell + 'B'

    spell = spell[:-1]

    print(spell)
    p.sendline(spell.encode())

p.interactive()
