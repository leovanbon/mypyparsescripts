from math import sqrt
from pwn import *
from functools import cmp_to_key

def cal(a):
    return (1- (a[1] + a[2] + a[0])/ (sqrt(3) * sqrt(a[1]*a[1] + a[0]*a[0] + a[2]*a[2])))

def compar(a,b):
    x = cal(a)
    y = cal(b)

    if x<y: return -1
    elif x>y: return 1
    else: return 0

r = remote('host8.dreamhack.games', 15703)
data = r.recvuntil(b'Result?').decode()
arr = [list(map(int, line.split(':')[1].split())) + [int(line.split(':')[0])] for line in data.splitlines() if ':' in line and line.split(':')[0].strip().isdigit()]
sor = sorted(arr, key=cmp_to_key(compar))
payload = " ".join(str(a[3]) for a in sor)
r.sendline(payload.encode())
r.interactive()