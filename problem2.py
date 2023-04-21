import sys

for line in sys.stdin:
    vals = [int(n) for n in line.split()]
    s = sum(vals)
    if s >= 2**31:
        s -= 2**32
    elif s < -2**31:
        s += 2**32
    print(s)