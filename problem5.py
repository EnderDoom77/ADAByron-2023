import sys

lines = 0
words = 0
for line in sys.stdin:
    lines += 1
    words += len([w for w in line.split()])
    
print(f"{words:11d} words")
print(f"{lines:11d} lines")