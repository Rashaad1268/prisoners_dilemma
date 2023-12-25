import random

from game.game_manager import GameManager
from game.player import Player
from game import strategies

max_rounds_per_game = 500

all_players = [
    Player(strategies.TitForTatStrategy),
    Player(strategies.FriedmanStrategy),
    Player(strategies.RandomStrategy),
    Player(strategies.JossStrategy),
    Player(strategies.TesterStrategy),
    Player(strategies.TitForTwoTatsStrategy),
    Player(strategies.AlwaysDefectStrategy),
]

for _ in range(5):
    for player_1 in all_players:
        for player_2 in all_players:
            GameManager(player_1, player_2).run_rounds(max_rounds_per_game)

for place, player in enumerate(sorted(all_players, key=lambda p: p.points, reverse=True), start=1):
    print(
        f"{place}: {player.strategy} (avg points: {player.points / (len(all_players)*5)} in {max_rounds_per_game} rounds)")
