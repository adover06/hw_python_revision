class Base:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        

class Circle(Base): #added the Base class as a parent class
    def __init__(self, x, y, size): #added the y paramerter
        super().__init__(x, y, size) #pass the values to the parent constructor
        
    def shape(self): #returns the shape type
        return "This is a square"
    def draw(self):
        return f"""
({self.x}, {self.y})\n{self.size}"""

def main():
    c = Circle(2,3,5)
    print(c.shape())
    print(c.draw())


main()