from grid import Grid, Point

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
