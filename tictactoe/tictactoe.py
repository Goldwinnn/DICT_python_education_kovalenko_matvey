board = ['➖', '➖', '➖',
         '➖', '➖', '➖',
         '➖', '➖', '➖']
current_player = "❌"
winner = None
game_running = True


def print_board(game_board):
    """Печатаем игровое поле"""
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2])
    print("-" * 13)
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5])
    print("-" * 13)
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8])


def player_input(game_board):
    """Выбор ячейки игроком"""
    while True:
        if current_player == "❌":
            inp = int(input("Enter a number 1-9  Player (❌) : "))
        else:
            inp = int(input("Enter a number 1-9 Player (⭕️) : "))
        if 1 <= inp <= 9 and game_board[inp - 1] == "➖":
            game_board[inp - 1] = current_player
            break
        else:
            if current_player == "❌":
                print("Oops! Try again! Player - (❌) ")
            else:
                print("Oops! Try again! Player - (⭕️) ")
            print_board(board)


def check_horizontal(game_board):
    """Проверяем победу по горизонтале"""
    global winner
    if (game_board[0] == game_board[1] == game_board[2] and game_board[0] != "➖") or (
            game_board[3] == game_board[4] == game_board[5] and game_board[3] != "➖") or (
            game_board[6] == game_board[7] == game_board[8] and game_board[6] != "➖"):
        winner = current_player
        return True


def check_row(game_board):
    """Проверяем победу в ряд"""
    global winner
    if (game_board[0] == game_board[3] == game_board[6] and game_board[0] != "➖") or (
            game_board[1] == game_board[4] == game_board[7] and game_board[1] != "➖") or (
            game_board[2] == game_board[5] == game_board[8] and game_board[2] != "➖"):
        winner = current_player
        return True


def check_diagonal(game_board):
    """Проверяем победу по диагонали"""
    global winner
    if (game_board[0] == game_board[4] == game_board[8] and game_board[0] != "➖") \
            or (game_board[2] == game_board[4] == game_board[6] and game_board[2] != "➖"):
        winner = current_player
        return True


def check_tie(game_board):
    """Проверяем ничью"""
    global game_running
    if "➖" not in game_board:
        print_board(game_board)
        print("Its a tie")
        game_running = False


def check_win():
    if check_diagonal(board) or check_horizontal(board) or check_row(board):
        print(f"The winner is {winner}")


def switch_player():
    """Смена игрока"""
    global current_player
    if current_player == "❌":
        current_player = "⭕️"
    else:
        current_player = "❌"


while game_running:
    print_board(board)
    if winner is not None:
        break
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
