import random

class RandomPlayer:
    def action(self,board,opponent_action):
        return random.sample(board.puttable_tiles(),1)[0]


