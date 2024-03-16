import random
import copy

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
            if 1 <= inp <= 36 and isValid(board, inp, currentPlayer):
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
    
def isValid(board, inp, currentPlayer):
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
    global posA
    global posB
    global gameRunning

    if (currentPlayer == "B"):
        pos = posA
    else:
        pos = posB

    # Bordpositie opsplitsen in een row en col
    pos_row, pos_col = divmod(pos, 6)

    # Omliggende vakjes definiëren
    surrounding = [      
        [pos_row, pos_col - 1],         # links
        [pos_row, pos_col + 1],         # rechts     
        [pos_row - 1, pos_col],         # boven  
        [pos_row - 1, pos_col - 1],     # linksboven  
        [pos_row - 1, pos_col + 1],     # rechtsboven    
        [pos_row + 1, pos_col],         # beneden      
        [pos_row + 1, pos_col - 1],     # linksbeneden    
        [pos_row + 1, pos_col + 1]]     # rechtsbeneden
    
    for square in surrounding:
        row, col = square
        if row < 0 or row > 5 or col < 0 or col > 5:
            continue
        if board[convert(row, col)] == "-":
            return False

    return True

def switchPlayer():
    global currentPlayer
    if (currentPlayer == "A"):
        currentPlayer = "B"
    else:
        currentPlayer = "A"

# Een row en col omzetten naar een bordpositie
def convert(row, col):
    return row * 6 + col

def scoreBot(board):
    global posA
    global posB

    if currentPlayer == "B":
        pos = posB 
    else: 
        pos = posA
    moves = {}
    maxMove = None
    maxScore = 0

    # Alle mogelijke zetten ophalen
    for square in range(0, len(board)):
        if isValid(board, square + 1, currentPlayer):
            moves.update({square: 0})
    
    # Alle mogelijke zetten simuleren en evalueren op basis van score (vrije buren)
    for move in moves.keys():
        board2 = copy.deepcopy(board)
        score = 0
        board2[move] = currentPlayer
        board2[pos] = "X"

        # Bordpositie opsplitsen in een row en col
        move_row, move_col = divmod(move, 6)

        neighbors = [      
            [move_row, move_col - 1],         # links
            [move_row, move_col + 1],         # rechts     
            [move_row - 1, move_col],         # boven  
            [move_row - 1, move_col - 1],     # linksboven  
            [move_row - 1, move_col + 1],     # rechtsboven    
            [move_row + 1, move_col],         # beneden      
            [move_row + 1, move_col - 1],     # linksbeneden    
            [move_row + 1, move_col + 1]]     # rechtsbeneden

        for neighbor in neighbors:
            if 0 <= neighbor[0] < 6 and 0 <= neighbor[1] < 6:
                if board2[convert(neighbor[0], neighbor[1])] == "-":
                    score += 1

        moves.update({move: score})
    
    for move, score in moves.items():
        if score >= maxScore:
            maxMove = move
            maxScore = score

    board[pos] = "X"
    posB = maxMove
    board[maxMove] = currentPlayer
    switchPlayer()

def randomBot(board):
    global posB

    while currentPlayer == "B":
        position = random.randint(1, 36)
        if isValid(board, position, currentPlayer):           
            board[posB] = "X"
            posB = position - 1
            board[position - 1] = currentPlayer
            switchPlayer()

while gameRunning:       
    printBoard(board)
    playerInput(board)
    if checkWin(board, currentPlayer):
        break       
    switchPlayer()
    if checkWin(board, currentPlayer):
        break
    scoreBot(board)
    if checkWin(board, currentPlayer):
        break  
    
printBoard(board)
print(f"{currentPlayer} heeft gewonnen!")
