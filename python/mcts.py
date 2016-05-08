import math
import random
import board
import copy
import treenode
import pickle
import state

class MCTS:
    budget = 20
    def __init__(self,root_node):
        self.root_node = root_node
        self.current_node = None
        self.history = []

    def find(self,target_node):
        return self.root_node.find(target_node)

    def serialize(self,root):
        root.total_visits_for_pickling = treenode.Node.total_visits
        with open('data.pickle', 'wb') as f:
           pickle.dump(root, f, pickle.HIGHEST_PROTOCOL)

    def start(self,target_node,serialization=False):
        if target_node is None:
            s = state.State(board.Board())
            target_node = treenode.Node(s, None)

        base_node = self.find(target_node)

        for i in range(MCTS.budget):
            node = base_node
            if i % 1000 == 0 :
                print("searching in " + str(i) + " iteration")
            while not node.is_end():
                if node.is_fully_expanded():
                    node = node.select()
                    if(node is None) :
                        print("NONE")
                else:
                    node = node.expand()
                    break

            p = node.simulate()
            node.back_propagate(p)

        if serialization:
            self.serialize(base_node)




