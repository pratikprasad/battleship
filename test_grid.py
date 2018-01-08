import unittest

from grid import Grid, Point

class TestGrid(unittest.TestCase):

    def test_all_valid_points(self):
        self.assertEqual(
            set(Point(x, y)
                for x in range(1,11)
                for y in "ABCDEFGHIJ"),
            set(Grid.IterAllPoints()))

    def test_invalid_insert(self):
        g = Grid()
        self.assertRaisesRegexp(Exception,
         "The given point doesn't have a valid x coordinate",
         lambda: g.Put(-1, "A", ""))
        self.assertRaisesRegexp(Exception,
         "The given point doesn't have a valid x coordinate",
         lambda: g.Put(11, "A", ""))
        self.assertRaisesRegexp(Exception,
         "The given point doesn't have a valid y coordinate",
         lambda: g.Put(1, "K", ""))
        self.assertRaisesRegexp(Exception,
         "The given point doesn't have a valid y coordinate",
         lambda: g.Put(1, "a", ""))

    def test_Grid_Put(self):
        g = Grid()
        self.assertTrue(g.Put(1, "A", "value"))
        self.assertFalse(g.Put(1, "A", "value"))

    def test_Grid_Get(self):
        g = Grid()
        self.assertIsNone(g.Get(1, "A"))
        self.assertTrue(g.Put(1, "A", "value"))
        self.assertEqual("value", g.Get(1, "A"))

if __name__ == "__main__":
    unittest.main()
