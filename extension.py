"""
    File: extension.py
    ------------------------------------------
    AI game of Nimm in which computer always wins. Player 1 always
    lose the game, no point except lose the game by any strategy.
"""

def main():
    total_stones = 20
    turn = 2
    print("Computer removes 1 stone")
    total_stones = total_stones - 1
    """
   
    """
    while(total_stones >= 1):
        print("There are",total_stones,"stones left")
        if turn == 1:
            if turn == 1:
                total_stones = total_stones - 2
                print("Computer removes 2 stones")
            else:
                total_stones = total_stones - 1
                print("Computer removes 1 stone")
            print('')
            turn = 2
        else:
            play1 = int(input("Player 1 would you like to remove 1 or 2 stones? "))
            while play1 != 1 and play1 != 2:
                play1 = int(input("Please enter 1 or 2: "))
            if play1 <= total_stones:
                total_stones = total_stones - play1
            else:
                while play1 != 1:
                   play1 = int(input("Please enter 1 or 2: ")) 
            print('')
            turn = 1
        if total_stones == 0 and turn == 1:
            print("Player Computer wins!")
        if total_stones == 0 and turn == 2:
            print("Player 2 wins!")

if __name__ == "__main__":
    main()