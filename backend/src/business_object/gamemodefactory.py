from business_object.game_mode.coin_flip_mode import CoinFlipMode
from business_object.game_mode.dice_mode import DiceMode
from business_object.game_mode.game_mode import GameMode


class GameModeFactory:
    @classmethod
    def get_mode(cls, game_mode: str) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """

        if game_mode.lower() == "coinflip":
            result = CoinFlipMode()

        if game_mode.lower() == "dice":
            result = DiceMode()

        else:
            raise ValueError("Vous devez choisir entre coinflip et dice")

        return result
