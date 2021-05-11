"""
Part A:
Replace this comment with your answer to Part A
line 18: replace 'n =' by return
line 21: replace 'n =' by return
line 26: put n = divide_and_round(n)

"""

"""
Part B: 
Edit this code so that it works correctly
line 31 and 32 added to start the main fun

"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        return n / 2
    else:
        return (n + 1) / 2

def main():
    n = 10
    n = divide_and_round(n)
    print(n) 

if __name__ == '__main__':
    main()