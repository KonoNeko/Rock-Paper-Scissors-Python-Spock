import game

player1 = ''
player2 = ''


# function that use to select gamemode and run the simulate_tournament
def game_stater(p1: str, p2: str):
    p1 = input("Please Enter The Name for player1: ")
    p2 = input("Please Enter The Name for player2: ")
    game_mode_selection = int(input("(1) Best of 3\n"
                                    + "(2) Best of 5\n"
                                    + "(3) Best of 7\n"))
    # set selection to number of games
    if game_mode_selection == 1:
        index = 3
    if game_mode_selection == 2:
        index = 5
    if game_mode_selection == 3:
        index = 7
    simulate_tournament(p1, p2, index)


# function that simulate the game
def simulate_tournament(p1: str, p2: str, mode: int):
    p1_counter = 0
    p2_counter = 0
    # loop for how many games will be played
    for i in range(mode):
        result = game.player_result(p1, p2)
        if result == p1:
            p1_counter += 1
        else:
            p2_counter += 1
    if p1_counter > p2_counter:
        print(p1 + " is the winner！！\n" + "final score: "
              + str(p1_counter) + " : " + str(p2_counter))
    else:
        print(p2 + " is the winner！！\n" + "final score: "
              + str(p2_counter) + " : " + str(p1_counter))


# display the menu and run the starter function
def game_menu(p1: str, p2: str):
    selection = input("Enter 1 to play Rock Paper Scissors Python Spock 0 to "
                      "exit\n"
                      + "(1) start\n"
                      + "(2) exit\n")
    if selection == "1":
        game_stater(p1, p2)
    if selection == "2":
        exit()
    else:
        print("\nYou Must Enter 1 or 2")
        game_menu(p1, p2)


# main function that run the program
if __name__ == '__main__':
    game_menu(player1, player2)
