import unittest
import mcts
import pickle
import treenode
import board
import state

class TestMCTS(unittest.TestCase):
    #@unittest.skip("")
    def test_start(self):

        s = state.State(board.Board())
        n = treenode.Node(s)
        m = mcts.MCTS(n)
        m.start(n,True)


if __name__ == '__main__':
    unittest.main()

