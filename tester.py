from importlib import reload, import_module
import sys
import os
import re

sample_re = re.compile(r"sample.*([0-9]+).*\.([0-9]+)\.in")
modules = {}
console_out = sys.stdout

def run_program(n: int):
    name = f"problem{n}"
    if name in modules:
        reload(modules[name])
    else:
        modules[name] = import_module(name)

def check_equal(path_expected: str, path_result: str, pid: str):
    lines1 = open(path_expected, "r").readlines()
    lines2 = open(path_result, "r").readlines()
    for i,(l1,l2) in enumerate(zip(lines1, lines2)):
        if l1 != l2:
            print(f"DIFF LINE: {pid} -> Line {i + 1}")
            print(f"\tEXPECTED: \'{l1[:-1]}\'\n\tRESULT:   \'{l2[:-1]}\'")
            return
    if (cnt1 := len(lines1)) != (cnt2 := len(lines2)):
        print(f"DIFF LNCOUNT: {pid} -> {cnt1} != {cnt2}")
    print(f"SUCCESS: {pid}")

to_check = []
data_root = "data/"
for path in os.listdir(data_root):
    full_path = os.path.join(data_root, path)
    if not os.path.isfile(full_path): continue
    
    m = sample_re.match(path)
    if m is None: continue
    (problem, sample) = m.groups()
    
    sys.stdin = open(full_path, "r")
    outpath = f"{full_path[:-3]}.out"
    sys.stdout = open(f"{outpath}.test", "w")
    try:
        run_program(int(problem))
        to_check.append((outpath, f"{outpath}.test", f"P{problem}.{sample}"))
    except:
        sys.stdout = console_out
        print(f"Unable to find module \'problem{problem}.py\'")

sys.stdout = console_out
for (refpath, testpath, pid) in to_check:
    check_equal(refpath, testpath, pid)