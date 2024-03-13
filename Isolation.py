EMPTY = "-"
PLAYER_A = "A"
PLAYER_B = "B"

# Initialize the board
def initializeBoard():
    global PLAYER_A
    global PLAYER_B
    return [[EMPTY for _ in range(6)] for _ in range(6)]

def printBoard(board):
    for row in board:
        print(" | ".join(row))

def isValid(board, row, col, player):
    if not (0 <= row < 6 and 0 <= col < 6):
        return False  # Move is out of bounds

    if board[row][col] != EMPTY:
        return False  # Square is not empty

    return True

def updateBoard(board, row, col, player):
    board[row][col] = player

def checkWin(board, player):
    # Implement win condition check here
    pass

def switchPlayer(currentPlayer):
    return PLAYER_B if currentPlayer == PLAYER_A else PLAYER_A

# Main game loop
def playGame():
    board = initializeBoard()
    board[0][0] = PLAYER_A
    board[5][5] = PLAYER_B
    currentPlayer = PLAYER_A

    while True:
        printBoard(board)
        row = int(input(f"Enter row (1-6) for player {currentPlayer}: ")) - 1
        col = int(input(f"Enter column (1-6) for player {currentPlayer}: ")) - 1

        if isValid(board, row, col, currentPlayer):
            updateBoard(board, row, col, currentPlayer)
            if checkWin(board, currentPlayer):
                print(f"Player {currentPlayer} wins!")
                break
            current_player = switchPlayer(currentPlayer)
        else:
            print("Invalid move. Try again.")

playGame()
