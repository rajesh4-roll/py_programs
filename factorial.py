"""
    File: factorial.py
    ---------------------------------------
    This program finds the factorial upto 9
    example:-
    0 1
    1 1
    2 2
    3 6
    4 24
    5 120
"""

MAX_NUM = 9

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    for i in range(MAX_NUM + 1):
        x = factorial(i)
        print(i,x)
        

if __name__ == '__main__':
    main()