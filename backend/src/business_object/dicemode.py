import secrets
from datetime import datetime

from businees_object.player import Player

from business_object.game import Game
from business_object.gamemode import GameMode


class DiceMode(GameMode):
    def play(self, p1: Player, p2: Player) -> Game:

        d1 = secrets.choice(range(1, 7))
        d2 = secrets.choice(range(1, 7))

        if d1 < d2:
            winner = p2
        elif d2 < d1:
            winner = p1

        description = f"dice game between {p1} and {p2}. Winner = {winner}"
        timestamp = datetime.now()

        return Game(p1, p2, "coinflip", winner, description, timestamp)
