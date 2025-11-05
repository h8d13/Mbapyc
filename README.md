# Mbapyc

A mix of bash, python and inline-C.

- 2 Bash wrappers, one for setup, one for running.
- Auto-update pip, create venv if it doesn't exist.
- Check executable is actually using venv, also elevated True/False.
- Build temp `.so` files, build using `gcc`, run and clean-up, exit.

## Usage

`$ ./pya_venv`

**Output:**
```
Creating .venv ...
Requirement already satisfied: pip in ./.venv/lib/python3.13/site-packages (25.2)
Collecting pip
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.2
    Uninstalling pip-25.2:
      Successfully uninstalled pip-25.2
Successfully installed pip-25.3
Collecting numpy (from -r requirements.txt (line 1))
Installing collected packages: numpy
Successfully installed numpy-2.3.4
Done.
```

`$ ./run`

**Output:**
```
Ru-using existing venv.
/home/hadeaneon/Desktop/Mbapyc/.venv/bin/python3, Venv: True, Admin False
[[ 0  1  1  2]
 [ 3  5  8 13]
 [21 34 55 89]]
Bit count: 0
Bit count: 1
Bit count: 2
Bit count: 3
Bit count: 4
Bit count: 5
Bit count: 6
Bit count: 7
Bit count: 8
Bit count: 9
Bit count: 10
Bit count: 11
Bit count: 12
Bit count: 13
Bit count: 14
Bit count: 15
Bit count: 16
Bit count: 17
Bit count: 18
Bit count: 19
Bit count: 20
Bit count: 21
Bit count: 22
Bit count: 23
Bit count: 24
Bit count: 25
Bit count: 26
Bit count: 27
Bit count: 28
Bit count: 29
Bit count: 30
Bit count: 31
Reached bit 32 — exit delimiter triggered.
child exited with status 0
```