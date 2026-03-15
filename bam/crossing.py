import math
input = "flag.jpg.crossing"
output = "flag.jpg"
board = open(input, "rb").read()

a = int(math.sqrt(len(board)))

original = {}
checked = [0] * len(board)

def harvest_right(pos):
    frame_count = -1
    original_idx = 0
    nibble = -1
    pow_val = 0

    frame_check = []
    nib_bytes = []
    line = pos // a
    cur = pos

    while cur < len(board) and frame_count < 2 and board[cur] != 0 and (cur // a) == line:
        if board[cur] == 0xff and checked[cur] == 0:
            frame_check.append(cur)
            frame_count += 1
            cur += 1
            continue

        if frame_count == 0:
            buf = board[cur] - 2
            original_idx += buf * (253 ** pow_val)
            pow_val += 1

        elif frame_count == 1:
            nibble += 1
            nib_bytes.append(board[cur])

        cur += 1

    if original_idx >= 1 and nibble >= 0 and all(b == 1 for b in nib_bytes):
        for i in frame_check:
            checked[i] = 1
        return (original_idx - 1, nibble)
    return (-1, -1)

def harvest_down(pos):
    frame_count = -1
    original_idx = 0
    nibble = -1
    pow_val = 0

    frame_check = []
    nib_bytes = []
    cur = pos
    col = pos % a

    while cur < len(board) and frame_count < 2 and board[cur] != 0 and (cur % a) == col:
        if board[cur] == 0xff and checked[cur] == 0:
            frame_check.append(cur)
            frame_count += 1
            cur += a
            continue

        if frame_count == 0:
            buf = board[cur] - 2
            original_idx += buf * (253 ** pow_val)
            pow_val += 1

        elif frame_count == 1:
            nibble += 1
            nib_bytes.append(board[cur])

        cur += a

    if original_idx >= 1 and nibble >= 0 and all(b == 1 for b in nib_bytes):
        for i in frame_check:
            checked[i] = 1
        return (original_idx - 1, nibble)
    return (-1, -1)

def h4rvest(pos):
    idx, val = harvest_down(pos)
    if idx < 0 or val < 0:
        idx, val = harvest_right(pos)

    if idx >= 0 and val >= 0:
        if idx not in original:
            original[idx] = val


for i in range(len(board)):
    if checked[i]:
        continue

    if board[i] == 0xff:
        h4rvest(i)


# Filter out spurious high-index entries (artefacts from crossing points being
# mis-parsed). Real nibble indices are dense starting from 0; find the first
# large gap and discard everything beyond it.
sorted_keys = sorted(original.keys())
cutoff = sorted_keys[-1]
for i in range(len(sorted_keys) - 1):
    if sorted_keys[i + 1] - sorted_keys[i] > 2:
        cutoff = sorted_keys[i]
        break

filtered = {k: v for k, v in original.items() if k <= cutoff}

max_idx = max(filtered.keys())
result = [0] * (max_idx + 1)
for k, v in filtered.items():
    result[k] = v

flag = open(output, "wb")
for i in range(len(result) // 2):
    flag.write(bytes([result[i * 2] * 16 + result[i * 2 + 1]]))