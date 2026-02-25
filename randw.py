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

verni = open('main', 'rb').read()
byt = bytearray(len(verni)+1)
for i in range(len(verni)):
    if i >= 0x1000 and verni[i] == 0xeb and verni[i+1] == 0xff and verni[i+2] == 0xc1:
        for j in range(5):
            byt[i+j] = 0x90
    else:
        byt[i] = verni[i]

open('patched_main', 'wb').write(byt)
