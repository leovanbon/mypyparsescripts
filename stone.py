from unicorn import Uc, UC_ARCH_ARM, UC_MODE_ARM
from unicorn.arm_const import UC_ARM_REG_R0, UC_ARM_REG_R1, UC_ARM_REG_R2
from pwn import *

HOST = "154.57.164.79"
PORT = 32517

r = remote(HOST, PORT)

for i in range(1, 51):
    print(f"--- Solving Level {i}/50 ---")
    
    r.recvuntil(b'/50: ')
    
    hex_data = r.recvuntil(b'Register r0:', drop=True).strip()
    
    binary_code = binascii.unhexlify(hex_data)

    ADDRESS = 0x10000 
    mu = Uc(UC_ARCH_ARM, UC_MODE_ARM)
    mu.mem_map(ADDRESS, 2 * 1024 * 1024)
    mu.mem_write(ADDRESS, binary_code)

    mu.emu_start(ADDRESS, ADDRESS + len(binary_code))

    r0 = mu.reg_read(UC_ARM_REG_R0)
    print(f"Result r0: {r0} (0x{r0:08x})")

    r.sendline(str(r0).encode())

r.interactive()