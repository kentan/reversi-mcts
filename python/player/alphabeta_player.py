
from state import State
from board import Board,BoardUtil
from player import minmax_player
import copy
import time

class AlphaBetaTree(minmax_player.MinMaxTree):
    SEARCH_DEAPTH = 4

    def __init__(self, state_, depth, parent,alpha,beta):
        super().__init__(state_,depth,parent)
        self.alpha = alpha
        self.beta = beta
        self.passed = False
        self.game_end = False


    def should_prone(self):
        if self.parent.is_maxnode():
            # print("MAX:" + str(self.v)+ ":" + str(self.v) + ":" + str(self.alpha))
            if self.v < self.alpha:
                return True
        else:
            # print("MIN:" + str(self.depth) + ":" + str(self.v) + ":" + str(self.beta))
            if self.v > self.beta:
                return True
        return False

    def evaluate(self):
        self.v = self.value()
        # self.prone = self.should_prone()


    def update(self):
        self.v = self.best_child.v
        if self.parent is None:
            return
        if self.is_maxnode():
            # print("in alpha")
            self.alpha = self.v
            self.parent.alpha = self.v
        else:
            # print("in beta")
            self.beta = self.v
            self.parent.beta = self.v

    def dfs_evaluate(self,depth):
        # print("DEPTH:" + str(depth))
        if depth == 0:
            self.evaluate()
        else:
            self.expand()

            if self.game_end:
                return

            for action,child in self.children.items():
                child.alpha = self.alpha
                child.beta = self.beta
                child.dfs_evaluate(depth - 1)
                if child.should_prone() :break

            self.best_action,self.best_child = self.pick_best()
            self.update()


    def expand(self):
        actions = self.state.board.puttable_tiles()
        if len(actions) == 0:
            s = State(copy.deepcopy(self.state.board))
            t = AlphaBetaTree(s,self.depth + 1,self,self.alpha,self.beta)
            self.children[-1] = t
            self.passed = True
            if self.parent.passed:
                self.game_end = True
            if self.state.board.get_num_of_yourtile() == 0:
                self.game_end = True

        # print(str(actions))
        max_value = 0
        for action in actions:
            s = State(copy.deepcopy(self.state.board))
            s.board.put(action)
            t = AlphaBetaTree(s,self.depth + 1,self,self.alpha,self.beta)
            self.children[action] = t



    def value(self):
        v1 =  bin(self.state.board.boards[1]).count("1")
        if self.passed and self.parent.passed:
            v2 = bin(self.state.board.boards[-1]).count("1")
            if v1 > v2 : v1 += 1000
            if v1 < v2 : v1 -= 1000
        return v1


    def __lt__(self,other):
        return self.v < other.v

    def pretty_print(self):
        indent = '>' * self.depth
        min_max = "o" if self.is_maxnode() else "x"
        # print(min_max + ":" + str(self.v) + ":")

        self.state.board.show_board(indent)


        for child in self.children.values():
            child.pretty_print()



b = Board()
s = State(b)
t = AlphaBetaTree(s, 0, None,-1,100)

start = time.time()
t.dfs_evaluate(AlphaBetaTree.SEARCH_DEAPTH)
# t.pretty_print()

end = time.time()
print(end - start)



