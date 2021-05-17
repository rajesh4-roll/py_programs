def main():
    # a = common(x,y,z)
    # print(a)
    common('', 'T', 'A')
    # print(best)
    

def common(x,y,z):
    lst1 = ['A','T','C','G']
    lst2 = [x,y,z]
    for i in range(len(lst2)):
        if lst2[i] in lst1:
            a = lst2[i]
    b = a
    print(b)

if __name__ == '__main__':
    main()