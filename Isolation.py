# print bord

# invoer speler

# check win/lose/tie

# beurtwissel

board = ["A", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "B"]
currentPlayer = "A"
posA = 0
posB = 35
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4] + " | " + board[5]
           + "     " + " 1" + " | " + " 2" + " | " + " 3" + " | " + " 4" + " | " + " 5" + " | " + " 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | " + board[9] + " | " + board[10] + " | " + board[11]
          + "     " + " 7" + " | " + " 8" + " | " + " 9" + " | " + "10" + " | " + "11" + " | " + "12")
    print(board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] + " | " + board[16] + " | " + board[17]
          + "     " + "13" + " | " + "14" + " | " + "15" + " | " + "16" + " | " + "17" + " | " + "18")
    print(board[18] + " | " + board[19] + " | " + board[20] + " | " + board[21] + " | " + board[22] + " | " + board[23]
          + "     " + "19" + " | " + "20" + " | " + "21" + " | " + "22" + " | " + "23" + " | " + "24")
    print(board[24] + " | " + board[25] + " | " + board[26] + " | " + board[27] + " | " + board[28] + " | " + board[29]
          + "     " + "25" + " | " + "26" + " | " + "27" + " | " + "28" + " | " + "29" + " | " + "30")
    print(board[30] + " | " + board[31] + " | " + board[32] + " | " + board[33] + " | " + board[34] + " | " + board[35]
          + "     " + "31" + " | " + "32" + " | " + "33" + " | " + "34" + " | " + "35" + " | " + "36")

def playerInput(board):
    global posA
    global posB
    global currentPlayer
    while True:
        try:
            inp = int(input("Verplaatsen naar welk vak? (1-36): "))
            if 1 <= inp <= 36 and is_valid(board, inp, currentPlayer):
                break
            else:
                print("Ongeldige invoer. Probeer het opnieuw.")
        except ValueError:
            print("Ongeldige invoer. Probeer het opnieuw.")

    if (currentPlayer == "A"): 
            board[posA] = "X"
            posA = inp - 1
    else:
        board[posB] = "X"
        posB = inp - 1

    board[inp - 1] = currentPlayer            
    
def is_valid(board, inp, currentPlayer):
    global posA
    global posB
    newPos = inp - 1  
    
    if currentPlayer == "A":
        oldPos = posA
        otherPos = posB
    else:
        oldPos = posB
        otherPos = posA

    old_row, old_col = divmod(oldPos, 6)
    new_row, new_col = divmod(newPos, 6)
  
    # Check if the move is horizontally, vertically, or diagonally connected
    if (old_row == new_row or old_col == new_col or abs(old_row - new_row) == abs(old_col - new_col)):
        # Check if the new position is empty and not occupied by the other player
        if board[newPos] == "-" and newPos != otherPos:
            # Check if the path between oldPos and newPos is clear
            if old_row == new_row:  # Move is along the same row
                min_pos = min(oldPos, newPos)
                max_pos = max(oldPos, newPos)
                if all(board[pos] == "-" or pos == otherPos for pos in range(min_pos + 1, max_pos)):
                    return True
            elif old_col == new_col:  # Move is along the same column
                min_pos = min(oldPos, newPos)
                max_pos = max(oldPos, newPos)
                if all(board[pos] == "-" or pos == otherPos for pos in range(min_pos + 6, max_pos, 6)):
                    return True
            else:  # Move is along a diagonal
                # Determine direction of diagonal movement
                row_step = -1 if old_row > new_row else 1
                col_step = -1 if old_col > new_col else 1
                # Check if the path is clear along the diagonal
                check_pos = oldPos + row_step * 6 + col_step
                while check_pos != newPos:
                    if board[check_pos] != "-":
                        return False
                    check_pos += row_step * 6 + col_step
                return True
    return False

def checkWin(board, currentPlayer):
    global posA
    global posB
    if currentPlayer == "A":
        player_pos = posB
    else:
        player_pos = posA

    # Convert position to row and column indices
    row, col = divmod(player_pos - 1, 6)

    # Check if all neighboring positions are occupied
    for dr in range(-1, 2):
        for dc in range(-1, 2):
            if (0 <= row + dr < 6 and 0 <= col + dc < 6 and
                    (dr != 0 or dc != 0) and board[(row + dr) * 6 + col + dc] == "-"):
                return False  # At least one neighboring position is empty
    return True  # All neighboring positions are occupied

def switchPlayer():
    global currentPlayer
    if (currentPlayer == "A"):
        currentPlayer = "B"
    else:
        currentPlayer = "A"

while gameRunning:       
    printBoard(board)
    playerInput(board)
    checkWin(board, currentPlayer)
    switchPlayer()
    checkWin(board, currentPlayer)
