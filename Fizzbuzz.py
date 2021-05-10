def fizzbuzz(x):
    fizz = 0
    buzz = 0
    fizzbuzz = 0
    i = 0
    while i != x:
        i = i + 1
        if i % 3 ==0 and i % 5==0:
            print('Fizzbuzz')
            fizzbuzz = fizzbuzz + 1
        elif i % 3 ==0:
            print('Fizz')
            fizz = fizz + 1
        elif i % 5 ==0:
            print('Buzz')
            buzz = buzz + 1
        else:
            print(i)
    print('')
    print('Num Fizzed: ', fizz)
    print('Num Buzzed: ',buzz)
    print('Num Fizzbuzzed: ',fizzbuzz)

def main():
        fizzbuzz(17)

if __name__ == '__main__':
    main()