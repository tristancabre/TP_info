class Game:
    def __init__(self, player1, player2, gamemode, winner, description, timestamp, id_game=None):

        self.id_game = id_game
        self.player1 = player1
        self.player2 = player2
        self.gamemode = gamemode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        return f"{self.gamemode} between {self.player1} and {self.player2}. Winner = {self.winner}"
