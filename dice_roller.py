import random
"""
1. Add more inputs (like player or team name).
2. Store each player's roll totals in separate arrays.
3. Choose a dice-based game that you can fully simulate using python.
"""
def main():
    dice_rolls = int(input('How many dice would you like to roll?'))
    dice_size = int(input('How many sides are the dice?'))
    #dice_rolls = 2
    dice_sum = 0
    for i in range(dice_rolls):
        roll = random.randint(1,dice_size)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll} Critical Fail')
        elif roll == dice_size:
            print(f'You rolled a {roll} Critical Success!')
        else:
            print(f'You rolled a {roll}')
    
    print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
    main()
