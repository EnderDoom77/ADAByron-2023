import sys

for line in sys.stdin:
    vals = [float(n) for n in line.split()]
    a = vals[0]
    b = vals[1]
    result = f" {a:17.7f} / {b:17.7f} = "
    if b == 0:
        if a < 0:
            result += "-Infinite"
        elif a > 0:
            result += " Infinite"
        else:
            result += " Not a Number"
    else:
        result += f"{a/b:17.7f}"
    print(result)