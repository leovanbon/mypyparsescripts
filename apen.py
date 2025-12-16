lo = "ad d8 cb cb 9d 97 cb c4 92 a1 d2 d7 d2 d6 a8 a5 dc c7 ad a3 a1 98 4c"
LO = lo.split()
cip = [int(h,16) for h in LO]

flat = 0

print(len(cip)) #23
a = -1
for i in range(23):
    a = a * (-1)
    flat += a * cip[i]

for i in range(0,23,1):
    print(chr(flat), end = "")
    flat = flat - cip[i]
    flat = flat * (-1)

# cn-1 - cn = 
    
"""
flat = bytes(flag)
print(flat)
"""