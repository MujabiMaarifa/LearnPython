"""Lets define the propety decorator
    property method gives us the getter set deleter methods
    and can be used to add additional logic to our codes


"""

class Rectangle:
    def __init__(self, height, width) :
        self._height = height
        self._width = width

    """The attributes have to be set to private"""
    @property
    def height(self):
        return f"{self._height:.1f} cm"
    @property
    def width(self):
        return f"{self._width:.1f} cm"
    @width.setter
    def width(self, newWidth) :
        if newWidth > 0:
            self._width = newWidth
        else:
            print("width must be greater than zero")
    @height.setter
    def height(self, newHeight) :
        if newHeight > 0:
            self._height = newHeight
        else:
            print("height must be greater than zero")

    @width.deleter
    def Width(self) :
        del self._width
        print("width has been deleted")

    @height.deleter
    def Height(self) :
        del self._height
        print("height has been deleted")
rect = Rectangle(4, 5)
# rect.width = 0
# rect.height = -1
rect.width = 6
rect.height = 35
# print(rect)
# print(rect.height)
# print(rect.width)

del rect.Width
del rect.Height