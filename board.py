from grid import Grid, Point
from ship import Fleet, Ship

STRUCK_SHIP = "STRUCK_SHIP"
STRIKE = "STRIKE"
SHIP = "SHIP"
NONE = "NONE"

class PrintableBoard(object):
    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        out = "   A  B  C  D  E  F  G  H  I  J \n"
        for i, point in enumerate(Grid.IterAllPoints()):
            if (i) % 10 == 0:
                out += str((i/10)+1)
                if (i/10 + 1) != 10:
                    out += " "
            itemType = self.getPositionType(point)
            if itemType == STRUCK_SHIP:
                out += " H "
            elif itemType == STRIKE:
                out += " X "
            elif itemType == SHIP:
                out += " O "
            else:
                out += " . "

            if (i+1) % 10 == 0:
                out += "\n"

        return out

class ShipBoard(PrintableBoard):
    """A board to track a fleet of ships"""

    def __init__(self, fleet):
        super(ShipBoard, self).__init__()
        self.fleet = fleet
        self.grid = Grid()
        self.recordedStrikes = set()

        if type(fleet) is not Fleet:
            raise Exception("Expected a Fleet of ships, and instead got: ", type(fleet))

        for ship in fleet:
            self.addShip(ship)

    def addShip(self, ship):
        for point in ship:
            x, y = point.x, point.y
            ok = self.grid.Put(x, y, ship)
            if not ok:
                raise Exception("Unable to place ship at", x, y, ". Grid contains", self.grid.Get(x, y))

    """True iff we've received a strike for every ship in the fleet.
    """
    def IsFleetSunk(self):
        for ship in self.fleet:
            for point in ship:
                if point not in self.recordedStrikes:
                    return False
        return True

    """ Receive a strike at the given coordinates:
    Args:
        x - a valid x coordinate
        y - a valid y coordinate
    Returns:
        True iff the point corresponds to a hit ship.
    """
    def RecordStrike(self, x, y):
        strike = Point(x, y)
        self.recordedStrikes.add(strike)

        value = self.grid.Get(x, y)
        return (value is not None)


    def getPositionType(self, point):
        isStrike = point in self.recordedStrikes
        gridValue = self.grid.Get(point.x, point.y)
        isShip = type(gridValue) == Ship

        if isStrike and isShip:
            return STRUCK_SHIP
        elif isShip and not isStrike:
            return SHIP
        elif not isShip and isStrike:
            return STRIKE
        else:
            return NONE

class StrikeBoard(PrintableBoard):
    def __init__(self):
        self.recordedStrikes = dict()

    def RecordStrike(self, x, y, isHit):
        point = Point(x, y)
        self.recordedStrikes[point] = isHit

    def GetPositions(self):
        return dict(self.recordedStrikes)

    def getPositionType(self, point):
        if point in self.recordedStrikes:
            if self.recordedStrikes[point]:
                return STRUCK_SHIP
            else:
                return STRIKE
        else:
            return NONE

