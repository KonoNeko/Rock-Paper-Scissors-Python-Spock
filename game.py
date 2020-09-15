import enum
import random


class Elements(enum.Enum):
    Rock = 0
    Spock = 1
    Paper = 2
    Python = 3
    Scissors = 4


'''
A function that takes two player's name and return the Winner Name
@:param1 p1: str
@:param2 p2: str
@:return str
'''


def player_result(p1: str, p2: str) -> str:
    # get two random enums
    player1_result = random.choice(list(Elements))
    player2_result = random.choice(list(Elements))

    # calculate the difference of 2 enum values
    differ = (player1_result.value - player2_result.value) % 5

    # check if the player1 win
    if (differ == 1) or (differ == 2):
        print(p1 + " = " + str(player1_result.name) + "\n" + p2 + " = "
              + str(player2_result.name) + "\n" + p1 + " is the Winner\n")
        return p1

    # check if the player2 win
    if (differ == 3) or (differ == 4):
        print(p1 + " = " + str(player1_result.name) + "\n" + p2 + " = "
              + str(player2_result.name) + "\n" + p2 + " is the Winner\n")
        return p2

    # check when its tie, get the new winner
    while differ == 0:
        player1_result = random.choice(list(Elements))
        player2_result = random.choice(list(Elements))
        differ = (player1_result.value - player2_result.value) % 5
        if (differ == 1) or (differ == 2):
            print(p1 + " = " + str(player1_result.name) + "\n" + p2 + " = "
                  + str(player2_result.name) + "\n" + p1 + " is the Winner\n")
            return p1
        if (differ == 3) or (differ == 4):
            print(p1 + " = " + str(player1_result.name) + "\n" + p2 + " = "
                  + str(player2_result.name) + "\n" + p2 + " is the Winner\n")
            return p2