"""
TODO: We execute the exercise() fonction as long as we haven't got 3 good answer in a row
"""

import random

def main():
    rand1 = random.randint(0, 100)
    rand2 = random.randint(0, 100)
    res = rand1 + rand2
    print('What is ',rand1,' + ',rand2,'?')
    ans = int(input('Your answer: '))
    streak = 0
    while streak != 3:
        if ans == res:
            streak = streak + 1
            print("Correct! You've gotten "+str(streak)+" correct in a row. ")
        else:
            streak = 0
            print("Incorrect. The expected answer is",res)
    print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()