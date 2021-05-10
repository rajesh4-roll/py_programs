"""
    File: equals.py
    ---------------------------
    Checking the equality of number
"""

import random

def main():
    n = 0
    num = random.randint(1,90)
    while (n != num):
        n = n + 1
        print(n)

if __name__ == '__main__':
    main()