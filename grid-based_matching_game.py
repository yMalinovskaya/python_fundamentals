#Initialize
from random import choice

def InitializeGrid(board):
    for i in range(8):
        for j in range(8):
            board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])


def Initialize(board):
    #Initialize game
    #Initialize grid
    InitializeGrid(board)
    #Initialize score
    global score
    score = 0
    global turn
    turn = 1



def ContinueGame(current_score, goal_score = 100):
    #Check to see if we should continue
    if (current_score >= goal_score):
        return False
    else:
        return True

def DrawBoard(board):
    print("\n\n\n")
    print("---------------------------------")
    for i in range(7,-1, -1):
        linetodraw = str(i + 1)
        for j in range(8):
            linetodraw += " | " + board[i][j]
        linetodraw += " |"
        print(linetodraw)
        print("---------------------------------")
    print("    a   b   c   d   e   f   g   h")
    global score
    print("Current Score: ", score)

def GetMove():
    #Get move from the user
    print("Enter the move by specifying the space and the direction (u, d, l, r). Spaces should list column then row.")
    print("For example, e3u would swap position e3 with the one above, and f7r would swap f7 to the right")
    move = input("Enter move: ")
    return move

def ConvertLetterToCol(Col):
    if Col == "a":
        return 0
    elif Col == "b":
        return 1
    elif Col == "c":
        return 2
    elif Col == "d":
        return 3
    elif Col == "e":
        return 4
    elif Col == "f":
        return 5
    elif Col == "g":
        return 6
    elif Col == "h":
        return 7
    else:
        #not a valid column!
        return -1

def SwapPieces(board, move):
    #Swap pieces on board according to move
    #Get original position
    origrow = int(move[1]) - 1
    origcol = ConvertLetterToCol(move[0])
    #Get adjacent position
    if move[2] == 'u':
        newrow = origrow + 1
        newcol = origcol
    elif move[2] == 'd':
        newrow = origrow - 1
        newcol = origcol
    elif move[2] == 'l':
        newrow = origrow
        newcol = origcol - 1
    elif move[2] == 'r':
        newrow = origrow
        newcol = origcol + 1
    #Swap objects in two positions
    temp = board[origrow][origcol]
    board[origrow][origcol] = board[newrow][newcol]
    board[newrow][newcol] = temp

def RemovePieces(board):
    #Create board to store removed pieces
    remove = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    #Go through rows
    for i in range(8):
        for j in range(6):
            if(board[i][j] == board[i][j + 1]) and (board[i][j] == board[i][j + 2]):
                remove[i][j] = 1;
                remove[i][j + 1] = 1;
                remove[i][j + 2] = 1;

    #Go through columns
    for j in range(8):
        for i in range(6):
            if(board[i][j] == board[i + 1][j]) and (board[i][j] == board[i + 2][j]):
                remove[i][j] = 1;
                remove[i + 1][j] = 1;
                remove[i + 2][j] = 1;

    #Eliminate those marked
    global score
    removed_any = False
    for i in range(8):
        for j in range(8):
            if remove[i][j] == 1:
                board[i][j] = 0
                score += 1
                removed_any = True
    return removed_any

def DropPieces(board):
    #Drop pieces to fill in blanks
    for j in range(8):
        #make list of pieces in the column
        listofpieces = []
        for i in range(8):
            if board[i][j] != 0:
                listofpieces.append(board[i][j])
        #copy that list into column
        for i in range(len(listofpieces)):
            board[i][j] = listofpieces[i]
        #fill in remainder of column with 0s
        for i in range(len(listofpieces), 8):
            board[i][j] = 0

def FillBlanks(board):
    #Fill blanks with random pieces
    for i in range(8):
        for j in range(8):
            if (board[i][j] == 0):
                board[i][j] = choice(['Q', 'R', 'S', 'T', 'U'])

def Update(board, move):
    SwapPieces(board, move)
    pieces_eliminated = True
    while pieces_eliminated:
        pieces_eliminated = RemovePieces(board)
        DropPieces(board)
        FillBlanks(board)

def DoRound(board):
    DrawBoard(board)
    #get move
    move = GetMove()
    #Update board
    Update(board, move)
    #Update turn number
    global turn
    turn += 1

score = 0
turn = 0
goalscore = 100
board = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

Initialize(board)

while ContinueGame(score, goalscore):
    DoRound(board)
