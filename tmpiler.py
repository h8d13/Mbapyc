#tmpiler.py
import os
import sys as sus
import tempfile as tf
import subprocess as sp
import shutil
import uuid
from contextlib import contextmanager

tmp_dir = tf.mkdtemp(dir=os.getcwd())

def _envir():
    is_admin = None
    is_venv = sus.prefix != getattr(sus, "base_prefix", sus.prefix)
    if os.getuid() == 0:
        is_admin = True
    else:
        is_admin = False
        #print(f"{is_admin}. Please run elevated.")
        #sys.exit()

    print(f"{sus.executable}, Venv: {is_venv}, Admin: {is_admin}")

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

def _tmp_code(c_path, c_code):
    ## Write to temp helper
    with open(c_path, "w") as f:
        f.write(c_code)
    return c_path

def _tmpile_c(c_code, c_filename="bitcount.c", so_name = f"tmp_{uuid.uuid4().hex}.so", flags=None):
    """
    Compile C code into a shared library (.so) in a temporary dir
    
    Returns:
        exe_path (str): Path to the compiled shared library.
        tmp_dir (str): Path to the temporary directory for cleanup.
    """

    c_path = os.path.join(tmp_dir, c_filename)
    exe_path = os.path.join(tmp_dir, so_name)

    _tmp_code(c_path, c_code)

    sp.run(["gcc", "-shared", *flags, c_path, "-o", exe_path], check=True)
    
    return exe_path, tmp_dir
