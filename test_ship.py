from collections import namedtuple
import unittest

from grid import Point
from ship import Ship

RegexTestCase = namedtuple("RegexTestCase", ["PointTuples", "ExceptionRegex"])

class TestShip(unittest.TestCase):

    def runTestCases(self, testCases):
        for case in testCases:
            points = tuple(Point(x, y) for (x, y) in case.PointTuples)
            if len(case.ExceptionRegex) > 0:
                self.assertRaisesRegexp(
                    Exception,
                    case.ExceptionRegex,
                    lambda: Ship(points))
            else:
                Ship(points)

    def test_tooSmall(self):
        self.runTestCases([
            RegexTestCase(
                [(1, "B")],
                "This ship is too small, it needs more points"),
            RegexTestCase(
                [(2, "B"), (3, "B")],
                "")
            ])

    def test_tooBig(self):
        self.runTestCases([
            RegexTestCase(
                [(1, "B"), (1, "C"), (1, "D"), (1, "E"), (1, "F"),(1, "G")],
                "This ship is too big, it needs fewer points"),
            RegexTestCase(
                [(1, "B"), (1, "C"), (1, "D"), (1, "E"), (1, "F")],
                "")
            ])

    def test_ValidPoints(self):
        self.runTestCases([
            RegexTestCase(
                [(12, "B"), (1, "D"), (1, "E"), (1, "F"),(1, "G")],
                "The given point doesn't have a valid x coordinate"),
            RegexTestCase(
                [(1, "B"), (1, "C"), (1, "D"), (1, "E"), (1, "F")],
                "")
            ])

    def test_PointsInLine(self):
        self.runTestCases([
            RegexTestCase(
                [(1, "B"), (2, "C"), (1, "D"), (1, "E"), (1, "F")],
                "All the points in a ship must be in line"),
            RegexTestCase(
                [(1, "B"), (1, "C"), (1, "D"), (1, "E"), (1, "F")],
                "")
            ])

    def test_unique(self):
        self.runTestCases([
            RegexTestCase(
                [(1, "B"), (2, "B"), (1, "B")],
                "All the points in a ship must be unique"),
            RegexTestCase(
                [(1, "B"), (2, "B"), (3, "B")],
                "")
            ])


if __name__ == "__main__":
    unittest.main()
