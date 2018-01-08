from collections import namedtuple
from grid import Grid, Point

ship = namedtuple("ship", ["points"])

class Ship(ship):
    """A ship - represented as a tuple of points"""

    def __init__(self, points):
        super(Ship, self).__init__(points)

        if type(points) is not tuple:
            raise Exception("A ship is a tuple of points. The value", points, "is not a tuple.")
        if len(points) < 2:
            raise Exception("This ship is too small, it needs more points", points)
        if len(points) > 5:
            raise Exception("This ship is too big, it needs fewer points", points)

        for p in points:
            if type(p) is not Point:
                raise Exception("A ship can be only made of points. The value", p, "is not a point.")
            Grid.RaiseExceptionForInvalidCoordinates(p.x, p.y)

        if not (len(set(p.x for p in points)) == 1 or len(set(p.y for p in points)) == 1):
            raise Exception("All the points in a ship must be in line", points)

        if not len(set(points)) == len(points):
            raise Exception("All the points in a ship must be unique", points)

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return self.points.__iter__()

class Fleet(object):
    """A fleet is a complete set of ships for the game of battleships"""

    def __init__(self, ships):
        if not set(range(2,6)) == set(len(s) for s in ships):
            raise Exception("The fleet needs to have exactly four ships, one of each of length 2, 3, 4, 5")

        self.ships = ships

    def __iter__(self):
        return self.ships.__iter__()


