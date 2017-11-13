#Here's a simple class for an (x, y) coordinate pair:

class Point:
    "" "
    Point on a plane.
    """

    def __init__(self x, y):
        self.x=x
        self.y=y
    def __repr__(self):
        return "{cls}({x:.of},{y:.of}).format(
            cls=self.__class__.__name__, x=self.x,y=self.y)
    
