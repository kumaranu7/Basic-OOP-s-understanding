class Square:
    def __init__(self, side):
        self.side = side
    
    def __mul__(self, side):
        return(4*square1.side * 4*square2.side)
        
square1 = Square(5)
square2 = Square(15)

print('The sum of squares is', square1*square2)

#     def __add__(self, side):
#         return(4*square1.side + 4*square2.side)
        
# square1 = Square(5)
# square2 = Square(15)

# print('The sum of squares is', square1+square2)