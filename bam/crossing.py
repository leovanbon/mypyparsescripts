import math
input = "flag.jpg.crossing"
output = "flag.jpg"
board = open(input, "rb").read()

a = int(math.sqrt(len(board)))

original = {}
checked = [0] * len(board)

def harvest_right(pos):
    frame_count = -1
    original_idx = -1
    nibble = -1 
    pow_val = 0
    
    frame_check = []
    line = pos // a
    cur = pos
    

    while cur < len(board) and frame_count < 2 and board[cur] != 0 and (cur // a) == line:
        if board[cur] == 0xff and checked[cur] == 0:
            frame_check.append(cur)
            frame_count += 1
            cur += 1
            continue
            
        if frame_count == 0:
            buf = 253 if board[cur] == 2 else board[cur] - 2
            original_idx += buf * (253 ** pow_val)
            pow_val += 1
            
        elif frame_count == 1:
            nibble += 1
            
        cur += 1

    if original_idx >= 0 and nibble > 0: 
        for i in frame_check: 
            checked[i] = 1
        return (original_idx, nibble)
    return (-1, 0)

def harvest_down(pos):
    frame_count = -1
    original_idx = -1
    nibble = -1
    pow_val = 0
    
    frame_check = []
    cur = pos
    while cur < len(board) and frame_count < 2 and board[cur] != 0:
        if board[cur] == 0xff and checked[cur] == 0:
            frame_check.append(cur)
            frame_count += 1
            cur += a
            continue
            
        if frame_count == 0:
            buf = 253 if board[cur] == 2 else board[cur] - 2
            original_idx += buf * (253 ** pow_val)
            pow_val += 1
            
        elif frame_count == 1:
            nibble += 1
            
        cur += a

    if original_idx >= 0 and nibble > 0: 
        for i in frame_check: 
            checked[i] = 1
        return (original_idx, nibble)
    return (-1, 0)

def h4rvest(pos):
    idx, val = harvest_right(pos)
    if idx < 0 or val <= 0: 
       idx, val = harvest_down(pos)    
        
    if idx >= 0 and val > 0: 
        original[idx] = val

def h4rvest_1(pos):
    idx, val = harvest_down(pos)
    if idx < 0 or val <= 0: 
       idx, val = harvest_right(pos)    
        
    if idx >= 0 and val > 0: 
        original[idx] = val


for i in range(len(board)):
    if checked[i]:
        continue
        
    if board[i] == 0xff: 
        h4rvest_1(i)


max_idx = max(original.keys())
result = [0] * (max_idx + 1)
for k, v in original.items():
    result[k] = v

flag = open(output, "wb")
for i in range(len(result)//2):
    flag.write(bytes([result[i*2]*16 + result[i*2+1]]))