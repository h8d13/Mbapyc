# Mbapyc

A mix of bash, python and C.

- 2 Bash wrappers, one for setup `pya_venv`, one for running `run`.
- Auto-update pip, create venv if it doesn't exist.
- Check executable is actually using venv, also elevated True/False.

- Build temp `.so` files, modify on the fly, build using `gcc`, run and clean-up, exit.
