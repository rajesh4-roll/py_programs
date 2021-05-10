"""
    File: Nimm.py
    -------------------------
    This program plays Nimm 
    game between two players.
"""

def main():
    stones = 20
    player = "Player 1 "
    while stones > 0:
        print("There are {} stones left".format(stones))
        remove_stones = int(
            input(player + "would you like to remove 1 or 2 stones? "))
        stones = calculate_stones(stones, remove_stones)
        player = rotate_player(player)
        print('')
    print(player + "wins!")

# calculate new stone numbers
def calculate_stones(x, y):
    # if input invalid
    while y < 1 or y > 2:
        y = int(input("Please enter 1 or 2: "))
    # if valid inputs
    stones = x - y
    return stones

# change players
def rotate_player(player):
    if player == "Player 1 ":
        return "Player 2 "
    else:
        return "Player 1 "

if __name__ == '__main__':    
    main()
