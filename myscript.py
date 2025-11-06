#!/usr/bin/env python3
#myscript.py
import numpy as np
import ctypes, shutil, random
import multiprocessing as mp

from tmpiler import _envir, _tmpile_c, _read_code, tmp_dir

#########################################################
_envir() # Check venv/admin
#########################################################
## Do some Python work
def Fibon(r, c):
    seq = [0, 1]
    for i in range(r * c - 2):
        seq.append(sum(seq[-2:]))
    return np.array(seq).reshape((r,c))

result = Fibon(3, 4)
print(result)

#########################################################
## Do some C work (But modify it using Python)
## See tmpiler implemetation
## Limititations: exit(0); vs return 0; 
## As the first, would also stop our python process: 
## But we can use pid multi-processing to circumvent this which would still correctly capture exits.
in_d="./in"
c_code = _read_code(f"{in_d}/bitcount.c") 
## Load example code

def _mod_temp(c_code):
    ## Using our temp strat we can modify on-the-fly without actually touching source.
    x = random.choice(result.flatten())
    c_code = c_code.replace("const int MAX_BITS = 32;", f"const int MAX_BITS = {x};")
    return c_code 

c_code = _mod_temp(c_code)

exe_path, tmp_dir = _tmpile_c(c_code, flags=["-O2", "-fPIC"])
## Compile to tmp

## Define ctype run CDLL
def run_c():
    ctypes.CDLL(exe_path).run()

## Run it in mp so we dont have to use fork (depracted)
## Define process
p = mp.Process(target=run_c)
## Start/join threads
p.start()
p.join()
## Done flag linked to exit code
done_success = (p.exitcode == 0)
print("Child exited with code", p.exitcode)
## Clean-up only on success (useful for debug)
if done_success:
    shutil.rmtree(tmp_dir)

#########################################################
## If we do want to use return x;
## Then we do not need to fork/multiprocess at all.
## Define runtime, run and capture exit

#rt = ctypes.CDLL(exe_path)
#rt.run.restype = ctypes.c_int
#exit_code = rt.run()
#print("C function returned", exit_code)

######################################################### BECAUSE WHY NOT