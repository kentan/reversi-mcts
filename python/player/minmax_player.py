
from state import State
from board import Board
from board import BoardUtil
import copy
import time

class MinMaxPlayer:
    def __init__(self,player_id):
        self.fist = (player_id == 0)
        self.previous = None

    def action(self, board_,opponent_action):
        state_before = State(copy.deepcopy(board_))
        tree = self.previous
        if tree is None:
            tree = MinMaxTree(state_before,0,None,self.fist)

        while tree.best_child is not None:
            tree = tree.best_child



        tree.dfs_evaluate()
        action = tree.best_action
        self.previous = tree.best_child


        return action


class MinMaxTree:
    SEARCH_DEPTH = 3
    def __init__(self,state_,depth,parent,first):
        self.children = {}
        self.best_child = None
        self.best_action = - 1
        self.v = 0
        self.alpha = -1
        self.beta = 100
        self.prone = False
        self.state = state_
        self.depth = depth
        self.parent = parent
        self.passed = False
        self.first = first




    def evaluate(self):
        self.v = self.value()

    def is_maxnode(self):
        return self.depth % 2 == 0


    def pick_best(self):
        try:
            if self.is_maxnode():
                k = max(self.children, key=self.children.get)
            else:
                k = min(self.children, key=self.children.get)
        except ValueError as e:
            self.pretty_print()

        return k, self.children[k]

    def update(self):
        self.v = self.best_child.v

    def dfs_evaluate(self,depth=SEARCH_DEPTH):
        if depth == 0 or self.depth == 60:
            self.evaluate()

        else:
            # max = 0
            self.expand()

            for action,child in self.children.items():
                child.dfs_evaluate(depth - 1)

            self.best_action,self.best_child = self.pick_best()
            self.update()
            # return self.best_child.v


    def expand(self):
        actions = self.state.board.puttable_tiles()
        if len(actions) == 0:
            s = State(copy.deepcopy(self.state.board))
            t = MinMaxTree(s,self.depth + 1,self,self.first)
            self.children[-1] = t
            self.passed = True
            if self.parent.passed:
                self.game_end = True


        # print(str(actions))
        max_value = 0
        for action in actions:
            s = State(copy.deepcopy(self.state.board))
            s.board.put(action)
            t = MinMaxTree(s,self.depth + 1,self,self.first)
            self.children[action] = t



    def value(self):
        player_id = 1 if self.first else -1
        return bin(self.state.board.boards[player_id]).count("1")

    # for max function
    def __lt__(self,other):
        return self.v < other.v

    def pretty_print(self):
        indent = '>' * self.depth
        min_max = "o" if self.is_maxnode() else "x"
        print(min_max + ":" + str(self.v) + ":")

        self.state.board.show_board(indent)


        for child in self.children.values():
            child.pretty_print()


if __name__ == "__main__":
    b = Board()
    s = State(b)
    t = MinMaxTree(s,0,None,True)

    start = time.time()
    t.dfs_evaluate(MinMaxTree.SEARCH_DEPTH)
    # t.pretty_print()

    end = time.time()

    print(end - start)