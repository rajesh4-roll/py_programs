"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 
# max & min random number for random function
MAX_RANDOM = 100
MIN_RANDOM = 10

def main():
    ran1 = random.randint(MIN_RANDOM,MAX_RANDOM)
    ran2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    total = ran1 + ran2
    print("What is "+str(ran1)+" + "+str(ran2)+"?")
    answer = int(input("Your answer: "))
    if total == answer:
        print("Correct!")
    else:
        print("Incorrect. "+"The expected answer is "+str(total))

if __name__ == '__main__':
    main()