"""
    File: khansole-academy.py
    ------------------------------
    This program generates the random number, add them and give user
    to guess the answer and display the no. of correct answer
"""

import random 
MAX_RANDOM = 100
MIN_RANDOM = 10

def main():
    count = 0
    while count != 3:
        ran1 = random.randint(MIN_RANDOM,MAX_RANDOM)
        ran2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        total = ran1 + ran2
        print("What is "+str(ran1)+" + "+str(ran2)+"?")
        answer = int(input("Your answer: "))
        if answer == total:
            count = count + 1
            print("Correct! "+"You've gotten "+str(count)+" in a row.")
        else:
            print("Incorrect. "+"The expected answer is "+str(total)) 
            count = 0 # it reset the value if 3 in correct if made
    if count == 3:
        print("Congratulations! You mastered addition.")

if __name__ == '__main__':
    main()