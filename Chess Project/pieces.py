class Pawn:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.squaresMoved = 0
        self.name = f"{self.color[0].upper()}P"

class Rook:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = f"{self.color[0].upper()}R"

class Knight:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = f"{self.color[0].upper()}N"

class Bishop:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = f"{self.color[0].upper()}B"

class Queen:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = f"{self.color[0].upper()}Q"

class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.name = f"{self.color[0].upper()}K"