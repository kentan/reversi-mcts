import unittest
import board
import test.testdata
import simulator

class TestSimulator(unittest.TestCase):
    def test_simulator(self):
        data = test.testdata.gen_test_data()

        for d in data:
            b = board.Board(d.mine, d.yours)
            sim = simulator.Simulator(b)
            sim.board.show_board()
            sim.playout()
            sim.board.show_board()