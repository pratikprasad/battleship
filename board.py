from grid import Grid, Point
from ship import Fleet, Ship

STRIKE = "STRIKE"
SHIP = "SHIP"
NONE = "NONE"

class ShipBoard(object):
    """A board to track a fleet of ships"""

    def __init__(self, fleet):
        super(ShipBoard, self).__init__()
        self.fleet = fleet
        self.grid = Grid()
        self.receivedStrikes = set()

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

    """ Receive a strike at the given coordinates:
    Args:
        x - a valid x coordinate
        y - a valid y coordinate
    Returns:
        True iff the point corresponds to a hit ship.
    """
    def ReceiveStrike(self, x, y):
        strike = Point(x, y)
        self.receivedStrikes.add(strike)

        value = self.grid.Get(x, y)
        return value != None

    """True iff we've received a strike for every ship in the fleet.
    """
    def IsFleetSunk(self):
        for ship in self.fleet:
            for point in ship:
                if point not in self.receivedStrikes:
                    return False
        return True

    def GetPositionType(self, point):
        if point in self.receivedStrikes:
            return STRIKE
        gridValue = self.grid.Get(point.x, point.y)
        if type(gridValue) == Ship:
            return SHIP

        return NONE


def DisplayBoard(board):
    out = "  A  B  C  D  E  F  G  H  I  J \n"
    for i, point in enumerate(board.grid.IterAllPoints()):
        if (i) % 10 == 0:
            out += str((i/10)+1)
            if (i/10 + 1) != 10:
                out += " "
        itemType = board.GetPositionType(point)
        if itemType == STRIKE:
            out += " X "
        elif itemType == SHIP:
            out += " O "
        else:
            out += " . "

        if (i+1) % 10 == 0:
            out += "\n"

    return out