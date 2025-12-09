class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        

class Square(Base): #added the Base class as a parent class
    def __init__(self, x, y, size): #added the y paramerter
        super().__init__(x, y, size) #pass the values to the parent constructor
        
    def shape(self): #returns the shape type
        return "This is a square"
    def draw(self):
        return f"({self.x}, {self.y})\n{self.size}"

def main():
    s = Square(2, 3, 5)
    print(s.shape())
    print((s.x, s.y))
    print(s.size)
main()