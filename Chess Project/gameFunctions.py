from translations import *
from pieces import *
from copy import *

################################################################################

# checklegality
def validMove(moveFrom, moveTo, board, turn = None):

    # translate moves
    moveFrom = chessToCPU(moveFrom)
    moveTo = chessToCPU(moveTo)

    # check if piece moves to different square 
    if moveFrom == moveTo:
        return False

    # check if piece is moving from/to square on board
    if not (0 <= moveFrom[0] <= 7 and 0 <= moveFrom[1] <= 7 and
            0 <= moveTo[0] <= 7 and 0 <= moveTo[1] <= 7):
        return False

    fromPiece = board[moveFrom[0]][moveFrom[1]]
    toPiece = board[moveTo[0]][moveTo[1]] 




    # check if there is piece on beginning square
    if fromPiece == None:
        return False

    # check if piece is moving to square occupied by own piece
    if toPiece != None:
        if fromPiece.color == toPiece.color:
            return False



    ############################################################################
    # check each piece for valid move
    ############################################################################
    # pawn
    if isinstance(fromPiece, Pawn):
        if fromPiece.color == "white":

            # check for non-capture moves
            if abs(moveFrom[1] - moveTo[1]) == 0:

                # Check if moving onto another piece
                if toPiece != None:
                    return False

                # check if initial move valid

                if moveTo[0] - moveFrom[0] == -2:
                    if fromPiece.squaresMoved != 0:
                        return False

                    squaresBetween = findVerticalSquaresBetween(moveFrom,moveTo)

                    # check if pawn moving through another piece
                    if board[squaresBetween[0][0]][squaresBetween[0][1]] !=None:
                        return False
                
                return True

            # check for capture moves
            elif abs(moveFrom[1] - moveTo[1]) == 1:

                # capture moves must only move 1 forward
                if moveTo[0] - moveFrom[0] != -1:
                    return False

                # capture moves must capture something
                if board[moveTo[0]][moveTo[1]] == None:
                    return False

                # cannot capture own piece
                if fromPiece.color == toPiece.color:
                    return False
                
                return True

            else:
                return False


        elif fromPiece.color == "black":

            # check for non-capture moves
            if abs(moveFrom[1] - moveTo[1]) == 0:

                # Check if moving onto another piece
                if toPiece != None:
                    return False

                # check if initial move valid

                if moveTo[0] - moveFrom[0] == 2:
                    if fromPiece.squaresMoved != 0:
                        return False

                    squaresBetween = findVerticalSquaresBetween(moveFrom,moveTo)

                    # check if pawn moving through another piece
                    if board[squaresBetween[0][0]][squaresBetween[0][1]] !=None:
                        return False
                
                return True

            # check for capture moves
            elif abs(moveFrom[1] - moveTo[1]) == 1:

                # capture moves must only move 1 forward
                if moveTo[0] - moveFrom[0] != 1:
                    return False

                # capture moves must capture something
                if board[moveTo[0]][moveTo[1]] == None:
                    return False

                # cannot capture own piece
                if fromPiece.color == toPiece.color:
                    return False
                
                return True

            else:
                return False
    ############################################################################
    # rook
    elif isinstance(fromPiece, Rook):
            if ((moveTo[0] - moveFrom[0] != 0) and
                (moveTo[1] - moveFrom[1] != 0)):
                return False

            if moveTo[0] - moveFrom[0] == 0:
                inBetween = findHorizontalSquaresBetween(moveFrom, moveTo)
                if len(inBetween) != 0:
                    for coords in inBetween:
                        if board[coords[0]][coords[1]] != None:
                            return False

            elif moveTo[1] - moveFrom[1] == 0:
                inBetween = findVerticalSquaresBetween(moveFrom, moveTo)
                if len(inBetween):
                    for coords in inBetween:
                        if board[coords[0]][coords[1]] != None:
                            return False

            return True

    ############################################################################
    # knight
    elif isinstance(fromPiece, Knight):

            #check if knight move is valid
            if not ((abs(moveTo[1] - moveFrom[1]) == 1 and 
                abs(moveTo[0] - moveFrom[0]) == 2) or 
                (abs(moveTo[1] - moveFrom[1]) == 1 and 
                abs(moveTo[0] - moveFrom[0]) == 2)):
                return False

            return True

    ############################################################################
    # bishop
    elif isinstance(fromPiece, Bishop):
            
            # check if valid bishop move
            if abs(moveFrom[0] - moveTo[0]) != abs(moveFrom[1] - moveTo[1]):
                return False

            # check if any pieces are being hopped over
            inBetween = findDiagonalSquaresBetween(moveFrom, moveTo)
            if len(inBetween) != 0:
                for coords in inBetween:
                    if board[coords[0]][coords[1]] != None:
                        return False

            return True

    ############################################################################
    # queen
    elif isinstance(fromPiece, Queen):

            # check if valid queen move
            # check if queen moving through pieces

            if (moveFrom[0] - moveTo[0] == 0):

                inBetween = findHorizontalSquaresBetween(moveFrom, moveTo)
                if len(inBetween) != 0:
                    for coords in inBetween:
                        if board[coords[0]][coords[1]] != None:
                            return False
                return True

            elif (moveFrom[1] - moveTo[1] == 0):
                inBetween = findVerticalSquaresBetween(moveFrom, moveTo)
                if len(inBetween) != 0:
                    for coords in inBetween:
                        if board[coords[0]][coords[1]] != None:
                            return False
                return True

            elif (abs(moveFrom[0]-moveTo[0]) == abs(moveFrom[1]-moveTo[1])):
                inBetween = findDiagonalSquaresBetween(moveFrom, moveTo)
                
                if len(inBetween) != 0:
                    for coords in inBetween:
                        if board[coords[0]][coords[1]] != None:
                            return False
                return True

            else:
                return False

################################################################################
# check if input is valid string
def validString(moveFrom, moveTo):
    return (moveFrom[0].isalpha() and moveTo[0].isalpha() 
            and moveFrom[1].isnumeric() and moveTo[1].isnumeric()
            and len(moveTo) == len(moveFrom) == 2)

################################################################################
# translates from board coordinates to python list coordinates  
def chessToCPU(move):
    return (chessToCPUcoords[int(move[1])], chessToCPUcoords[move[0]])

# translates from python list coordinates to board coordinates
def CPUToChess(x, y):
    return (CPUToChessCoords1[y] + str(CPUToChessCoords2[x]))

    
# finds all squares in a direct line between two squares
def findVerticalSquaresBetween(moveFrom, moveTo):
    squares = []
    for i in range(min(moveFrom[0],moveTo[0]) + 1, max(moveFrom[0], moveTo[0])):
        squares.append((i, moveFrom[1]))

    return squares

def findHorizontalSquaresBetween(moveFrom, moveTo):
    squares = []
    for i in range(min(moveFrom[1],moveTo[1]) + 1, max(moveFrom[1], moveTo[1])):
        squares.append((moveFrom[0], i))

    return squares

# finds all squares in a diagonal between two squares
def findDiagonalSquaresBetween(moveFrom, moveTo):

    # set parameters
    squares = []
    horizontalDir = 0
    verticalDir = 0

    # check the directional of diagonal
    if moveTo[0] - moveFrom[0] < 0:
        verticalDir = -1

    elif moveTo[0] - moveFrom[0] > 0:
        verticalDir = 1

    if moveTo[1] - moveFrom[1] < 0:
        horizontalDir = -1

    elif moveTo[1] - moveFrom[1] > 0:
        horizontalDir = 1

    # set counter for iterations
    counter = 1

    # add squares and return them
    for i in range(abs(moveFrom[0] - moveTo[0])-1):
        
        newX = moveFrom[0] + verticalDir * counter 
        newY = moveFrom[1] + horizontalDir * counter
        squares.append((newX, newY))
        counter += 1

    return squares

################################################################################
# check if king is in check
def inCheck(board, color):

    oppositeColor = None

    if color == "white":
        oppositeColor = "black"

    elif color == "black":
        oppositeColor = "white"

    kingCoords = None
    for i in range(8):
        for j in range(8):
            cur = board[i][j]
            if cur != None:
                if isinstance(cur, King) and cur.color == color:
                    kingCoords = (i,j)

                    break

    kingChessCoords = CPUToChess(kingCoords[0], kingCoords[1])
    print(kingChessCoords)

    for i in range(8):
        for j in range(8):
            cur = board[i][j]
            if cur == None:
                continue
            if cur.color != color:
                curChessCoords = (CPUToChess(i, j))
                print(curChessCoords)
                


    return False

################################################################################
def inCheckmate(board, color):
    if not inCheck(board, color):
        return False

    newBoard = deepcopy(board)
    kingCoords = None

    for i in range(8):
        for j in range(8):
            if isinstance(newBoard[i][j], King):
                if newBoard[i][j].color == color:
                    kingCoords = (i, j)
                    break

    chessKingCoords = CPUToChess(kingCoords[0], kingCoords[1])

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            newKingCoords = (kingCoords[0] + i, kingCoords[1] + j)
            if newKingCoords[0] in range(8) and newKingCoords[1] in range(8):
                chessNewKingCoords=CPUToChess(newKingCoords[0],newKingCoords[1])
                if validMove(chessKingCoords,chessNewKingCoords,newBoard,color):
                    return False

    return True

################################################################################

def inStalemate(board, color):
    if inCheck(board, color):
        return False
    
    newBoard = deepcopy(board)
    kingCoords = None

    for i in range(8):
        for j in range(8):
            if isinstance(newBoard[i][j], King):
                if newBoard[i][j].color == color:
                    kingCoords = (i, j)
                    break

    chessKingCoords = CPUToChess(kingCoords[0], kingCoords[1])

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            newKingCoords = (kingCoords[0] + i, kingCoords[1] + j)
            if newKingCoords[0] in range(8) and newKingCoords[1] in range(8):
                chessNewKingCoords=CPUToChess(newKingCoords[0],newKingCoords[1])
                if validMove(chessKingCoords,chessNewKingCoords,newBoard,color):
                    return False

    return True
                
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
board = [ ([None] * 8) for i in range(8) ]
board[7][7] = King(7,7,"white")
board[6][6] = Queen(6,6, "black")
board[5][5] = King(7,7, "black")

visualBoard = [ ([None] * 8) for i in range(8) ]
for i in range(8):
        for j in range(8):
            if board[i][j] == None:
                visualBoard[i][j] = None

            else:
                visualBoard[i][j] = board[i][j].name
    
print2d(visualBoard)

print(inCheckmate(board, "black"))
print(inStalemate(board, "black"))



'''
    # check player is moving own piece
    if turn != None:
        if turn != fromPiece.color:
            return False

        # check if player is putting their own king in check
        newBoard = deepcopy(board)
        newBoard[moveTo[0]][moveTo[1]] = newBoard[moveFrom[0]][moveFrom[1]]
        newBoard[moveFrom[0]][moveFrom[1]] = None

        if inCheck(newBoard, turn):
            return False'''