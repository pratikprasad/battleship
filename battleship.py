# The final battleship game.
from collections import namedtuple
from time import sleep

from board import ShipBoard, StrikeBoard
from grid import Grid

"""A player is required to have a PlayerName, NextStrike, StartingFleet functions."""


def isPlayer(player):
    requiredFunctions = ["PlayerName", "NextStrike", "StartingFleet"]
    for requiredFunction in requiredFunctions:
        if not hasattr(player, requiredFunction):
            return False
        fn = getattr(player, requiredFunction)
        if not callable(fn):
            return False
    return True


playerContext = namedtuple("playerContext", ["player", "shipBoard", "strikeBoard"])


class Game(object):
    def __init__(self, player1, player2):
        if not isPlayer(player1):
            raise Exception("Player1 is not a valid player.")
        if not isPlayer(player2):
            raise Exception("Player2 is not a valid player.")

        # try:
        player1ShipBoard = ShipBoard(player1.StartingFleet())
        player1StrikeBoard = StrikeBoard()
        self.player1Context = playerContext(player1, player1ShipBoard, player1StrikeBoard)
        # except Exception as e:
        #     raise Exception("Error initializing player 1: ", e)

        try:
            player2ShipBoard = ShipBoard(player2.StartingFleet())
            player2StrikeBoard = StrikeBoard()
            self.player2Context = playerContext(player2, player2ShipBoard, player2StrikeBoard)
        except Exception as e:
            raise Exception("Error initializing player 2: ", e)

    def Play(self, delay):
        for i in range(2*len(list(Grid.IterAllPoints()))):
            if delay:
                sleep(delay)
            current = self.player1Context if i % 2 == 0 else self.player2Context
            other = self.player1Context if i % 2 == 1 else self.player2Context

            def arrangeBoards():
                out = "Player1: " + self.player1Context.player.PlayerName() + 40 * " " + "Player2: " + self.player2Context.player.PlayerName() + "\n"
                p1strikes = self.player1Context.strikeBoard.__repr__().split("\n")
                p1ships = self.player1Context.shipBoard.__repr__().split("\n")
                p2strikes = self.player2Context.strikeBoard.__repr__().split("\n")
                p2ships = self.player2Context.shipBoard.__repr__().split("\n")
                for i in range(len(p1strikes)):
                    out += p1strikes[i] + " " * 20 + p2strikes[i] + "\n"
                for i in range(len(p1ships)):
                    out += p1ships[i] + " " * 20 + p2ships[i] + "\n"
                return out

            try:
                print arrangeBoards()
                print "Make your move: ", current.player.PlayerName()
                nextStrike = current.player.NextStrike(current.strikeBoard.GetPositions())
                isHit = other.shipBoard.RecordStrike(nextStrike.x, nextStrike.y)
                current.strikeBoard.RecordStrike(nextStrike.x, nextStrike.y, isHit)
                print arrangeBoards()
                if other.shipBoard.IsFleetSunk():
                    return current.player
            except Exception as e:
                raise Exception("Error playing turn for", str(current.player.PlayerName()), e)
