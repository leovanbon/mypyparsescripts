import pefile
from pwn import xor

flag = ""

for i in range(20, -1, -1):
    pe = pefile.PE(f"nucleus{i+1}.exe")

    for res_type in pe.DIRECTORY_ENTRY_RESOURCE.entries:
        if res_type.id == pefile.RESOURCE_TYPE['RT_RCDATA']:
            for res_id in res_type.directory.entries:
                if res_id.id == 101:
                    for res_lang in res_id.directory.entries:
                        data_rva  = res_lang.data.struct.OffsetToData
                        size      = res_lang.data.struct.Size
                        payload   = pe.get_data(data_rva, size)
                        
                        key = payload[0] ^ 0x4D
                        flag += chr(key)
                        open(f"nucleus{i}.exe", "wb").write(xor(payload,key))

print(flag[::-1])

