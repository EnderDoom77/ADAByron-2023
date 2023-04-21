import sys

lines = 0
digits = 0
letters = 0
for line in sys.stdin:
    lines += 1
    letters += len([w for w in line if w.isalpha()])
    digits += len([w for w in line if w.isdigit()])
    
print(f"{letters:11d} letters")
print(f"{digits:11d} digits")
print(f"{lines:11d} lines")