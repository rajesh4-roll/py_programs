MAX_NUMBER = 100

def main():
    i = 0
    while i != MAX_NUMBER:
        i+=1
        a = odd_even(i)
        print(i,a)

def odd_even(x):
    if x % 2 == 0:
        return "is even"
    else:
        return "is odd"
if __name__ == '__main__':
    main()