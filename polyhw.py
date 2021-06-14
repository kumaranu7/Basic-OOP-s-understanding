class Square:
    def __init__(self, side):
        self.side = side
    def __pow__(square1, square2):
        return (square1.side**square2.side)

square1 = Square(2)
square2 = Square(4)

print("The result is:", square1**square2)