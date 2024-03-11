#!/usr/bin/python3
import sys
import os
import compileall

pyfile = os.environ.get('PYFILE')
if not pyfile:
    print("Environment variable PYFILE not set.")
    sys.exit(1)

pyfilec = f"{pyfile}c"
compileall.compile_file(pyfile, pyfilec)
print(f"Compiling {pyfile}...")
