from battleship import Game
from player import RandomPlayer
g = Game(RandomPlayer("one"), RandomPlayer("two"))
g.Play()