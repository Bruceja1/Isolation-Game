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
            inp = int(input(f"'{currentPlayer}' Verplaatsen naar welk vak? (1-36): "))
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

    if (old_row == new_row or old_col == new_col or abs(old_row - new_row) == abs(old_col - new_col)):
       
        if board[newPos] == "-" and newPos != otherPos:
            
            if old_row == new_row:  
                step = 1 if oldPos < newPos else -1
                for pos in range(oldPos + step, newPos, step):
                    if board[pos] != "-":
                        return False
            elif old_col == new_col: 
                step = 6 if oldPos < newPos else -6
                for pos in range(oldPos + step, newPos, step):
                    if board[pos] != "-":
                        return False
            else:  
                row_step = 1 if old_row < new_row else -1
                col_step = 1 if old_col < new_col else -1
                check_pos = oldPos + row_step * 6 + col_step
                while check_pos != newPos:
                    if board[check_pos] != "-":
                        return False
                    check_pos += row_step * 6 + col_step
            return True
    return False

def checkWin(board, currentPlayer):
    print("Ik ben nu aan het kijken of er een speler gewonnen heeft.")
    global posA
    global posB
    global gameRunning

    if (currentPlayer == "A"):
        pos = posA
    else:
        pos = posB

    topleft = board[pos - 7]
    topcenter = board[pos - 6]
    topright = board[pos - 5]

    bottomleft = board [pos + 5]
    bottomcenter = board[pos + 6]
    bottomright = board[pos + 7]

    left = board[pos - 1]
    right = board [pos + 1]

# Een lijst van alle posities direct om mij heen. Als minimaal één van deze leeg is "-",
# dan kan ik nog een zet maken.
    positions = [topleft, topcenter, topright, bottomleft, bottomcenter, bottomright, left, right]
    for position in positions:
        if position == "-":
            return False
        else:
            gameRunning = False
            return True
            
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

print(f"{currentPlayer} heeft gewonnen!")