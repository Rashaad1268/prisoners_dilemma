import abc
import typing
from game.enums import Action


class Strategy(abc.ABC):
    def __init__(self):
        self.history: typing.List[Action] = []

    @abc.abstractmethod
    def get_output(self, *, opponent: "Strategy", round_number: int):
        pass

    @property
    def last_move(self) -> typing.Optional[Action]:
        return self.history[-1] if len(self.history) > 0 else None

    def __str__(self):
        return self.__class__.__name__
