#tmpiler.py
import os
import sys as sus
import tempfile as tf
import subprocess as sp
import shutil
import random

tmp = tf.mkdtemp(dir=os.getcwd())

def _read_code(c_code):
    try:
        with open(c_code, "r") as f:
            return f.read()

    except FileNotFoundError:
        #Remove the temp dir
        shutil.rmtree(tmp) 
        #Warn/exit
        print(f'{c_code} not found.')
        sus.exit(1)

def _mod_temp(c_code):
    ### Using our temp strat we can modify on the fly existing bitcount.c file without actually touching it.

    x = random.randint(1,31)
    c_code = c_code.replace("const int MAX_BITS = 32;", f"const int MAX_BITS = {x};")
    return c_code 

def _tmp_code(c_path, c_code):
    """Write C code to a temp file and return the path."""
    with open(c_path, "w") as f:
        f.write(c_code)
    return c_path

def _tmpile_c(c_code, work_dir=None, so_name="bitcount.so", flags=None):
    """
    Compile C code into a shared library (.so) in a temporary dir
    
    Returns:
        exe_path (str): Path to the compiled shared library.
        tmp_dir (str): Path to the temporary directory for cleanup.
    """
    tmp_dir = tf.mkdtemp(dir=work_dir)
    c_path = os.path.join(tmp_dir, "bitcount.c")
    exe_path = os.path.join(tmp_dir, so_name)

    c_code = _mod_temp(c_code)

    _tmp_code(c_path, c_code)

    sp.run(["gcc", "-shared", *flags, c_path, "-o", exe_path], check=True)
    
    shutil.rmtree(tmp) 

    return exe_path, tmp_dir
