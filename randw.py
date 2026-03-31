# def deco_file(input_file, output_file, key):
#     with open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:

#         c = 0
#         while True:
#             byte_doc = f_in.read(1)
#             if not byte_doc:
#                 break
            
#             byte_ma = byte_doc[0]
#             byte_goc = ((byte_ma - 0x13) %256) ^ key[c%4]
#             f_out.write(bytes([byte_ma]))
#             c+=1

verni = open('sun-temple', 'rb').read()
byt = bytearray(len(verni))
for i in range(len(verni)):
    if i >= 0x1000 and verni[i] == 0xeb and verni[i+1] == 0xf7 and verni[i+2] == 0xe8:
        for j in range(15):
            byt[i - 12 + j] = 0x90
    else:
        byt[i] = verni[i]

open('sun-patched', 'wb').write(byt)
