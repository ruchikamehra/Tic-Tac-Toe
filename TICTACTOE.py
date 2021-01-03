board = [".", ".", "."], [".", ".", "."], [".", ".", "."]
count = 0
check_winner = 0


def display_board():
    print("\n")
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2].format(".", ".", "."))
    print("-""|" + "-""|" + "-")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2].format(".", ".", "."))
    print("-""|" + "-""|" + "-")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2].format(".", ".", "."))
    print("\n")


def username_enter():
    global user1, user2
    user1 = input("enter the first user for X player")
    user2 = input("enter the second user for O player")


def player_check():
    global gamer
    print("who play first {0} or {1}".format(user1, user2))
    w = input()
    if w == user1 or w == user2:
        display_board()
        if w == user1:
            gamer = "X"
        elif w == user2:
            gamer = "O"
    else:
        print(" not a registered player,kindly write the name correctly")
        player_check()


def which_player_turn(user1, user2):
    if gamer == "X":
        print("player of current turn : {0}".format(user1))
    elif gamer == "O":
        print("player of current turn: {0}".format(user2))


def change_player():
    global gamer
    if gamer == "X":
        gamer = "O"
    elif gamer == "O":
        gamer = "X"


def input_row():
    global row
    row = int(input("enter your rows 0to2"))
    if row > 2:
        print("wrong row attempt try again")
        input_row()


def input_column():
    global col
    col = int(input("enter the columns 0to 2"))
    if col > 2:
        print("wrong user attempt try again ")
        input_column()


def space_full():
    if board[row][col] != ".":
        print("space is filled,kindly go back")
        input_row(), input_column()
        space_full()
        board[row][col] = gamer
    elif board[row][col] == ".":
        board[row][col] = gamer


def check_win():
    if board[0][0] == board[0][1] == board[0][2] == "X":  # row check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[1][0] == board[1][1] == board[1][2] == "X":  # 2 row check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[2][0] == board[2][1] == board[2][2] == "X":  # 3 row check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[0][0] == board[1][0] == board[2][0] == "X":  # 1 column check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[0][1] == board[1][1] == board[2][1] == "X":  # 2 column check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[0][2] == board[1][2] == board[2][2] == "X":  # 3 column check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "X":  # diagonal check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "X":  # diagonal check
        print("congratulations!!,{0} wins".format(user1))
        return 1
    elif board[0][0] == board[0][1] == board[0][2] == "O":  # row check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[1][0] == board[1][1] == board[1][2] == "O":  # 2 row check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[2][0] == board[2][1] == board[2][2] == "O":  # 3 row check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[0][0] == board[1][0] == board[2][0] == "O":  # 1 column check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[0][1] == board[1][1] == board[2][1] == "O":  # 2 column check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[0][0] == board[1][1] == board[2][2] == "O":  # diagonal check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    elif board[0][2] == board[1][1] == board[2][0] == "O":  # diagonal check
        print("congratulations!!,{0} wins".format(user2))
        return 1
    else:
        return 0


def play_again_check():
    global count
    choice = input("would you like to play again? (Y/N)")
    if choice == "Y":
        print("Good,lets play again")
        username_enter()
        for i in range(0, 3):
            for j in range(0, 3):
                board[i][j] = '.'
        count = 0
        playing_game()
    elif choice == "N":
        print("thank you for your time, bye ,bye")
    elif choice != "Y" or choice != "N":
        print(" {0} wrong input".format(choice))
        print("enter a valid statement")
        play_again_check()


game_still = True


def game_over():
    global game_still
    if count == 9:
        if check_win() == 1:
            play_again_check()
        else:
            game_still = False
            print("oops,it's a tie")
            play_again_check()


def playing_game():
    global count
    player_check()
    while game_still:
        check_winner = check_win()
        if check_winner == 1:
            play_again_check()
            break
        which_player_turn(user1, user2)
        if gamer == "X" or gamer == "O":
            input_row()
            input_column()
            space_full()
            change_player()
            display_board()
            count = count + 1
            game_over()


username_enter()
playing_game()
