import random

from grid import Grid, Point
from ship import Fleet, Ship

class Player(object):
    """Represents on player on the board.
    An abstract class for students to implement.
    """

    def PlayerName(self):
        pass

    """ Return a Point where the next strike should be placed.
    """
    def NextStrike(self):
        pass

    """ Return a fleet to start the game with.
    """
    def StartingFleet(self):
        pass

class ManualPlayer(Player):
    def __init__(self, name):
        self.name = name

    def PlayerName(self):
        return self.name

    def StartingFleet(self):
        return Fleet([
            Ship((Point(1, "A"), Point(2, "A"))),
            Ship((Point(1, "B"), Point(2, "B"), Point(3, "B"))),
            Ship((Point(1, "C"), Point(2, "C"), Point(3, "C"), Point(4, "C"))),
            Ship((Point(1, "D"), Point(2, "D"), Point(3, "D"), Point(4, "D"), Point(5, "D"))),
        ])

    def NextStrike(self):
        rawInput = raw_input("Please enter an x, y ")
        rawX, rawY = (s.strip() for s in rawInput.split(','))
        if not rawX.isdigit():
            print "The value: ", rawX, "isn't valid"
            return self.NextStrike()
        x = int(rawX)
        if x not in range(1,11):
            print "The value: ", x, "isn't valid"
            return self.NextStrike()
        y = rawY.upper()
        if y not in "ABCDEFGHIJ":
            print "The value: ", y, "isn't valid"
            return self.NextStrike()

        return Point(x, y)

class RandomPlayer(Player):
    def __init__(self, name):
        self.name = name + "(random)"
        self.availableMoves = list(Grid.IterAllPoints())

    def PlayerName(self):
        return self.name

    def findValidShip(self, availablePoints, length):
        pt = random.choice(availablePoints)
        ships = Grid.GetAdjacent(length, pt.x, pt.y)
        ship = random.choice(ships)
        if all(pt in availablePoints for pt in ship):
            return ship
        else:
            return self.findValidShip(availablePoints, length)

    def StartingFleet(self):
        out = []
        availablePoints = list(Grid.IterAllPoints())
        for i in range(1,5):
            validShip = self.findValidShip(availablePoints, i)
            for pt in validShip:
                availablePoints.remove(pt)
            out.append(Ship(validShip))

        return Fleet(out)

    def NextStrike(self):
        pt = random.choice(self.availableMoves)
        self.availableMoves.remove(pt)
        return pt
