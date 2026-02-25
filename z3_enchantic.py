from z3 import *

# s = Solver()
# x = [Int(f'x_{i}') for i in range(12)]
# targets = [-4, 11, 8, 10, 31, 0, 28, 4, 1, 25, 10, 11]

# s.add(x[0] * x[1] - 2 * x[2] == targets[0])
# s.add(x[1] + 5 * x[2] - 3 * x[3] == targets[1])
# s.add(x[2] + x[3] * x[4] - x[0] == targets[2])
# s.add(x[5] + 2 * x[4] + x[2] == targets[3])
# s.add(20 * x[1] - 2 * x[2] - x[4] == targets[4])
# s.add(x[2] + x[5] - 2 * x[1] == targets[5])
# s.add(2 * x[1] + x[2] + 3 * x[6] + 4 * x[7] == targets[6])
# s.add(5 * x[5] - x[7] - x[8] + 2 * x[9] == targets[7])
# s.add(3 * x[8] + 2 * x[9] + 4 * x[10] - 3 * x[6] == targets[8])
# s.add(9 * x[11] + 2 * x[10] - x[8] == targets[9])
# s.add(4 * x[7] - x[8] + x[10] == targets[10])
# s.add((x[3] ** x[8]) + 3 * x[11] - 2 * x[7] + x[6] + x[5] + x[10] == targets[11])

# for i in range(12):
#     s.add(x[i] >= 0)
#     s.add(x[i] <= 999)

# if s.check() == sat:
#     m = s.model()
#     result = [m[x[i]].as_long() for i in range(12)]
#     print(result)

s = Solver()
a1 = [BitVec(f'a1_{i}', 8) for i in range(25)]
def z(x): return ZeroExt(24,x)

v66 = z(a1[0]) * z(a1[8])
v2 = z(a1[7])
s.add((v2 + v66) & z(a1[1]) == 0x4B)

v65 = z(a1[16])
v3 = z(a1[6])
v64 = z(a1[14])
v62 = z(a1[10]) * z(a1[2])
s.add(((v64 - v62) ^ (v65 - v3)) == 0x182B)

v60 = z(a1[7]) * z(a1[11])
v4 = z(a1[13])
s.add(((v60 - v4) ^ z(a1[4])) == 0x12B3)

v59 = z(a1[0])
v58 = z(a1[17]) * v59
v5 = z(a1[17])
s.add(v5 + v58 == 3417)

v57 = z(a1[5])
v6 = z(a1[1])2
bit_and_res = z(a1[14] & a1[6]) 
s.add(((v57 - v6) ^ bit_and_res) == 0x40)

v56 = z(a1[9])
v55 = z(a1[9])
v7 = z(a1[0])
part_a = ((v55 - v7) ^ ((z(a1[11]) * v56) & z(a1[7]))) == 0x1E
part_b = (z(a1[17]) & (z(a1[0] ^ a1[6]))) == 0x31
s.add(part_a)
s.add(part_b)

v54 = z(a1[17])
v8 = z(a1[6])
s.add((z(a1[9]) ^ (v8 + v54)) == 0xF6)

v53 = z(a1[14])
v52 = (z(a1[4]) * v53) ^ z(a1[6])
v50 = z(a1[7]) * z(a1[4])
s.add(v52 - v50 == 4680)

v49 = z(a1[16])
v9 = z(a1[6])
v48 = v49 - v9
v47 = z(a1[7])
v10 = z(a1[17]) & (z(a1[12]) * v47)
s.add(v48 - v10 == -36) 

s.add(v48 - v10 == BitVecVal(-36, 32))

v46 = z(a1[7])
v45 = z(a1[12])
v44 = z(a1[15]) * v45
v43 = v46 - v44
v11 = z(a1[6])
s.add(v43 - v11 == BitVecVal(-10706, 32))

v42 = z(a1[9])
v41 = z(a1[7])
v40 = z(a1[3]) * v41
v39 = v40 + v42
v12 = z(a1[2])
s.add(v12 + v39 == 3544)

v38 = z(a1[14])
v13 = z(a1[10])
v37 = v13 + v38
v14 = z(a1[13])
s.add((v14 ^ (v37 - v14)) == 0x3A)

v36 = z(a1[14] ^ a1[7] ^ a1[5])
v15 = z(a1[8])
s.add(v15 + v36 == 159)

v35 = z(a1[4] & a1[9])
v16 = z(a1[11])
v34 = v35 - v16
v17 = z(a1[2])
s.add(v17 + v34 == 46)

v33 = z(a1[6])
v18 = z(a1[3])
v32 = v33 - v18
v19 = z(a1[6])
s.add(v19 + v32 == 161)

v31 = z(a1[8])
v30 = z(a1[2])
v29 = z(a1[9]) * v30
v28 = z(a1[6])
v20 = z(a1[9])
s.add(((v20 + v28) ^ (v29 + v31)) == 0x1A9E)

v27 = z(a1[15])
v26 = z(a1[16]) * v27
v21 = z(a1[16])
v25 = v21 + v26
v22 = z(a1[4])
s.add(v25 - v22 == 12815)

v24 = z(a1[6])
part_end_1 = ((z(a1[16]) * v24) & z(a1[0])) ^ z(a1[1] & a1[3]) == 0x43
part_end_2 = (z(a1[11] ^ a1[2] ^ a1[8])) == 91
s.add(part_end_1)
s.add(part_end_2)

s.add(a1[18] == 115)
s.add(a1[19] == 53)
s.add(a1[20] == 49)
s.add(a1[21] == 48)
s.add(a1[22] == 110)
s.add(a1[23] == 83)
s.add(a1[24] == 125)

for i in range(25):
    s.add(a1[i] >= 32)
    s.add(a1[i] <= 126)

if s.check() == sat:
    m = s.model()
    result = [0] * 25
    for i in range(25):
        val = m[a1[i]]
        result[i] = val.as_long()
    flag = bytes(result)
    print(flag)