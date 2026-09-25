import secrets
from datetime import datetime

from businees_object.player import Player

from business_object.game import Game
from business_object.gamemode import GameMode


class CoinFlipMode(GameMode):
    def play(self, p1: Player, p2: Player, choice: str = "heads") -> Game:
        choice = choice.lower()
        if choice not in ["heads", "tails"]:
            raise ValueError(
                f"Invalid choice for CoinFlipMode: '{choice}'. Must be 'heads' or 'tails'."
            )
        result = secrets.choice(["heads", "tails"])
        winner = p1 if result == choice else p2

        description = f"coinflip game between {p1} and {p2}. Winner = {winner}"
        timestamp = datetime.now()

        return Game(p1, p2, "coinflip", winner, description, timestamp)
