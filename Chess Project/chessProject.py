from pieces import *
from gameFunctions import *

################################################################################


################################################################################
# print 2d list nicely
def repr2dList(L):
    if (L == []): return '[]'
    output = [ ]
    rows = len(L)
    cols = max([len(L[row]) for row in range(rows)])
    M = [['']*cols for row in range(rows)]
    for row in range(rows):
        for col in range(len(L[row])):
            M[row][col] = repr(L[row][col])
    colWidths = [0] * cols
    for col in range(cols):
        colWidths[col] = max([len(M[row][col]) for row in range(rows)])
    output.append('[\n')
    for row in range(rows):
        output.append(' [ ')
        for col in range(cols):
            if (col > 0):
                output.append(', ' if col < len(L[row]) else '  ')
            output.append(M[row][col].rjust(colWidths[col]))
        output.append((' ],' if row < rows-1 else ' ]') + '\n')
    output.append(']')
    return ''.join(output)

# print 2d list
def print2d(list):
    print(repr2dList(list))
################################################################################

def startgame():
    player1 = input("Type name of player1:")
    plyaer2 = input("Type name of player2:")
    print("Let the game begin!")
    play()
################################################################################

def play():

    gameOver = False

    # Keeps track of white/black move
    turn = "white"

    # create board
    board = [ ([None] * 8) for i in range(8) ]
    visualBoard = [ ([None] * 8) for i in range(8) ]

    for i in range(8):

        # add white pawns
        board[6][i] = Pawn(6,i, "white")
            
        # add black pawns
        board[1][i] = Pawn(6,i, "black")

    # add white rooks
    board[7][0] = Rook(7,0, "white")
    board[7][7] = Rook(7,7, "white")
    # add black rooks
    board[0][0] = Rook(0,0, "black")
    board[0][7] = Rook(0,7, "black")

    # add white knights 
    board[7][1] = Knight(7,1, "white")
    board[7][6] = Knight(7,6, "white")

    # add black knights 
    board[0][1] = Knight(0,1, "black")
    board[0][6] = Knight(0,6, "black")

    # add white bishops
    board[7][2] = Bishop(7,2, "white")
    board[7][5] = Bishop(7,5, "white")

    # add black bishops
    board[0][2] = Bishop(0,2, "black")
    board[0][5] = Bishop(0,5, "black")

    # add white king/queen
    board[7][3] = Queen(7,3, "white")
    board[7][4] = King(7,4, "white")

    # add black king/queen
    board[0][3] = Queen(0,3, "black")
    board[0][4] = King(0,4, "black")

    # Move all pieces to visual board
    for i in range(8):
        for j in range(8):
            if board[i][j] == None:
                visualBoard[i][j] = None

            else:
                visualBoard[i][j] = board[i][j].name
    
    print2d(visualBoard)

    while gameOver == False:

        # white's turn #########################################################
        if turn == "white":

            # input move
            print("White to move!")
            moveFrom = input("Make your move from: ")
            moveTo = input("Make your move to: ")

            # check if move is legal
            while not (validString(moveFrom, moveTo) 
                       and validMove(moveFrom, moveTo, board, turn)):
                
                print("Invalid move, try again!")
                print("White to move!")
                moveFrom = input("Make your move from: ")
                moveTo = input("Make your move to: ")

            # translate from chess board coordinates to CPU coordinates
            moveFrom, moveTo = chessToCPU(moveFrom), chessToCPU(moveTo)

            # Record initial move if pawn
            if isinstance(board[moveFrom[0]][moveFrom[1]], Pawn):
                board[moveFrom[0]][moveFrom[1]].squaresMoved += 1
                print()

            # move the piece
            board[moveTo[0]][moveTo[1]] = board[moveFrom[0]][moveFrom[1]]
            board[moveFrom[0]][moveFrom[1]] = None
            print(board[moveTo[0]][moveTo[1]].squaresMoved)
            
            # check for checks and checkmates
            if inCheck(board, "black"):
                print("CHECK!")

            

            # print the visual
            for i in range(8):
                for j in range(8):
                    if board[i][j] == None:
                        visualBoard[i][j] = None

                    else:
                        visualBoard[i][j] = board[i][j].name
    
            print2d(visualBoard)

            # change turns
            turn = "black"

        # black's turn #########################################################
        elif turn == "black":
                        # input move
            print("Black to move!")
            moveFrom = input("Make your move from: ")
            moveTo = input("Make your move to: ")

            # check if move is legal
            while not (validString(moveFrom, moveTo) 
                       and validMove(moveFrom, moveTo, board, turn)):
                
                print("Invalid move, try again!")
                print("Black to move!")
                moveFrom = input("Make your move from: ")
                moveTo = input("Make your move to: ")

            # translate from chess board coordinates to CPU coordinates
            moveFrom, moveTo = chessToCPU(moveFrom), chessToCPU(moveTo)

            # Record initial move if pawn
            if isinstance(board[moveFrom[0]][moveFrom[1]], Pawn):
                board[moveFrom[0]][moveFrom[1]].squaresMoved += 1

            board[moveTo[0]][moveTo[1]] = board[moveFrom[0]][moveFrom[1]]
            board[moveFrom[0]][moveFrom[1]] = None

            for i in range(8):
                for j in range(8):
                    if board[i][j] == None:
                        visualBoard[i][j] = None

                    else:
                        visualBoard[i][j] = board[i][j].name
    
            print2d(visualBoard)

            turn = "white"



################################################################################

play()

