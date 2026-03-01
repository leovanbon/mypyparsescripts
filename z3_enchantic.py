from z3 import *

# s = Solver()
# x = [Int(f'x_{i}') for i in range(12)]
# targets = [-4, 11, 8, 10, 31, 0, 28, 4, 1, 25, 10, 11]

# s.add(x[0] * x[1] - 2 * x[2] == targets[0])
# s.add(x[1] + 5 * x[2] - 3 * x[3] == targets[1])
# s.add(x[2] + x[3] * x[4] - x[0] == targets[2])
# s.add(x[5] + 2 * x[4] + x[2] == targets[3])
# s.add(20 * x[1] - 2 * x[2] - x[4] == targets[4])
# s.add(x[2] + x[5] - 2 * x[1] == targets[5])
# s.add(2 * x[1] + x[2] + 3 * x[6] + 4 * x[7] == targets[6])
# s.add(5 * x[5] - x[7] - x[8] + 2 * x[9] == targets[7])
# s.add(3 * x[8] + 2 * x[9] + 4 * x[10] - 3 * x[6] == targets[8])
# s.add(9 * x[11] + 2 * x[10] - x[8] == targets[9])
# s.add(4 * x[7] - x[8] + x[10] == targets[10])
# s.add((x[3] ** x[8]) + 3 * x[11] - 2 * x[7] + x[6] + x[5] + x[10] == targets[11])

# for i in range(12):
#     s.add(x[i] >= 32)
#     s.add(x[i] <= 126)

# if s.check() == sat:
#     m = s.model()
#     result = [m[x[i]].as_long() for i in range(12)]
#     print(result)
