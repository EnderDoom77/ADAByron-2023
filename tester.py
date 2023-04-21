import importlib
import sys
import os
import re
import time

test_file_re = re.compile(r"sample.*([1-9][0-9]*).*\.([1-9][0-9]*)\.(in|out)")
modules = {}
original_in = sys.stdin
original_out = sys.stdout

def run_program(n: int):
    mod_name = f"problem{n}"
    if mod_name in modules:
        importlib.reload(modules[mod_name])
    else:
        modules[mod_name] = importlib.import_module(mod_name)

def check_equal(path_expected: str, path_result: str, problem:int, sample:int):
    lines1 = open(path_expected, "r").readlines()
    lines2 = open(path_result, "r").readlines()
    for i in range(max(len(lines1), len(lines2))):
        try:
            l1 = lines1[i]
            l2 = lines2[i]
        except IndexError:
            print(f"DIFF LNCOUNT: P{problem}.{sample} -> Line {i + 1}")
            return
        
        if l1 != l2:
            print(f"DIFF LINE: P{problem}.{sample} -> Line {i + 1}")
            print(f"EXPECTED: \'{l1[:-1]}\'\nRESULT:   \'{l2[:-1]}\'")
            return
    print(f"SUCCESS: P{problem}.{sample}")

to_check = []

data_root = "data/"
for path in os.listdir(data_root):
    full_path = os.path.join(data_root, path)
    if os.path.isfile(full_path):
        m = test_file_re.match(path)
        if m is None: continue
        (problem, sample, putType) = m.groups()
        if putType == "in":
            sys.stdin = open(full_path, "r", encoding="utf-8")
            outpath = f"{full_path[:-3]}.out"
            sys.stdout = open(f"{outpath}.test", "w", encoding="utf-8")
            try:
                run_program(int(problem))
                time.sleep(0.5)  
            except:
                sys.stdout = original_out
                print(f"Unable to find module \'problem{problem}.py\'")
                continue

            to_check.append((outpath, f"{outpath}.test", problem, sample))

time.sleep(1)
sys.stdout = original_out
for (refpath, testpath, problem, sample) in to_check:
    check_equal(refpath, testpath, problem, sample)