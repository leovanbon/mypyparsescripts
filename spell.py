import os

# This reads directly from /dev/urandom
random_bytes = os.urandom(8)
print(random_bytes)
