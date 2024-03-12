#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char not in (ord('q'), ord('e')):
        print(chr(char), end='')
