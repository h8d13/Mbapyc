#!/usr/bin/env python3

import numpy as np

import sys as sus
import os

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

import tempfile, subprocess, ctypes, shutil

c_code = r"""
#include <stdio.h>
int run() {
    for (int i = 0; i < 32; i++)
        printf("Bit count: %d\n", i);
    printf("Reached 32 bits. Exiting.\n");
    return 0;
}
"""

tmpdir = tempfile.mkdtemp(dir=os.getcwd())

c_path = os.path.join(tmpdir, "bitcount.c")
so_path = os.path.join(tmpdir, "bitcount.so")

with open(c_path, "w") as f:
    f.write(c_code)

subprocess.run(["gcc", "-shared", "-fPIC", c_path, "-o", so_path], check=True)
ctypes.CDLL(so_path).run()
shutil.rmtree(tmpdir)

