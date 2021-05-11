"""
    File: nondecrease.py
    -----------------------------------------
    A sequence of non-decreasing numbers entered
    by the user if does then program stop and displays 
    the sequence length.
"""


def main():
    count = 0
    print('Enter a sequence of non-decreasing numbers.')
    num = float(input('Enter num: '))
    sum = num
    while True:
        num = float(input('Enter num: '))
        if num >= sum:
            sum += num
            count += 1
        else:
            print('Thanks for playing!')
            break
    print('Sequence length: ',count)

if __name__ == '__main__':
    main()