import re

data = """
* - - - - - - - - *
| | - * | - * | - |
| 3 5 j . l Z v C |
* - - - - - - - - *
"""

chars = re.findall(r'(?<=^\| | ).(?= | \|$)', data, re.MULTILINE)

print(chars)