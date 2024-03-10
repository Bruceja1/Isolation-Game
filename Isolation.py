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
posA = 1
posB = 36
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8] + " | " + board[9] + " | " + board[10] + " | " + board[11])
    print(board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] + " | " + board[16] + " | " + board[17])
    print(board[18] + " | " + board[19] + " | " + board[20] + " | " + board[21] + " | " + board[22] + " | " + board[23])
    print(board[24] + " | " + board[25] + " | " + board[26] + " | " + board[27] + " | " + board[28] + " | " + board[29])
    print(board[30] + " | " + board[31] + " | " + board[32] + " | " + board[33] + " | " + board[34] + " | " + board[35])

def playerInput(board):
    global posA
    inp = int(input("Verplaatsen naar welk vak? (1-36): "))

    # In deze if moet nog een legal move conditie toegevoegd worden. (Alleen horizontaal, verticaal & diagonaal)
    if inp >= 1 and inp <= 36 and board[inp - 1 == "-"]:
        board[posA - 1] = "X"
        board[inp - 1] = currentPlayer     
        posA = inp
    else:
        print("Ongeldige zet")
                
def is_valid(board, inp, currentPlayer)
    global posA
    global posB
    newPos = inp  
    if (currentPlayer == "A"):
          oldPos = posA
    else:
          newPos = posB
    # if newPos is horizontally or vertically or diagonally connected to oldPos, return True

printBoard(board)
playerInput(board)
printBoard(board)

