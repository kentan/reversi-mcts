import math
import random
import copy
import simulator

class Node:
    total_visits = 0
    def __init__(self,state,parent=None):
        self.children = {}
        self.visits = 0
        self.value = 0
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1


    def is_fully_expanded(self):
        return len(self.children) == len(self.available_actions())

    def available_actions(self):
        return self.state.board.puttable_tiles()

    def select(self):
        if self.children is None :
            print("children null")
            return None
        return max(self.children.values(), key=lambda x: x.ucb1())


    def expand(self,action=None):
        actions = self.available_actions()#
        #print("actions:" + str(actions))
        if len(actions) == 0:
            print("No action!")
            return None
        if action is None:
            while True:
                action = random.sample(actions,1)[0]
                if action not in self.children.keys():
                    break
        elif action not in actions:
            print(str(action) + " is not in available actions")
            return None


        #print("picked action: " + str(action))
        state = copy.deepcopy(self.state)
        child = Node(state,self)
        child.state.board.put(action)
        self.children[action] = child
        return child


    def simulate(self):
        sim = simulator.Simulator(self.state.board)
        return sim.playout()

    def back_propagate(self,point):
        self.value += point
        self.visits += 1
        Node.total_visits += 1
        if not self.parent is None:
            self.parent.back_propagate(point)

    def ucb1(self):
        return self.value + math.sqrt(2 * math.log(Node.total_visits,math.e) / self.visits)

    def is_end(self):
        return self.state.board.is_end()


    def show(self,rec=True):
        indent = ' ' * self.depth
        print(indent + "depth:" + str(self.depth))
        print(indent + "value:" + str(self.value))
        print(indent + "visits:" + str(self.visits))
        self.state.board.show_board()

        if rec:
            for c in self.children.values():
                c.show()

    def find(self,node_):
        if self.state == node_.state:
            print("equal")
            return self

        for c in self.children.values():
            n = c.find(node_)
            if n is not None:
                return n

        return None


