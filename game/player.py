import typing
from game.strategy import Strategy


class Player:
    def __init__(self, strategy_cls: typing.Type[Strategy]):
        self.strategy_cls = strategy_cls
        self.strategy = strategy_cls()

        self.points = 0

    def reset(self):
        # This is to reset the strategies history after every game
        self.strategy = self.strategy_cls()

    def __repr__(self):
        return f"<Player strategy={self.strategy.__class__.__name__} points={self.points}>"
