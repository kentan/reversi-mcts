import unittest
import board
import mcts
import test.testdata


class TestMain(unittest.TestCase):

    def test_is_puttable(self):
        data = test.testdata.gen_test_data()
        for d in data:
            puttable_poses = d.mine_puttables
            for pos in puttable_poses:
                b = board.Board(d.mine, d.yours)
                result = b.is_puttable(pos)
                self.assertTrue(result,"test id is " + str(d.id) + " mine,pos is " + str(pos))

            puttable_poses = d.yours_puttables
            for pos in puttable_poses:
                b = board.Board(d.yours, d.mine)
                result = b.is_puttable(pos)
                self.assertTrue(result,"test id is " + str(d.id) + " yours,pos is " + str(pos))


    def test_put1(self):

        """
        x x x o
        - x x x
        - o x -
        - - - -

        next: o 4
        """
        p1 = 0b1000001000000
        p2 = 0b1110011100100000

        pos = 4

        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        b.put(pos)
        b.show_board()


    def test_put2(self):
        """
        o - - -
        o o x -
        o x x x
        - - x o

        next: o 2
        """
        p1 = 0b1000110010000001
        p2 = 0b1001110010

        pos = 2

        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        b.put(pos)

        """
        id 0
        x x x o
        - x x x
        - o x -
        - - - -

        available = o4, x2, x7
        current_player = o
        """
        p1 = 0b1000001000000
        p2 = 0b1110011100100000

        pos = 4
        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        b.put(pos)

        b.show_board()


    # def test_mtcs(self):
    #     m = mcts.MCTS()
    #     m.start()

    def test_winning_player(self):
        """
        o - - -
        o o x -
        o x x x
        - - x o

        next: o 2
        """
        p1 = 0b1000110010000001
        p2 = 0b1001110010

        pos = 2

        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        self.assertEqual(b.get_wining_player(),"draw")

        b.put(pos)

        self.assertEqual(b.get_wining_player(),"player1")

    def test_is_end(self):
        """
        ide 01111300
        x x x o
        x x x o
        x o o o
        x o o o
        available = o0
        current_player = x
        """
        ide = "01111300"
        p1 = 0b1000101110111
        p2 = 0b1110111010001000
        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        self.assertTrue(b.is_end())


        """
            ide 0111300
            x x x o
            o x x o
            - o x o
            x o x x
            available = none
            current_player = o
        """
        ide = "0111300"
        p1 = 0b1100101010100
        p2 = 0b1110011000101011
        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        self.assertTrue(b.is_end())

        """
        o - - -
        o o x -
        o x x x
        - - x o

        next: o 2
        """
        p1 = 0b1000110010000001
        p2 = 0b1001110010

        pos = 2

        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len
        b = board.Board(p1,p2)
        self.assertFalse(b.is_end())

if __name__ == '__main__':
    unittest.main()

