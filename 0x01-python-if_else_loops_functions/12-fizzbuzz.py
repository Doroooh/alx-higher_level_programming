#!/usr/bin/python3
# to print numbers one to 100 with a space separation.
# for the multiples of 3, then print Fizz instead of the number.
# for the multiples of 5 then print Buzz instead of the number.
# for the multiple of 3 and 5 then print FizzBuzz instead of the number

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz ", end="")
    elif number % 3 == 0:
        print("Fizz ", end="")
    elif number % 5 == 0:
        print("Buzz ", end="")
    else:
        print(f"{number} ", end="")
