import re
year = 2025; month = 12; day = 30

def pick(chrs, lock):
    if lock == 0: return ("".join(c for i in range(8) for c in chrs if (ord(c) % 32) % 4 == 0 and (ord(c) % 32) // 4 == i))
    elif lock == 1: return ("".join(c for i in [(year>>10) & 0x1f, (year>>5) & 0x1f, year & 0x1f, month, day] for c in chrs if ord(c) % 32 == i))
    elif lock == 2:
        kay = []
        for j in range(1,33):
            s = j*j
            if str(s) == str(s)[::-1] and s >= 10: kay.extend([(s//32) % 32, s % 32])
            if len(kay) >= 6: break
        return ("".join(c for i in kay for c in chrs if ord(c) % 32 == i))
    
    else: return ("".join(c for i in (lambda x: [int(x[i:i+5], 2) for i in range(0, len(x), 5)])("".join(f"{ord(c):08b}" for c in "Rootsquare")) for c in chrs if ord(c) % 32 == i))


for j in range(4):
    lines = [re.findall(r'\| (.*) \|', input()) for i in range(4)]
    keys = [key for l in lines for li in l for key in li.split()]
    print(pick(keys, j))

