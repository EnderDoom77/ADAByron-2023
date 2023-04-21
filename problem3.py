import sys

for line in sys.stdin:
    vals = [float(n) for n in line.split()]
    s = sum(vals)
    print(f" {vals[0]:12.3f} + {vals[1]:12.3f} = {s:12.3f}")