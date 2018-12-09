import os


def board(size=3):
    grids = [["@"] * size for _ in range(size)]

    exp = []
    for x in range(1, 10):
        exp.append(x)

    grids[0] = exp[0:3]
    grids[1] = exp[3:6]
    grids[2] = exp[6:9]

    return grids


def printBoard(grids):
    os.system("clear")
    for row in grids:
        print(row)
        # //TODO:  pálya normálius kinézet


def playerChars():
    players = [0, 0]
    choosen = "x"  # input("choose one, X or O :")
    if choosen == "X" or choosen == "x":
        players[0] = "X"
        players[1] = "O"
    elif choosen == "O" or choosen == "o":
        players[0] = "O"
        players[1] = "X"

    print("player 1 is: "+players[0]+"\nplayer 2 is: "+players[1])

    return players


def turns(selected, board):
    turnTracker = 0
    for char in selected:
        placement = playerTurn(turnTracker)
        for x in range(3):
            if placement in board[x]:
                y = board[x].index(placement)
                break
        else:
            print("invalid input")
            break
        turnTracker += 1
        try:
            board[x][y] = char
            printBoard(board)
        except ValueError:
            print("PLS FIGYELJ ODA, NEM VOLT IDŐNK LEKEZELNI :D")

    return board


def playerTurn(turnTracker):
    if turnTracker == 0:
        player = "player 1 turn"
    elif turnTracker == 1:
        player = "player 2 turn"
    try:
        print("\n"+player)
        usr = int(input("select a number between 1-9: "))
    except ValueError:
        print("Invalid input, try again")
        print(player)
        usr = int(input("select a number between 1-9: "))
    return usr


def watcher(board):
    result = []
    for i, row in enumerate(board):
        if not not result:
            break
        tmp = []
        if row[0] is row[1] and row[1] is row[2]:
            print("row")
            result.append(row[0])
        for x in range(3):
            tmp.append(board[x][i])
        if tmp[0] is tmp[1] and tmp[1] is tmp[2]:
            print("colum")
            result.append(tmp[0])
        if board[0][0] is board[2][2] or board[0][2] is board[2][0]:
            for x in range(3):
                if board[1][1] is board[0][x] and board[1][1] is board[x][0]:
                    print("cross")
                    result.append(board[1][1])
                    break
    return result


if __name__ == "__main__":
    board = board()
    selected = playerChars()
    printBoard(board)
    while True:
        board = turns(selected, board)
        result = watcher(board)
        if not not result:
            print("The winner is : "+str(result))
            break
            