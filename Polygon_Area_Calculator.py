class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return self.width * 2 + self.height * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        picture = ''
        for i in range(self.height):
            picture += ''.join(['*' for j in range(self.width)]) + '\n'
        return picture
    
    def get_amount_inside(self, other):
        across = self.width // other.width
        down = self.height // other.height
        return across * down

class Square(Rectangle):
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.width})'
        
    def __init__(self, side):
        self.width = side
        self.height = side
        super().__init__(self.width, self.height)

    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(Rectangle(4,8).get_amount_inside(Rectangle(3, 6)))