def solve_hidato(board):
    n = len(board)
    prefilled = {}
    max_val = n * n

    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                prefilled[board[r][c]] = (r, c)

    if 1 not in prefilled:
        return False

    start_r, start_c = prefilled[1]

    def get_next_target(current_val):
        for num in sorted(prefilled.keys()):
            if num > current_val:
                return num, prefilled[num]
        return None, None

    def is_reachable(r, c, current_val, target_val, target_pos):
        if target_val is None:
            return True
        tr, tc = target_pos
        dist = max(abs(r - tr), abs(c - tc))
        return dist <= (target_val - current_val)

    def backtrack(r, c, val):
        if val == max_val:
            return True

        next_val = val + 1
        target_val, target_pos = get_next_target(val)

        if next_val in prefilled:
            pr, pc = prefilled[next_val]
            if max(abs(r - pr), abs(c - pc)) == 1:
                return backtrack(pr, pc, next_val)
            else:
                return False

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue

                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if board[nr][nc] == 0:
                        if is_reachable(nr, nc, next_val, target_val, target_pos):
                            board[nr][nc] = next_val
                            if backtrack(nr, nc, next_val):
                                return True
                            board[nr][nc] = 0
        return False

    if backtrack(start_r, start_c, 1):
        return board
    else:
        return None


cip1 = bytes.fromhex("""
04 00 60 05 00 5E 06 00  5D 07 00 55 0A 00 4E 0B
00 4F 0C 00 48 0D 00 47  00 01 65 02 01 AF 03 01
B4 04 01 B5 06 01 5C 07  01 54 08 01 56 09 01 51
0A 01 50 0B 01 4D 0D 01  49 0E 01 45 00 02 66 01
02 AD 03 02 B3 04 02 B6  05 02 B7 06 02 5B 07 02
59 0A 02 DC 0B 02 DB 0C  02 4C 0D 02 4A 00 03 67
02 03 B1 03 03 B2 04 03  B8 05 03 BA 06 03 BB 08
03 DF 0E 03 43 00 04 AB  03 04 A4 04 04 B9 05 04
BC 07 04 E0 08 04 DE 0B  04 D5 0D 04 D7 0E 04 41
00 05 AA 03 05 6A 04 05  A3 05 05 BD 06 05 E1 08
05 D0 0A 05 CE 0B 05 D3  0C 05 D6 0D 05 40 00 06
A9 01 06 A7 02 06 A6 04  06 A2 06 06 C0 07 06 C2
09 06 CF 0A 06 CD 0B 06  3B 0C 06 3C 0D 06 3D 0E
06 3E 00 07 75 02 07 73  03 07 6C 04 07 A1 05 07
C5 0B 07 37 0C 07 3A 0D  07 39 0E 07 32 00 08 76
01 08 74 02 08 71 03 08  6D 04 08 6E 05 08 A0 06
08 C6 07 08 C7 08 08 C9  09 08 22 0A 08 21 0B 08
35 0D 08 33 00 09 77 01  09 7A 02 09 7B 03 09 70
04 09 6F 06 09 1D 07 09  1E 08 09 1F 09 09 20 00
0A 01 01 0A 78 02 0A 79  03 0A 7C 04 0A 1B 05 0A
1C 06 0A 9E 07 0A 9D 08  0A 28 0A 0A 2A 0B 0A 24
0C 0A 2C 0D 0A 2F 0E 0A  2E 00 0B 02 01 0B 03 03
0B 1A 05 0B 7E 06 0B 7F  07 0B 9C 08 0B 9B 09 0B
27 0B 0B 25 0D 0B 92 00  0C 05 03 0C 19 04 0C 15
05 0C 14 06 0C 11 07 0C  80 08 0C 81 09 0C 9A 0A
0C 99 0B 0C 97 0C 0C 96  0E 0C 90 00 0D 07 03 0D
16 09 0D 86 0A 0D 98 0B  0D 89 0C 0D 95 0E 0D 8E
00 0E 08 02 0E 0A 05 0E  0E 08 0E 84 09 0E 87 0D
0E 8C""")

board = [0]*225
for i in range(len(cip1)//3):
    board[cip1[i*3]+cip1[i*3+1]*15] = cip1[i*3+2]

b = [board[i:i+15] for i in range(0, 225, 15)]

res = solve_hidato(b)


open('ans', 'wb').write(bytearray([x for row in res for x in row]))
print(hex(102))