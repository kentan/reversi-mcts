import random
import copy
from player import random_player


class Simulator:
    points = {"player1":1,"draw":0,"player2":-1}
    def __init__(self,board):
        self.board = copy.deepcopy(board)
        self.sim1 = random_player.RandomPlayer()
        self.sim2 = random_player.RandomPlayer()#player.MinMaxPlayer()
        self.players = {board.player1:self.sim1,board.player2:self.sim2}

    def playout(self):
        #print("START PLAYOUT")
        while not self.board.is_end():
            action = self.players[self.board.current_player].action(self.board,None)
            #action = random.sample(self.board.puttable_tiles(),1)[0]
            #print(":" + str(action))
            self.board.put(action)
            self.board.check()
            #self.board.show_board()

        p = self.board.get_wining_player()
        #print("WIN:"+p)
        return Simulator.points[p]

