class Rectangle:
    def __init__(self, length, width=None):
        # If only one argument is provided, assume it's a square
        if width is None:
            self.length = length
            self.width = length
        else:
            self.length = length
            self.width = width

    def area(self):
        return self.length * self.width

# Test cases
# Creating a square with one argument
square = Rectangle(5)
print("Square area:", square.area())  # Output: 25

# Creating a rectangle with two arguments
rectangle = Rectangle(5, 10)
print("Rectangle area:", rectangle.area())  # Output: 50
