#!/usr/bin/env python3

import numpy as np
import sys as sus
import os
import tempfile as tf
import ctypes, shutil

from tmpiler import _tmpile_c, tmp

is_admin = None
is_venv = sus.prefix != getattr(sus, "base_prefix", sus.prefix)
if os.getuid() == 0:
    is_admin = True
else:
    is_admin = False
    #print(f"{is_admin}. Please run elevated.")
    #sys.exit()

print(f"{sus.executable}, Venv: {is_venv}, Admin {is_admin}")

#########################################################

def Fibon(r, c):
    seq = [0, 1]
    for i in range(r * c - 2):
        seq.append(sum(seq[-2:]))
    return np.array(seq).reshape((r,c))

result = Fibon(3, 4)

print(result)

#########################################################

# Limititations: exit(0); vs return 0; 
# As the first would also stop our python process: 
# But we can use pid os.fork() to circumvent this which would still correctly capture exits.

c_code = r'''
#include <stdio.h>
#include <stdlib.h>

int run() {
    const int MAX_BITS = 32;
    for (int bit = 0; bit < MAX_BITS; bit++)
        printf("BC: %d\n", bit);
    printf("Reached bit %d — exit delimiter triggered.\n", MAX_BITS);
    exit(0); // instead of return 0;
}
'''

exe_path, tmp_dir = _tmpile_c(c_code)

pid = os.fork()
if pid == 0:
    # child
    ctypes.CDLL(exe_path).run()
    os._exit(0)  # ensure child exits successfully eitherway
else:
    # parent
    _, status = os.waitpid(pid, 0)
    exit_code = os.WEXITSTATUS(status)
    print("Child exited with code", exit_code) # but still capture actual return code

# If we do want to use return x; 
# Then we do not need to fork at all.

## Define runtime
#rt = ctypes.CDLL(exe_path)
#rt.run.restype = ctypes.c_int
#exit_code = rt.run()
#print("C function returned", exit_code)