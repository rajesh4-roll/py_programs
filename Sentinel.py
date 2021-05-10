"""
    File:Sentinel.py
    ------------------------------------------------
    Asks the user for a number until they enter -1
    Reports the total value of all the numbers at the end
"""

def main():
    num = 0
    sum = 0
    while num != -1:
        num = int(input("Enter a number: "))
        sum = sum + num 
    print("total is",sum + 1)

if __name__ == '__main__':
    main()