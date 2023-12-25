import random
import typing as t

from game.enums import Action
from game.player import Player


class GameManager:
    def __init__(self, player_1: Player, player_2: Player, noise_percentage: t.Optional[float] = None):
        self.player_1 = player_1
        self.player_2 = player_2

        self.noise_percentage = noise_percentage

    def apply_noise(self, output):
        if self.noise_percentage:
            if output == Action.cooperate:
                if random.random() < self.noise_percentage:
                    return Action.defect

        return output

    def __run_round(self, round_number: int):
        player_1_output = self.apply_noise(
            self.player_1.strategy.get_output(opponent=self.player_2.strategy, round_number=round_number))
        player_2_output = self.apply_noise(
            self.player_2.strategy.get_output(opponent=self.player_1.strategy, round_number=round_number))

        if player_1_output == Action.cooperate:
            if player_2_output == Action.cooperate:
                self.player_1.points += 3
                self.player_2.points += 3

            elif player_2_output == Action.defect:
                self.player_2.points += 5

        elif player_1_output == Action.defect:
            if player_2_output == Action.defect:
                self.player_1.points += 1
                self.player_2.points += 1

            elif player_2_output == Action.cooperate:
                self.player_1.points += 5

        self.player_1.strategy.history.append(player_1_output)
        self.player_2.strategy.history.append(player_2_output)

    def run_rounds(self, total_rounds):
        for round_number in range(total_rounds):
            self.__run_round(round_number)

        self.player_1.reset()
        self.player_2.reset()
