#!/usr/bin/python3
import dis

def print_names(filename):
    with open(filename, 'rb') as f:
        code = f.read()
    dis.dis(code)
    print_names("hidden_4.pyc")

