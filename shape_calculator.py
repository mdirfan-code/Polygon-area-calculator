class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    def get_area(self):
        return (self.width*self.height)
    def get_perimeter(self):
        return (2*self.width + 2*self.height)
    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width,self.height)
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    def get_picture(self):
        if(self.height > 50 or self.width >50 ):
            return "Too big for picture."
        shape=""
        for _ in range(self.height):
            for o in range(self.width):
                shape+="*"
            shape+="\n"
        return shape
    def get_amount_inside(self,inshape):
        return (self.get_area()//inshape.get_area())
        




class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_side(self,side):
        self.set_height(side)
        self.set_width(side)
    def __str__(self):
        return "Square(side={})".format(self.width)
