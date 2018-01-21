from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

class Grid(object):
    """Represents one 10X10 grid in a game of battleship
    The values are addressable with [1-10]x[A-J] coordinates.
    """
    validXCoordinates = range(1,11)
    validYCoordinates = list("ABCDEFGHIJ")

    @staticmethod
    def GetAdjacent(length, x, y):
        out = []
        # Above
        if Grid.IsXValid(x-length):
            above = tuple(Point(xpt, y) for xpt in range(x-length, x+1))
            out.append(above)
        # Below
        if Grid.IsXValid(x+length):
            below = tuple(Point(xpt, y) for xpt in range(x, x+length+1))
            out.append(below)
        # Left
        ypos = Grid.validYCoordinates.index(y)
        if (ypos-length) >= 0:
            left = tuple(Point(x, Grid.validYCoordinates[pos]) for pos in range(ypos-length, ypos+1))
            out.append(left)
        # Right
        if (ypos+length) <= 9:
            right = tuple(Point(x, Grid.validYCoordinates[pos]) for pos in range(ypos, ypos+length+1))
            out.append(right)

        return out

    @staticmethod
    def IterAllPoints():
        for x in Grid.validXCoordinates:
            for y in Grid.validYCoordinates:
                yield Point(x, y)

    @staticmethod
    def IsXValid(x):
        return x in Grid.validXCoordinates

    @staticmethod
    def IsYValid(y):
        return y in Grid.validYCoordinates

    @staticmethod
    def RaiseExceptionForInvalidCoordinates(x, y):
        if not Grid.IsXValid(x):
            raise Exception("The given point doesn't have a valid x coordinate", x)
        if not Grid.IsYValid(y):
            raise Exception("The given point doesn't have a valid y coordinate", y)

    def __init__(self):
        super(Grid, self).__init__()
        self.store = dict()

    def __contains__(self, item):
        return item in self.store

    """ Places a value at the point in the grid
    Args:
        x - an x coordinate
        y - an y coordinate
    Exceptions:
        Raises an exception if the point is outside the grid
    Returns:
        Returns True if the point was placed successfully.
        Returns False if the point was not placed successfully
    """
    def Put(self, x, y, value):
        Grid.RaiseExceptionForInvalidCoordinates(x, y)

        point = Point(x, y)

        if point in self.store:
            return False

        self.store[point] = value
        return True

    """ Gets the value at the given point in the grid.
    Args:
        x - an x coordinate
        y - an y coordinate
    Returns:
        The value at the given (x, y) point in the grid if present,
        otherwise False
    """
    def Get(self, x, y):
        Grid.RaiseExceptionForInvalidCoordinates(x, y)
        point = Point(x, y)
        if point not in self.store:
            return None

        return self.store[point]

    def IterFilledPoints(self):
        return self.store.__iter__
