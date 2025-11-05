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
BC: 0
BC: 1
BC: 2
BC: 3
BC: 4
BC: 5
BC: 6
BC: 7
BC: 8
BC: 9
BC: 10
BC: 11
BC: 12
BC: 13
BC: 14
BC: 15
BC: 16
BC: 17
BC: 18
BC: 19
BC: 20
BC: 21
BC: 22
BC: 23
BC: 24
BC: 25
BC: 26
BC: 27
BC: 28
BC: 29
BC: 30
BC: 31
Reached bit 32 — exit delimiter triggered.
Child exited with code 0
```