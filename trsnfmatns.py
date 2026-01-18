from pwn import xor

opts = "123423123413122123432132121243123123431232123142131342121324123241234"
rev_opts = opts[::-1]
parsed = [int(bit) for c in "DH{This_is_fake_flag_hahahaha!!}" for bit in f"{ord(c):08b}"]

cip = [i for i in open("chip", "rb").read()] 
def opt4(mes, num):
    temp = [0] * 256
    for i in range(256):
        temp[i] = mes[i] ^ cip[i+num*256]
    return temp
def opt3(mes):
    temp = [0] * 256
    for a in range(16):
        for b in range(16):
            temp[16*a + b] = mes[16*b + (15-a)]
    return temp
def opt2(mes):
    temp = [0] * 256
    for a in range(16):
        for b in range(16):
            temp[16*a+b] = mes[16*(15-a) + b]
    return temp
def opt1(mes):
    temp = [0] * 256
    for a in range(16):
        for b in range(16):
            temp[16*a+b] = mes[16*a + (15-b)]
    return temp

n = 9
for i in rev_opts:
    if i == '4':
        parsed = opt4(parsed, n)
        n = n - 1
    elif i == '3': parsed = opt3(parsed)
    elif i == '2': parsed = opt2(parsed)
    elif i == '1': parsed = opt1(parsed)

flag = ""
for m in range(32):
    cur = 0
    chunk = parsed[m*8 : (m+1)*8]
    for bit in chunk:
        cur = (cur * 2) + bit
    flag += chr(cur)
print(flag)