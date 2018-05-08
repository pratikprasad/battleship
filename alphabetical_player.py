from grid import Grid, Point
from player import RandomPlayer

class AlphabeticalPlayer(RandomPlayer):
    """Plays all the moves in an alphabetical order."""
    def __init__(self):
        self.name = "Alphabetical player"
        self.allPoints = sorted(list(Grid.IterAllPoints()), reverse=True)

    """ Return a Point where the next strike should be placed.
    This player plays all points in an alphabetical order.
    """
    def NextStrike(self, playedPoints):
        return self.allPoints.pop()

