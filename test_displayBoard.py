from unittest import TestCase
from grid import Point
from ship import Fleet, Ship
from board import ShipBoard


class TestDisplayBoard(TestCase):
    def test_DisplayBoard(self):
        f = Fleet([
            Ship((Point(1, "A"), Point(2, "A"))),
            Ship((Point(1, "B"), Point(2, "B"), Point(3, "B"))),
            Ship((Point(1, "C"), Point(2, "C"), Point(3, "C"), Point(4, "C"))),
            Ship((Point(1, "D"), Point(2, "D"), Point(3, "D"), Point(4, "D"), Point(5, "D"))),
        ])
        board = ShipBoard(f)
        self.assertEqual("   A  B  C  D  E  F  G  H  I  J \n"
                         "1  O  O  O  O  .  .  .  .  .  . \n"
                         "2  O  O  O  O  .  .  .  .  .  . \n"
                         "3  .  O  O  O  .  .  .  .  .  . \n"
                         "4  .  .  O  O  .  .  .  .  .  . \n"
                         "5  .  .  .  O  .  .  .  .  .  . \n"
                         "6  .  .  .  .  .  .  .  .  .  . \n"
                         "7  .  .  .  .  .  .  .  .  .  . \n"
                         "8  .  .  .  .  .  .  .  .  .  . \n"
                         "9  .  .  .  .  .  .  .  .  .  . \n"
                         "10 .  .  .  .  .  .  .  .  .  . \n", board.__repr__(), board)

        board.RecordStrike(4, "G")
        self.assertEqual("   A  B  C  D  E  F  G  H  I  J \n"
                         "1  O  O  O  O  .  .  .  .  .  . \n"
                         "2  O  O  O  O  .  .  .  .  .  . \n"
                         "3  .  O  O  O  .  .  .  .  .  . \n"
                         "4  .  .  O  O  .  .  X  .  .  . \n"
                         "5  .  .  .  O  .  .  .  .  .  . \n"
                         "6  .  .  .  .  .  .  .  .  .  . \n"
                         "7  .  .  .  .  .  .  .  .  .  . \n"
                         "8  .  .  .  .  .  .  .  .  .  . \n"
                         "9  .  .  .  .  .  .  .  .  .  . \n"
                         "10 .  .  .  .  .  .  .  .  .  . \n", board.__repr__(), board)
