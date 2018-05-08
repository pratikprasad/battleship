from battleship import Game
from player import RandomPlayer
from alphabetical_player import AlphabeticalPlayer
g = Game(RandomPlayer("one"), AlphabeticalPlayer())
winner = g.Play(0)
print "The winner was: " + winner.PlayerName()