"""
extension.py
TODO: AI for game of NIMM. Nimm will always win the game.
The target of the game is to make the opponent pick the last stone
"""
import random 

def main():
    s = 20
    p = '1'
    print("Computer removes 1 stone")
    s = s - 1
    """
    Computer will keep on giving the player losing levels which are in
    the form of 3n+1. No matter what the player chooses computer will keep
    sending them to the next losing level
    """
    while(s >= 1):
        print("There are",s,"stones left")
        if p == 'computer':
            if n == 1:
                s = s - 2
                print("Computer removes 2 stones")
            else:
                s = s - 1
                print("Computer removes 1 stone")
        else:
            n = int(input("Player"+p+" would you like to remove 1 or 2 stones? "))
            while n != 1 and n != 2:
                n=int(input("Please enter 1 or 2: "))
            if n <= s:
                s = s - n
            else:
                while n != 1:
                   n = int(input("Please enter a number less than number of stones ")) 
        if p == 'computer':
            p = '1'
        else:
            p = 'computer'
        print()
    print("Player",p,"wins!")

if __name__ == "__main__":
    main()