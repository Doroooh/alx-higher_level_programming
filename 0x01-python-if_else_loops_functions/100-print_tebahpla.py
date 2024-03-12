#!/usr/bin/python3
# printing alphabets in reverse, while alternating between lowercase and uppercase alphabets

k = 0
for g in range(ord('s'), ord('h') - 1, -1):
    print(f"{chr(g - k)}", end="")
    k = 32 if k == 0 else 0
