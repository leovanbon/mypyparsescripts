from pwn import xor
import re

ciper = """
  local_98 = 0x29;
  local_97 = 0xb4;
  local_96 = 0x8e;
  local_95 = 0x3e;
  local_94 = 0x23;
  local_93 = 0x87;
  local_92 = 0x9a;
  local_91 = 0xf0;
  local_90 = 0x28;
  local_8f = 0x46;
  local_8e = 0xae;
  local_8d = 0x45;
  local_8c = 0x54;
  local_8b = 0x5e;
  local_8a = 0x78;
  local_89 = 0x18;
  local_88 = 0x66;
  local_87 = 100;
  local_86 = 5;
  local_85 = 0x82;
  local_84 = 0x67;
  local_83 = 0x95;
  local_82 = 1;
  local_81 = 0x65;
  local_80 = 0x5c;
  local_7f = 0xf2;
  local_7e = 0x6a;
  local_7d = 0x7c;
  local_7c = 0x27;
  local_7b = 199;
  local_7a = 0xa6;
  local_79 = 0x34;
  local_78 = 0x19;
  local_77 = 0x7e;
  local_76 = 0x28;
  local_75 = 0xc;
  local_74 = 4;
  local_73 = 0x6b;
  local_72 = 0x74;
  local_71 = 1;
  local_70 = 0x2a;
  local_6f = 0x20;
  local_6e = 0xd9;
  local_6d = 0x39;
  local_6c = 0x48;
  local_6b = 0x96;
  local_6a = 0x7e;
  local_69 = 0x19;
  local_68 = 0xa9;
  local_67 = 0xae;
  local_66 = 0x5e;
  local_65 = 0x5a;
  local_64 = 0xb4;
  local_63 = 0xe5;
  local_62 = 0xf8;
  local_61 = 0x50;
  local_60 = 0xa1;
  local_5f = 0x8a;
  local_5e = 0x6c;
  local_5d = 0x3a;
  local_5c = 0xdf;
  local_5b = 0xbd;
  local_5a = 0xf0;
  local_59 = 0x72;
"""

keb = """
  local_b8[0] = 8;
  local_b8[1] = 0x3c;
  local_b8[2] = 0x96;
  local_b8[3] = 0x53;
  local_b8[4] = 0x8d;
  local_b8[5] = 0x28;
  local_b8[6] = 0xce;
  local_b8[7] = 0x51;
  local_b8[8] = 0x67;
  local_b8[9] = 0x61;
  local_b8[10] = 0x98;
  local_b8[0xb] = 0x82;
  local_b8[0xc] = 0xaa;
  local_b8[0xd] = 0xe6;
  local_b8[0xe] = 0xcb;
  local_b8[0xf] = 0x20;
  local_b8[0x10] = 0x75;
  local_b8[0x11] = 0x7f;
  local_b8[0x12] = 0xc0;
  local_b8[0x13] = 0xee;
  local_b8[0x14] = 0x6c;
  local_b8[0x15] = 0x33;
  local_b8[0x16] = 0xaa;
  local_b8[0x17] = 0xd5;
  local_b8[0x18] = 0x5f;
  local_b8[0x19] = 0xca;
  local_b8[0x1a] = 0x22;
  local_b8[0x1b] = 0x8f;
  local_b8[0x1c] = 0x6f;
  local_b8[0x1d] = 0xa6;
  local_b8[0x1e] = 0x41;
  local_b8[0x1f] = 0x30;
"""

kef = """
  local_f8[0] = 0x96;
  local_f8[1] = 0x66;
  local_f8[2] = 0x85;
  local_f8[3] = 0x10;
  local_f8[4] = 0x53;
  local_f8[5] = 0x74;
  local_f8[6] = 0xa7;
  local_f8[7] = 0xad;
  local_f8[8] = 0xc9;
  local_f8[9] = 0x42;
  local_f8[10] = 0x34;
  local_f8[0xb] = 0x3a;
  local_f8[0xc] = 0x88;
  local_f8[0xd] = 0x91;
  local_f8[0xe] = 0xd5;
  local_f8[0xf] = 0x9f;
"""

pat = r"=\s*(0x[0-9a-fA-F]+|\d+);"
matches = re.findall(pat, ciper)

keye = bytearray("this-message-is-flag".encode())
keyb = bytearray([int(x,0)for x in re.findall(pat,keb)])
keyf = bytearray([int(x,0) for x in re.findall(pat,kef)])
final= bytearray([int(x, 0) for x in matches])


RL_64 = lambda p1, p2: ((p1 << (p2 & 0x3f)) & 0xFFFFFFFFFFFFFFFF) | (p1 >> (64 - (p2 & 0x3f)))    

first = xor(keyb, keyf)
print(first)
