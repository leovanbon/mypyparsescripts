from pwn import xor

xor_key = [0x88, 0x66, 0x44, 0x11, 0x77, 0x55, 0x22, 0x33]

def decrypt_xor_algo(data):
    
    length = len(data)
    output = bytearray()
    
    current_key_idx = (8 - (length % 8)) % 8
    
    for byte in data:
        output.append(byte ^ xor_key[current_key_idx])
        current_key_idx = (current_key_idx + 1) % 8
        
    return output
        
ciphe = bytes.fromhex("220c6a33204455fb390074013c4156d704316528205156d70b217c14255b6ce10837651234464e")

print(xor(ciphe, xor_key))

print(decrypt_xor_algo(ciphe))



