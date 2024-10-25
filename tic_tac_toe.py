board =     [
        [" "," "," "],
        [" "," "," "],
        [" "," "," "]
    ]

def print_board():
    for i in range(3):
        print("+---+---+---+")
        for j in range(3):
            print("|", end=" ")
            print(board[i][j], end=" ")
        print("|")
    print("+---+---+---+")

def check_row(row):
    return (board[row][1] == board[row][0] and board[row][1] == board[row][2]) and board[row][0] != " "

def check_column(column):
    return (board[1][column] == board[0][column] and board[1][column] == board[2][column]) and board[0][column] != " "

def check_diagonals():
    return ((board[0][0] == board[1][1] and board[1][1] == board[2][2]) and board[0][0] != " ") or (board[1][1] == board[0][2] and board[0][2] == board[2][0]) and board[0][2] != " "


def main():
    player = "X"

    for i in range(9):

        print_board()

        if player == "X":
            player = "O"
        else:
            player = "X"

        while True:
            print("Player " + player + " plays! ")
            row = int(input("Choose a line: "))
            column = int(input("Choose a column: "))

            if row < 0 or row > 2:
                print("Row out of bounds(0-2).")
                continue
            elif column < 0 or column > 2:
                print("Column out of bounds(0-2).")
                continue
            elif board[row][column] != " ":
                print("Pick an empty box.")
                continue
            else:
                board[row][column] = player
                break

        winner = False
        for i in range(3):
            if check_row(i):
                winner = player
                break
            elif check_column(i):
                winner = player
                break
        if not winner:
            if check_diagonals():
                winner = player

        if winner:
            print_board()
            print("Player"+ player + " won!")
            break

    else:
        print_board()
        print("Draw")


main()