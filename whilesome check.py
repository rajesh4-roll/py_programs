"""
    File: wholesome.py
    ------------------------
    this program is check wholesome machine
"""

AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)
    str1 = input()
    while str1 != AFFIRMATION:
        print("That was not the affirmation")
        print("Please type the following affirmation: " + AFFIRMATION)
        str1 = input()
    print("That's right! :)")

if __name__ == "__main__":
    main()
