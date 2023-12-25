import random
from game.enums import Action
from game.strategy import Strategy


class AlwaysDefectStrategy(Strategy):
    """Always defects"""

    def get_output(self, *, opponent, round_number):
        return Action.defect


class AlwaysCooperateStrategy(Strategy):
    """
    Always co-operates
    but do not include this in the simulation since the AlwaysDefectStrategy will take advantage of this
    """

    def get_output(self, *, opponent, round_number):
        return Action.cooperate


class TitForTatStrategy(Strategy):
    """
    Cooperates by default
    but if the opponent defects, this strategy defects in the next round as a response
    and if the opponent defects once and continues to cooperate, this strategy will also cooperate
    """
    def get_output(self, *, opponent, round_number):
        return opponent.last_move if opponent.last_move else Action.cooperate


class FriedmanStrategy(Strategy):
    """
    Cooperate by default
    but if the opponent defects once, this strategy will continue to defect for the rest of the game
    """
    def get_output(self, *, opponent, round_number):
        if Action.defect in opponent.history:
            return Action.defect

        else:
            return Action.cooperate


class RandomStrategy(Strategy):
    """Randomly cooperates or defects with a 50/50 chance"""
    def get_output(self, *, opponent, round_number):
        return random.choice([Action.cooperate, Action.defect])


class JossStrategy(Strategy):
    """
    This strategy cooperates at first
    but if the opponent defects, this strategy will also defect as a result
    there is also a 10% chance that this strategy will randomly defect in a round
    """
    def get_output(self, *, opponent, round_number):
        if opponent.last_move is None:
            return Action.cooperate

        elif opponent.last_move == Action.defect or (random.random() < 0.1):
            return Action.defect

        else:
            return Action.cooperate


class TesterStrategy(Strategy):
    """
    In the first round this strategy will defect, and then it'll cooperate in the 2nd round, and it'll also check the
    opponents response if the opponent defects in the 2nd round as a response for the first round this strategy will
    apologize and cooperate in the next round (3rd round) and it'll continue to play tit for tat for the rest of the
    game.

    But if the opponent cooperates in the 2nd round, this strategy will defect every other round
    """

    def get_output(self, *, opponent, round_number):
        if opponent.last_move is None:  # Return defect on the first round
            return Action.defect

        if round_number == 1:  # Cooperate on the 2nd round
            return Action.cooperate

        if opponent.history[1] == Action.cooperate:  # Check the opponents response on the 2nd round
            if round_number % 2 == 1:
                return Action.defect

        else:  # Just do the tit for tat strategy
            return opponent.last_move


class TitForTwoTatsStrategy(Strategy):
    """
    Cooperates by default
    but if the opponent defects 2 times in a row, this strategy will also defect as a response
    """

    def get_output(self, *, opponent, round_number):
        if opponent.history[-2:] == [Action.defect, Action.defect]:
            return Action.defect

        else:
            return Action.cooperate
