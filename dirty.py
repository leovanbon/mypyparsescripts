import re
# def x0r(match):
#     val1 = int(match.group(1))
#     val2 = int(match.group(2))
#     return str(val1 ^ val2)

# with open("fuckass.py", "r") as fuck:
#     content = fuck.read()

# pat = re.compile(r'xor\((\d+),\s*(\d+)\)')

# prev = ""

# while cur != prev:
#     prev = cur
#     cur = pat.sub(x0r, cur)

# print(cur)

# with open("xored.py", "w") as f:
#     f.write(cur)

pat = re.compile(r'')

code = """
    if ( *a1 == 66 )
    {
    if ( a2 <= 1 )
    core::panicking::panic_bounds_check();
    if ( a1[1] == 75 )
    {
    if ( a2 <= 2 )
    core::panicking::panic_bounds_check();
    if ( a1[2] == 83 )
    {
    if ( a2 <= 3 )
    core::panicking::panic_bounds_check();
    if ( a1[3] == 69 )
    {
    if ( a2 <= 4 )
    core::panicking::panic_bounds_check();
    if ( a1[4] == 67 )
    {
    if ( a2 <= 5 )
    core::panicking::panic_bounds_check();
    if ( a1[5] == 123 )
    {
    if ( a2 <= 6 )
    core::panicking::panic_bounds_check();
    if ( a1[6] == 119 )
    {
    if ( a2 <= 7 )
    core::panicking::panic_bounds_check();
    if ( a1[7] == 51 )
    {
    if ( a2 <= 8 )
    core::panicking::panic_bounds_check();
    if ( a1[8] == 108 )
    {
    if ( a2 <= 9 )
    core::panicking::panic_bounds_check();
    if ( a1[9] == 67 )
    {
    if ( a2 <= 0xA )
    core::panicking::panic_bounds_check();
    if ( a1[10] == 48 )
    {
    if ( a2 <= 0xB )
    core::panicking::panic_bounds_check();
    if ( a1[11] == 109 )
    {
    if ( a2 <= 0xC )
    core::panicking::panic_bounds_check();
    if ( a1[12] == 51 )
    {
    if ( a2 <= 0xD )
    core::panicking::panic_bounds_check();
    if ( a1[13] == 95 )
    {
    if ( a2 <= 0xE )
    core::panicking::panic_bounds_check();
    if ( a1[14] == 116 )
    {
    if ( a2 <= 0xF )
    core::panicking::panic_bounds_check();
    if ( a1[15] == 79 )
    {
    if ( a2 <= 0x10 )
    core::panicking::panic_bounds_check();
    if ( a1[16] == 95 )
    {
    if ( a2 <= 0x11 )
    core::panicking::panic_bounds_check();
    if ( a1[17] == 82 )
    {
    if ( a2 <= 0x12 )
    core::panicking::panic_bounds_check();
    if ( a1[18] == 101 )
    {
    if ( a2 <= 0x13 )
    core::panicking::panic_bounds_check();
    if ( a1[19] == 118 )
    {
    if ( a2 <= 0x14 )
    core::panicking::panic_bounds_check();
    if ( a1[20] == 118 )
    {
    if ( a2 <= 0x15 )
    core::panicking::panic_bounds_check();
    return a1[21] == 125;
"""

pat = r'a1\[.*?\]\s==\s([^\)\]\n;]+)'
l = (re.findall(pat,code))
print("".join([chr(int(x)) for x in l]))
