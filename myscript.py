#!/usr/bin/env python3
#myscript.py
import numpy as np
import ctypes, shutil
import multiprocessing as mp

from tmpiler import _envir, _tmpile_c, _read_code, tmp_dir

#########################################################
## Prereqs
_envir()

#########################################################
## Do some python work

def Fibon(r, c):
    seq = [0, 1]
    for i in range(r * c - 2):
        seq.append(sum(seq[-2:]))
    return np.array(seq).reshape((r,c))

result = Fibon(3, 4)
print(result)

#########################################################
## Do some C work
## Limititations: exit(0); vs return 0; 
## As the first, would also stop our python process: 
## But we can use pid multi-processing to circumvent this which would still correctly capture exits.

c_code = _read_code("bitcount.c") 
exe_path, tmp_dir = _tmpile_c(c_code, flags=["-O2", "-fPIC"])

def run_c():
    ctypes.CDLL(exe_path).run()

p = mp.Process(target=run_c)
p.start()
p.join()
print("Child exited with code", p.exitcode)

## Clean-up
shutil.rmtree(tmp_dir) 
#########################################################

## If we do want to use return x; 
## Then we do not need to fork at all.
## Define runtime and run and capture exit

#rt = ctypes.CDLL(exe_path)
#rt.run.restype = ctypes.c_int
#exit_code = rt.run()
#print("C function returned", exit_code)