import unittest
import board
import mcts
import state
import treenode
import test.testdata

# class TestData:
#     def __init__(self,p1,p2,expected):
#         self.mine = p1
#         self.yours = p2
#         self.expected = expected
#
#     def node(self):
#         b = board.Board(self.mine,self.yours)
#         s = state.State(b)
#         node = treenode.Node(s,None)
#         return node
#
# def gen_testData():
#
#     data = []
#     """
#     case 1
#     x x x o
#     - x x x
#     - o x -
#     - - - -
#
#     available = o4, x2, x7
#     """
#     p1 = 0b1000001000000
#     p2 = 0b1110011100100000
#     expected = [4] # available pos for p1
#     data.append(TestData(p1,p2,expected))
#
#     """
#     case 2
#     x - x o
#     - x x x
#     - o x -
#     - - - -
#
#     available = o4, o14
#     """
#     p1 = 0b1000001000000
#     p2 = 0b1010011100100000
#     expected = [4,14] # available pos for p1
#     data.append(TestData(p1,p2,expected))
#
#     """
#     case 3
#     x o x o
#     - x o x
#     - x x -
#     - - x o
#
#     available = o2, o3, o4,o11
#     """
#     p1 = 0b101001000000001
#     p2 = 0b1010010101100010
#     expected = [2,3,4,11] # available pos for p1
#     data.append(TestData(p1,p2,expected))
#
#     """
#     case 4
#     - x x o
#     - - - -
#     - - - -
#     o x x -
#
#     available = o2, o3, o4,o11
#     """
#     p1 = 0b1000000001000
#     p2 = 0b110000000000110
#     expected = [0,15] # available pos for p1
#     data.append(TestData(p1,p2,expected))
#
#     """
#     case 5
#     - - - o
#     x - - x
#     x - - x
#     o - - -
#
#     available = o2, o3, o4,o11
#     """
#     p1 = 0b1000000001000
#     p2 = 0b100110010000
#     expected = [0,15] # available pos for p1
#     data.append(TestData(p1,p2,expected))
#
#     return data

# class TestState:
#     def __init__(self,ide,p1,p2,actions,current,next_status):
#         self.ide = ide
#         self.player1_board = p1
#         self.player2_board = p2
#         self.current_player = current
#         self.actions = actions
#         self.next_status = next_status


# def gen_data2():
#     dataset = {}
#     """
#         id 0
#         x x x o
#         - x x x
#         - o x -
#         - - - -
#
#         available = o4, x2, x7
#         current_player = o
#     """
#     ide = "0"
#     p1 = 0b1000001000000
#     p2 = 0b1110011100100000
#
#     actions = [4]
#     next_status = ["00"]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         id 00
#         x x x o
#         - x x o
#         - o o o
#         - - - -
#         available = o11, x0,x1, x2, x3
#         current_player = x
#     """
#     ide = "00"
#     p1 = 0b1000101110000
#     p2 = 0b1110011000000000
#     actions = [0,1,2,3]
#     next_status = ["000","100","200","300"]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 000
#         x x x o
#         - x x o
#         - o x o
#         - - - x
#         available = o11,o2,x2,x3
#         current_player = o
#     """
#     ide = "000"
#     p1 = 0b1000101010000
#     p2 = 0b1110011000100001
#     actions = [11,2]
#     next_status = ["0000","1000"]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 100
#         x x x o
#         - x x o
#         - o x o
#         - - x -
#         available = o11,o2,,x2,x3
#         current_player = o
#     """
#     ide = "100"
#     p1 = 0b1000101010000
#     p2 = 0b1110011000100010
#     actions = [2,11]
#     next_status = ["0100","1100"]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         id 200
#         x x x o
#         - x x o
#         - x o o
#         - x - -
#         available = o3,o7,o11,x0,x1
#         current_player = o
#     """
#     ide = "200"
#     p1 = 0b1000100110000
#     p2 = 0b1110011001000100
#     actions = [3,7,11]
#     next_status = ["0200","1200","2200"]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 300
#         x x x o
#         - x x o
#         - x o o
#         x - - -
#         available = o7,o11,x0
#         current_player = o
#     """
#
#     ide = "300"
#     p1 = 0b1000100110000
#     p2 = 0b1110011001001000
#     actions = [7,11]
#     next_status = ["0300","1300"]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0000
#         x x x o
#         o o o o
#         - o x o
#         - - - x
#         available = o1,x2,x7
#         current_player = x
#     """
#     ide = "0000"
#     p1 = 0b1111101010000
#     p2 = 0b1110000000100001
#     actions = [2,7]
#     next_status = ["00000","10000"]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         id 1000
#         x x x o
#         - x x o
#         - o o o
#         - o - x
#         available = x1,x3
#         current_player = x
#     """
#     ide = "1000"
#     p1 = 0b1000101110100
#     p2 = 0b1110011000000001
#     actions = [1,3]
#     next_status = [None] #TODO Implement it
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 0100
#         x x x o
#         o o o o
#         - o x o
#         - - x -
#         available = o0,x2,x7
#         current_player = x
#     """
#     ide = "0100"
#     p1 = 0b1111101010000
#     p2 = 0b1110000000100010
#     actions = [2,7]
#     next_status = ["0" + ide, "1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 1100
#         x x x o
#         - x x o
#         - o o o
#         - o x -
#         available =
#         current_player = x
#     """
#     ide = "1100"
#     p1 = 0b1000101110100
#     p2 = 0b1110011000000010
#     actions = [None]#TODO found that it failed to be defined. Implement it.
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#
#     """
#         id 0200
#         x x x o
#         - x o o
#         - o o o
#         o x - -
#         available = o1,o11,x0,x1
#         current_player = x
#     """
#     ide = "0200"
#     p1 = 0b1001101111000
#     p2 = 0b1110010000000100
#     actions = [0,1]
#     next_status = ["0" + ide, "1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         id 1200
#         x x x o
#         - x x o
#         o o o o
#         - x - -
#         available = o11,x0,x1,x3,
#         current_player = x
#     """
#     ide = "1200"
#     p1 = 0b1000111110000
#     p2 = 0b1110011000000100
#     actions = [0,1,3]
#     next_status = ["0" + ide, "1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         id 2200
#         x x x o
#         o o o o
#         - x o o
#         - x - -
#         available = o3,o7,x0,x1,x7
#         current_player = x
#     """
#     ide = "2200"
#     p1 = 0b1111100110000
#     p2 = 0b1110000001000100
#     actions = [0,1,7]
#     next_status = ["0" + ide, "1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 0300
#         x x x o
#         - x x o
#         o o o o
#         x - - -
#         available = o11,x0,x1,x2,x11
#         current_player = x
#     """
#     ide = "0300"
#     p1 = 0b1000111110000
#     p2 = 0b1110011000001000
#     actions = [0,1,2,11]
#     next_status = ["0" + ide, "1" + ide,"2" + ide,"3" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 1300
#         x x x o
#         o o o o
#         - x o o
#         x - - -
#         available = o1,o2,o7,x0,x1,x7
#         current_player = x
#     """
#     ide = "1300"
#     p1 = 0b1111100110000
#     p2 = 0b1110000001001000
#     actions = [0,1,7]
#     next_status = ["0" + ide, "1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 00000
#         x x x o
#         o x o o
#         - x x o
#         - x - x
#         available = o1,o3,o7
#         current_player = o
#     """
#     ide = "00000"
#     p1 = 0b1101100010000
#     p2 = 0b1110010001100101
#     actions = [1,3,7]
#     next_status = ["0" + ide, "1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 10000
#         x x x o
#         x x o o
#         x x x o
#         - - - x
#         available = o1,o2,o3
#         current_player = o
#     """
#     ide = "10000"
#     p1 = 0b1001100010000
#     p2 = 0b1110110011100001
#     actions = [1,3,2]
#     next_status = ["0" + ide, "1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 00100
#         x x x o
#         o x o o
#         - x x o
#         - x x -
#         available = o3,o7,x11
#         current_player = o
#     """
#     ide = "00100"
#     p1 = 0b1101100010000
#     p2 = 0b1110010001100110
#     actions = [3,7]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 10100
#         x x x o
#         x x o o
#         x x x o
#         - - x -
#         available = o3
#         current_player = o
#     """
#     ide = "10100"
#     p1 = 0b1001100010000
#     p2 = 0b1110110011100010
#     actions = [3,2]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 00200
#         x x x o
#         - x o o
#         - o x o
#         o x - x
#         available = o1,o11,x7
#         current_player = o
#     """
#     ide = "00200"
#     p1 = 0b1001101011000
#     p2 = 0b1110010000100101
#     actions = [1,11]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 10200
#         x x x o
#         - x x o
#         - o x o
#         o x x -
#         available = o0,o11,x7
#         current_player = o
#     """
#     ide = "10200"
#     p1 = 0b1000101011000
#     p2 = 0b1110011000100110
#     actions = [11,0]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 01200
#         x x x o
#         - x x o
#         o o x o
#         - x - x
#         available = o11,x3
#         current_player = o
#     """
#     ide = "01200"
#     p1 = 0b1000111010000
#     p2 = 0b1110011000100101
#     actions = [11]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 11200
#         x x x o
#         - x x o
#         o o x o
#         - x x -
#         available = o11,x3
#         current_player = o
#     """
#     ide = "11200"
#     p1 = 0b1000111010000
#     p2 = 0b1110011000100110
#     actions = [11]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 21200
#         x x x o
#         - x x o
#         o x o o
#         x x - -
#         available = o11,x1,x2,
#         current_player = o
#     """
#     ide = "21200"
#     p1 = 0b1000110110000
#     p2 = 0b1110011001001100
#     actions = [11]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 02200
#         x x x o
#         o x o o
#         - x x o
#         - x - x
#         available = o1,o3,o7,x7
#         current_player = o
#     """
#     ide = "02200"
#     p1 = 0b1101100010000
#     p2 = 0b1110010001100101
#     actions = [1,3,7]
#     next_status = ["0" + ide,"1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 12200
#         x x x o
#         o o x o
#         - x x o
#         - x x -
#         available = o0,o3,o7,x7
#         current_player = o
#     """
#     ide = "12200"
#     p1 = 0b1110100010000
#     p2 = 0b1110001001100110
#     actions = [0,3,7]
#     next_status = ["0" + ide,"1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 22200
#         x x x o
#         x x o o
#         x x o o
#         - x - -
#         available = o3,x0,x2
#         current_player = o
#     """
#     ide = "22200"
#     p1 = 0b1001100110000
#     p2 = 0b1110110011000100
#     actions = [3]
#     next_status = ["0"+ ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 00300
#         x x x o
#         - x x o
#         o o x o
#         x - - x
#         available = o11,o2,,x2,x11
#         current_player = o
#     """
#     ide = "00300"
#     p1 = 0b1000111010000
#     p2 = 0b1110011000101001
#     actions = [11,2]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 10300
#         x x x o
#         - x x o
#         o o x o
#         x - x -
#         available = o11,o2,x1,x11
#         current_player = o
#     """
#     ide = "10300"
#     p1 = 0b1000111010000
#     p2 = 0b1110011000101010
#     actions = [11,2]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 20300
#         x x x o
#         - x x o
#         o x o o
#         x x - -
#         available = o11,x0,x1,x11
#         current_player = o
#     """
#     ide = "20300"
#     p1 = 0b1000110110000
#     p2 = 0b1110011001001100
#     actions = [11]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 30300
#         x x x o
#         x x x o
#         x o o o
#         x - - -
#         available = none
#         current_player = o
#     """
#     ide = "30300"
#     p1 = 0b1000101110000
#     p2 = 0b1110111010001000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 30300
#         x x x o
#         x x x o
#         x o o o
#         x - - -
#         available = x0,x1,x2
#         current_player = o
#     """
#     ide = "30300"
#     p1 = 0b1000101110000
#     p2 = 0b1110111010001000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 01300
#         x x x o
#         o x o o
#         - x x o
#         x - - x
#         available = o1,o7,o2,x7
#         current_player = o
#     """
#     ide = "01300"
#     p1 = 0b1101100010000
#     p2 = 0b1110010001101001
#     actions = [1,7,2]
#     next_status = ["0" + ide,"1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 11300
#         x x x o
#         o o x o
#         - x x o
#         x - x -
#         available = o0,o2,o7,x0,x7
#         current_player = o
#     """
#     ide = "11300"
#     p1 = 0b1110100010000
#     p2 = 0b1110001001101010
#     actions = [0,2,7]
#     next_status = ["0" + ide,"1" + ide,"2" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 21300
#         x x x o
#         x x o o
#         x x o o
#         x - - -
#         available = none
#         current_player = o
#     """
#     ide = "21300"
#     p1 = 0b1001100110000
#     p2 = 0b1110110011001000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 000000
#         x x x o
#         o x o o
#         - o o o
#         - x o x
#         available = o3,x7
#         current_player = x
#     """
#     ide = "000000"
#     p1 = 0b1101101110010
#     p2 = 0b1110010000000101
#     actions = [7]
#     next_status = ["0"+ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 100000
#         x x x o
#         o x o o
#         - o x o
#         o x - x
#         available = o1,x7
#         current_player = x
#     """
#     ide = "100000"
#     p1 = 0b1101101011000
#     p2 = 0b1110010000100101
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 200000
#         x x x o
#         o x o o
#         o o o o
#         - x - x
#         available = x1,x3
#         current_player = x
#     """
#     ide = "200000"
#     p1 = 0b1101111110000
#     p2 = 0b1110010000000101
#     actions = [1,3]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 010000
#         x x x o
#         x x o o
#         x x o o
#         - - o x
#         available = none
#         current_player = x
#     """
#     ide = "010000"
#     p1 = 0b1001100110010
#     p2 = 0b1110110011000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 110000
#         x x x o
#         x x o o
#         x o x o
#         o - - x
#         available = o1,o2,x1,x2
#         current_player = x
#     """
#     ide = "110000"
#     p1 = 0b1001101011000
#     p2 = 0b1110110010100001
#     actions = [1,2]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """#TODO Implement it
#         ide 210000
#         x x x o
#         x x o o
#         x x o o
#         - o - x
#         available =
#         current_player = x
#     """
#     ide = "210000"
#     p1 = 0b1001100110100
#     p2 = 0b1110110011000001
#     actions = [1]
#     next_status = [None] #TODO implement it
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     # """
#     #     ide 010000
#     #     x x x o
#     #     x x o o
#     #     x x o o
#     #     - - o x
#     #     available = o3,x2
#     #     current_player = x
#     # """
#     # ide = "010000"
#     # p1 = 0b1001100110010
#     # p2 = 0b1110110011000001
#     # actions = [2]
#     # next_status = ["0" + ide]
#     # data = TestState(ide,p1,p2,actions,-1,next_status)
#     #
#     # """
#     #     ide 110000
#     #     x x x o
#     #     x x o o
#     #     x o x o
#     #     o - - x
#     #     available = o1,x1,x2
#     #     current_player = x
#     # """
#     # ide = "110000"
#     # p1 = 0b1001101011000
#     # p2 = 0b1110110010100001
#     # actions = [1,2]
#     # next_status = ["0" + ide,"1" + ide]
#     # data = TestState(ide,p1,p2,actions,-1,next_status)
#
#     """
#         ide 000100
#         x x x o
#         o x o o
#         - o x o
#         o x x -
#         available = o0,x7
#         current_player = x
#     """
#     ide = "000100"
#     p1 = 0b1101101011000
#     p2 = 0b1110010000100110
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#
#
#
#     """
#         ide 100100
#         x x x o
#         o x o o
#         o o o o
#         - x x -
#         available = x0,x3
#         current_player = x
#     """
#     ide = "100100"
#     p1 = 0b1101111110000
#     p2 = 0b1110010000000110
#     actions = [0,3]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 010100
#         x x x o
#         x x o o
#         x o x o
#         o - x -
#
#         available = o2,x2
#         current_player = x
#     """
#     ide = "010100"
#     p1 = 0b1001101011000
#     p2 = 0b1110110010100010
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 110100
#         x x x o
#         x x o o
#         x x o o
#         - o x -
#         available = x0,x3
#         current_player = x
#     """
#     ide = "110100"
#     p1 = 0b1001100110100
#     p2 = 0b1110110011000010
#     actions = [0,3]
#     next_status = [None] #TODO implement it
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 000200
#         x x x o
#         - x o o
#         - o o o
#         o o o x
#         available = o11
#         current_player = x
#     """
#     ide = "000200"
#     p1 = 0b1001101111110
#     p2 = 0b1110010000000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 100200
#         x x x o
#         o o o o
#         - o x o
#         o x - x
#         available = o1,x7
#         current_player = x
#     """
#     ide = "100200"
#     p1 = 0b1111101011000
#     p2 = 0b1110000000100101
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 010200
#         x x x o
#         o o o o
#         - o x o
#         o x x -
#         available = o0,x7
#         current_player = x
#     """
#     ide = "010200"
#     p1 = 0b1111101011000
#     p2 = 0b1110000000100110
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 110200
#         x x x o
#         - x x o
#         - o x o
#         o o o o
#         available = x7
#         current_player = x
#     """
#     ide = "110200"
#     p1 = 0b1000101011111
#     p2 = 0b1110011000100000
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 001200
#         x x x o
#         o o o o
#         o o x o
#         - x - x
#         available = o1,x3
#         current_player = x
#     """
#     ide = "001200"
#     p1 = 0b1111111010000
#     p2 = 0b1110000000100101
#     actions = [3]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 011200
#         x x x o
#         o o o o
#         o o x o
#         - x x -
#         available = o0,x3
#         current_player = x
#     """
#     ide = "011200"
#     p1 = 0b1111111010000
#     p2 = 0b1110000000100110
#     actions = [3]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 021200
#         x x x o
#         o o o o
#         o x o o
#         x x - -
#         available = o1,x0,x1,
#         current_player = x
#     """
#     ide = "021200"
#     p1 = 0b1111110110000
#     p2 = 0b1110000001001100
#     actions = [0,1]
#     next_status = ["0" + ide,"1"+ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 002200
#         x x x o
#         o x o o
#         - o o o
#         - x o x
#         available = o3,x7
#         current_player = x
#     """
#     ide = "002200"
#     p1 = 0b1101101110010
#     p2 = 0b1110010000000101
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 102200
#         x x x o
#         o x o o
#         - o x o
#         o x - x
#         available = o1,x7
#         current_player = x
#     """
#     ide = "102200"
#     p1 = 0b1101101011000
#     p2 = 0b1110010000100101
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """TODO implement the later
#         ide 202200
#         x x x o
#         o x o o
#         o o o o
#         - x - x
#         available = x1,x3
#         current_player = x
#     """
#     ide = "202200"
#     p1 = 0b1010011110000
#     p2 = 0b1110010000000101
#     actions = [1,3]
#     next_status = [None] #TODO
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 202200
#         x x x o
#         o x o o
#         o o o o
#         - x - x
#         available = x1,x3
#         current_player = x
#     """
#     ide = "202200"
#     p1 = 0b1101111110000
#     p2 = 0b1110010000000101
#     actions = [1,3]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 012200
#         x x x o
#         o o x o
#         - x o o
#         - x x o
#         available = o3,o7,x7
#         current_player = x
#     """
#     ide = "012200"
#     p1 = 0b1110100110001
#     p2 = 0b1110001001000110
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 112200
#         x x x o
#         o o o o
#         - o x o
#         o x x -
#         available = o0,x7
#         current_player = x
#     """
#     ide = "112200"
#     p1 = 0b1111101011000
#     p2 = 0b1110000000100110
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 212200
#         x x x o
#         o o x o
#         o o o o
#         - x x -
#         available = x0,x3
#         current_player = x
#     """
#     ide = "212200"
#     p1 = 0b1110111110000
#     p2 = 0b1110001000000110
#     actions = [0,3]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 022200
#         x x x o
#         x x o o
#         x o o o
#         o x - -
#         available = o1,x0,x1
#         current_player = x
#     """
#     ide = "022200"
#     p1 = 0b1001101111000
#     p2 = 0b1110110010000100
#     actions = [0,1]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 000300
#         x x x o
#         o o o o
#         o o x o
#         x - - x
#         available = o1,o2,x2
#         current_player = x
#     """
#     ide = "000300"
#     p1 = 0b1111111010000
#     p2 = 0b1110000000101001
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 100300
#         x x x o
#         - x x o
#         o o o o
#         x o - x
#         available = x1,x11
#         current_player = x
#     """
#     ide = "100300"
#     p1 = 0b1000111110100
#     p2 = 0b1110011000001001
#     actions = [1,11]
#     next_status = [None] #implement it
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 010300
#         x x x o
#         o o o o
#         o o x o
#         x - x -
#         available = o0,o2,x2
#         current_player = x
#     """
#     ide = "010300"
#     p1 = 0b1111111010000
#     p2 = 0b1110000000101010
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 110300
#         x x x o
#         - x x o
#         o o o o
#         x o x -
#         available = x0,x11
#         current_player = x
#     """
#     ide = "110300"
#     p1 = 0b1000111110100
#     p2 = 0b1110011000001010
#     actions = [0,11]
#     next_status = [None] #Implement it
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 020300
#         x x x o
#         o o o o
#         o x o o
#         x x - -
#         available = o1,x0,x1
#         current_player = x
#     """
#     ide = "020300"
#     p1 = 0b1111110110000
#     p2 = 0b1110000001001100
#     actions = [0,1]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 001300
#         x x x o
#         o x o o
#         - o o o
#         x - o x
#         available = x2,x7
#         current_player = x
#     """
#     ide = "001300"
#     p1 = 0b1101101110010
#     p2 = 0b1110010000001001
#     actions = [2,7]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 101300
#         x x x o
#         o x o o
#         o o o o
#         x - - x
#         available = x1,x2
#         current_player = x
#     """
#     ide = "101300"
#     p1 = 0b1101111110000
#     p2 = 0b1110010000001001
#     actions = [1,2]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 201300
#         x x x o
#         o x o o
#         - x o o
#         x o - x
#         available = x1,x7
#         current_player = x
#     """
#     ide = "201300"
#     p1 = 0b1101100110100
#     p2 = 0b1110010001001001
#     actions = [1,7]
#     next_status = [None] #TODO implement it
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 011300
#         x x x o
#         o o x o
#         - x o o
#         x - x o
#         available = o2,o7,x7
#         current_player = x
#     """
#     ide = "011300"
#     p1 = 0b1110100110001
#     p2 = 0b1110001001001010
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 111300
#         x x x o
#         o o x o
#         - o o o
#         x o x -
#         available = o0,x0,x7
#         current_player = x
#     """
#     ide = "111300"
#     p1 = 0b1110101110100
#     p2 = 0b1110001000001010
#     actions = [0,7]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#     """
#         ide 211300
#         x x x o
#         o o x o
#         o o o o
#         x - x -
#         available = x0,x2
#         current_player = x
#     """
#     ide = "211300"
#     p1 = 0b1110111110000
#     p2 = 0b1110001000001010
#     actions = [0,2]
#     next_status = ["0" + ide,"1" + ide]
#     data = TestState(ide,p1,p2,actions,-1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 0000000
#         x x x o
#         x x o o
#         x o o o
#         - x o x
#         available = o3
#         current_player = o
#     """
#     ide = "0000000"
#     p1 = 0b1001101110010
#     p2 = 0b1110110010000101
#     actions = [3]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0100000
#         x x x o
#         x x o o
#         x x x o
#         o x - x
#         available = o1
#         current_player = o
#     """
#     ide = "0100000"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0200000
#         x x x o
#         o x x o
#         o o x o
#         - x x x
#         available = none
#         current_player = o
#     """
#     ide = "0200000"
#     p1 = 0b1100111010000
#     p2 = 0b1110011000100111
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1200000
#         x x x o
#         x x o o
#         x o o o
#         x x - x
#         available = none
#         current_player = o
#     """
#     ide = "1200000"
#     p1 = 0b1001101110000
#     p2 = 0b1110110010001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0110000
#         x x x o
#         x x o o
#         x x x o
#         o - x x
#         available = o2
#         current_player = o
#     """
#     ide = "0110000"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100011
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1110000
#         x x x o
#         x x o o
#         x x x o
#         o x - x
#         available = o1
#         current_player = o
#     """
#     ide = "1110000"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0000100x
#         x x x o
#         x x o o
#         x x x o
#         o x x -
#         available = o0
#         current_player = o
#     """
#     ide = "0000100"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0100100
#         x x x o
#         o x o o
#         o o x o
#         - x x x
#         available = None
#         current_player = o
#     """
#
#     ide = "0100100"
#     p1 = 0b1101111010000
#     p2 = 0b1110010000100111
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 1100100
#         x x x o
#         x x o o
#         x o o o
#         x x x -
#         available = None
#         current_player = o
#     """
#     ide = "1100100"
#     p1 = 0b1001101110000
#     p2 = 0b1110110010001110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 0010100
#         x x x o
#         x x o o
#         x x x o
#         o x x -
#
#         available = o0
#         current_player = o
#     """
#
#     ide = "0010100"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0100200
#         x x x o
#         x x o o
#         x x x o
#         o x - x
#         available = o1
#         current_player = o
#     """
#     ide = "0100200"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#
#
#
#     """
#         ide 0010200
#         x x x o
#         x x o o
#         x x x o
#         o x x -
#         available = none
#         current_player = o
#     """
#
#     ide = "0010200"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 0110200
#         x x x o
#         - x x o
#         x x x o
#         o o o o
#         available = o11
#         current_player = o
#     """
#     ide = "0110200"
#     p1 = 0b1000100011111
#     p2 = 0b1110011011100000
#     actions = [11]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#
#     """
#         ide 0001200
#         x x x o
#         x o o o
#         x o x o
#         x x - x
#         available = o1
#         current_player = o
#     """
#     ide = "0001200"
#     p1 = 0b1011101010000
#     p2 = 0b1110100010101101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0011200
#         x x x o
#         x o o o
#         x o x o
#         x x x -
#         available = o0
#         current_player = o
#     """
#     ide = "0011200"
#     p1 = 0b1011101010000
#     p2 = 0b1110100010101110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0021200
#         x x x o
#         o x o o
#         o x x o
#         x x - x
#         available = o1,
#         current_player = o
#     """
#     ide = "0021200"
#     p1 = 0b1101110010000
#     p2 = 0b1110010001101101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         id 1021200
#         x x x o
#         o o x o
#         o x x o
#         x x x -
#         available = o0
#         current_player = o
#     """
#     ide = "1021200"
#     p1 = 0b1110110010000
#     p2 = 0b1110001001101110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0002200
#         x x x o
#         x x o o
#         x o o o
#         - x o x
#         available = o3
#         current_player = o
#     """
#     ide = "0002200"
#     p1 = 0b1001101110010
#     p2 = 0b1110110010000101
#     actions = [3]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0102200
#         x x x o
#         x x o o
#         x x x o
#         o x - x
#         available = o1
#         current_player = o
#     """
#     ide = "0102200"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0202200
#         x x x o
#         o x x o
#         o o x o
#         - x x x
#         available = none
#         current_player = o
#     """
#     ide = "0202200"
#     p1 = 0b1100111010000
#     p2 = 0b1110011000100111
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1202200
#         x x x o
#         x x o o
#         x o o o
#         x x - x
#         available = none
#         current_player = o
#     """
#     ide = "1202200"
#     p1 = 0b1001101110000
#     p2 = 0b1110110010001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         id 0012200
#         x x x o
#         x x x o
#         x x o o
#         - x x o
#         available = o3
#         current_player = o
#     """
#     ide = "0012200"
#     p1 = 0b1000100110001
#     p2 = 0b1110111011000110
#     actions = [3]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0112200
#         x x x o
#         x x o o
#         x x x o
#         o x x -
#         available = o
#         current_player = o
#     """
#     ide = "0112200"
#     p1 = 0b1001100011000
#     p2 = 0b1110110011100110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0212200
#         x x x o
#         o x x o
#         o o x o
#         - x x x
#         available = none
#         current_player = o
#     """
#     ide = "0212200"
#     p1 = 0b1100111010000
#     p2 = 0b1110011000100111
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1212200
#         x x x o
#         x o x o
#         x x o o
#         x x x -
#         available = none
#         current_player = o
#     """
#     ide = "1212200"
#     p1 = 0b1010100110000
#     p2 = 0b1110101011001110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0022200
#         x x x o
#         x x o o
#         x o x o
#         o x - x
#         available = o1
#         current_player = o
#     """
#     ide = "0022200"
#     p1 = 0b1001101011000
#     p2 = 0b1110110010100101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1022200
#         x x x o
#         x x x o
#         x x x o
#         o x x -
#         available = o0
#         current_player = o
#     """
#     ide = "1022200"
#     p1 = 0b1000100011000
#     p2 = 0b1110111011100110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0000300
#         x x x o
#         o x o o
#         o x x o
#         x x - x
#         available = o2
#         current_player = o
#     """
#     ide = "0000300"
#     p1 = 0b1101110010000
#     p2 = 0b1110010001101101
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0010300
#         x x x o
#         o x o o
#         o x x o
#         x x x -
#         available = None
#         current_player = o
#     """
#     ide = "0010300"
#     p1 = 0b1101110010000
#     p2 = 0b1110010001101110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0020300
#         x x x o
#         o x o o
#         o x x o
#         x x - x
#         available = o1
#         current_player = o
#     """
#     ide = "0020300"
#     p1 = 0b1101110010000
#     p2 = 0b1110010001101101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1020300
#         x x x o
#         o o x o
#         o x x o
#         x x x -
#         available = o0
#         current_player = o
#     """
#     ide = "1020300"
#     p1 = 0b1110110010000
#     p2 = 0b1110001001101110
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0001300
#         x x x o
#         o x o o
#         - x o o
#         x x x x
#         available = o7
#         current_player = o
#     """
#     ide = "0001300"
#     p1 = 0b1101100110000
#     p2 = 0b1110010001001111
#     actions = [7]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1001300
#         x x x o
#         x x o o
#         x o o o
#         x - o x
#         available = None
#         current_player = o
#     """
#     ide = "1001300"
#     p1 = 0b1001101110010
#     p2 = 0b1110110010001001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0101300
#         x x x o
#         o x x o
#         o o x o
#         x - x x
#         available = o1
#         current_player = o
#     """
#     ide = "0101300"
#     p1 = 0b1100111010000
#     p2 = 0b1110011000101011
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#
#     """
#         ide 1101300
#         x x x o
#         o x o o
#         o x o o
#         x x - x
#         available = o1
#         current_player = o
#     """
#     ide = "1101300"
#     p1 = 0b1101110110000
#     p2 = 0b1110010001001101
#     actions = [1]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0011300
#         x x x o
#         x x x o
#         x x o o
#         x - x o
#         available = o2
#         current_player = o
#     """
#     ide = "0011300"
#     p1 = 0b1000100110001
#     p2 = 0b1110111011001010
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0111300
#         x x x o
#         o x x o
#         - o x o
#         x o x x
#         available = none
#         current_player = o
#     """
#     ide = "0111300"
#     p1 = 0b1100101010100
#     p2 = 0b1110011000101011
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1111300
#         x x x o
#         x x x o
#         x o o o
#         x o x -
#         available = o0
#         current_player = x
#     """
#     ide = "1111300"
#     p1 = 0b1000101110100
#     p2 = 0b1110111010001010
#     actions = [0]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 0211300
#         x x x o
#         o x x o
#         o o x o
#         x - x x
#         available = o2
#         current_player = o
#     """
#     ide = "0211300"
#     p1 = 0b1100111010000
#     p2 = 0b1110011000101011
#     actions = [2]
#     next_status = ["0" + ide]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 1211300
#         x x x o
#         o x x o
#         o x o o
#         x x x -
#         available = None
#         current_player = o
#     """
#     ide = "1211300"
#     p1 = 0b1100110110000
#     p2 = 0b1110011001001110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,1,next_status)
#     dataset[ide] = data
#     """
#         ide 00000000
#         x x x o
#         x x o o
#         x o o o
#         o o o x
#         available = None
#         current_player =
#     """
#
#     ide = "00000000"
#     p1 = 0b1001101111110
#     p2 = 0b1110110010000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00100000
#         x x x o
#         x x o o
#         x x o o
#         o o o x
#         available = o1
#         current_player = o
#     """
#     ide = "00100000"
#     p1 = 0b1001100111110
#     p2 = 0b1110110011000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00110000
#         x x x o
#         x x o o
#         x x o o
#         o o x x
#         available = none
#         current_player = o
#     """
#     ide = "00110000"
#     p1 = 0b1001100111100
#     p2 = 0b1110110011000011
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 01110000
#         x x x o
#         x x o o
#         x x o o
#         o o o x
#         available = none
#         current_player = none
#     """
#     ide = "01110000"
#     p1 = 0b1001100111110
#     p2 = 0b1110110011000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00000100
#         x x x o
#         x x o o
#         x x x o
#         o o o o
#         available = none
#         current_player = none
#     """
#     ide = "00000100"
#     p1 = 0b1001100011111
#     p2 = 0b1110110011100000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         ide 00010100
#         x x x o
#         x x o o
#         x x x o
#         o o o o
#
#         available = none
#         current_player = x
#     """
#     ide = "00010100"
#     p1 = 0b1001100011111
#     p2 = 0b1110110011100000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00100200
#         x x x o
#         x x o o
#         x x o o
#         o o o x
#         available = none
#         current_player = o
#     """
#     ide = "00100200"
#     p1 = 0b1001100111110
#     p2 = 0b1110110011000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         ide 00110200
#         x x x o
#         o o o o
#         o o x o
#         o o o o
#         available = o11
#         current_player = o
#     """
#     ide = "00110200"
#     p1 = 0b1111111011111
#     p2 = 0b1110000000100000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         ide 00001200
#         x x x o
#         x o o o
#         x o o o
#         x x o x
#         available = o1
#         current_player = o
#     """
#     ide = "00001200"
#     p1 = 0b1011101110010
#     p2 = 0b1110100010001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00011200
#         x x x o
#         x o o o
#         x o o o
#         x x x o
#         available = none
#         current_player = o
#     """
#     ide = "00011200"
#     p1 = 0b1011101110001
#     p2 = 0b1110100010001110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00021200
#         x x x o
#         o x o o
#         o o o o
#         x x o x
#         available = o1,
#         current_player = o
#     """
#     ide = "00021200"
#     p1 = 0b1101111110010
#     p2 = 0b1110010000001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         ide 01021200
#         x x x o
#         o o x o
#         o x o o
#         x x x o
#         available = o0
#         current_player = o
#     """
#
#     ide = "01021200"
#     p1 = 0b1110110110001
#     p2 = 0b1110001001001110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00002200
#         x x x o
#         x x o o
#         x o o o
#         o o o x
#         available = o3
#         current_player = o
#     """
#
#     ide = "00002200"
#     p1 = 0b1001101111110
#     p2 = 0b1110110010000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00102200
#         x x x o
#         x x o o
#         x x o o
#         o o o x
#         available = none
#         current_player = o
#     """
#
#     ide = "00102200"
#     p1 = 0b1001100111110
#     p2 = 0b1110110011000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         id 00012200
#         x x x o
#         x x o o
#         x o o o
#         o o o o
#         available = o3
#         current_player = o
#     """
#     ide = "00012200"
#     p1 = 0b1001101111111
#     p2 = 0b1110110010000000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00112200
#         x x x o
#         x x o o
#         x x x o
#         o o o o
#         available = o
#         current_player = o
#     """
#     ide = "00112200"
#     p1 = 0b1001100011111
#     p2 = 0b1110110011100000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00022200
#         x x x o
#         x x o o
#         x o o o
#         o o o x
#         available = o1
#         current_player = o
#     """
#     ide = "00022200"
#     p1 = 0b1001101111110
#     p2 = 0b1110110010000001
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 01022200
#         x x x o
#         x x x o
#         x x x o
#         o o o o
#         available = o0
#         current_player = o
#     """
#     ide = "01022200"
#     p1 = 0b1000100011111
#     p2 = 0b1110111011100000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00000300
#         x x x o
#         o x o o
#         o o o o
#         x x o x
#         available = o2
#         current_player = o
#     """
#
#     ide = "00000300"
#     p1 = 0b1101111110010
#     p2 = 0b1110010000001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00020300
#         x x x o
#         o x o o
#         o o o o
#         x x o x
#         available = o1
#         current_player = o
#     """
#     ide = "00020300"
#     p1 = 0b1101111110010
#     p2 = 0b1110010000001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         ide 01020300
#         x x x o
#         o o x o
#         o x o o
#         x x x o
#         available = o0
#         current_player = o
#     """
#     ide = "01020300"
#     p1 = 0b1110110110001
#     p2 = 0b1110001001001110
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00001300
#         x x x o
#         o x o o
#         o o o o
#         x x x x
#         available = o7
#         current_player = o
#     """
#     ide = "00001300"
#     p1 = 0b1101111110000
#     p2 = 0b1110010000001111
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00101300
#         x x x o
#         o x x o
#         o o o o
#         x o x x
#         available = o1
#         current_player = o
#     """
#     ide = "00101300"
#     p1 = 0b1100111110100
#     p2 = 0b1110011000001011
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     """
#         ide 01101300
#         x x x o
#         o x o o
#         o o o o
#         x x o x
#         available = o1
#         current_player = o
#     """
#     ide = "01101300"
#     p1 = 0b1101111110010
#     p2 = 0b1110010000001101
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00011300
#         x x x o
#         x x x o
#         x x o o
#         x o o o
#         available = o2
#         current_player = o
#     """
#     ide = "00011300"
#     p1 = 0b1000100110111
#     p2 = 0b1110111011001000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 01111300
#         x x x o
#         x x x o
#         x o o o
#         x o o o
#         available = o0
#         current_player = x
#     """
#     ide = "01111300"
#     p1 = 0b1000101110111
#     p2 = 0b1110111010001000
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#     """
#         ide 00211300
#         x x x o
#         o x x o
#         o o o o
#         x o x x
#         available = o2
#         current_player = o
#     """
#     ide = "00211300"
#     p1 = 0b1100111110100
#     p2 = 0b1110011000001011
#     actions = [None]
#     next_status = [None]
#     data = TestState(ide,p1,p2,actions,0,next_status)
#     dataset[ide] = data
#
#     return dataset

class TestMCTS(unittest.TestCase):


    def setUp(self):
        self.dataset = test.testdata.gen_data2()
        board.Board.column_len = 4
        board.Board.row_len = 4
        board.Board.index_len = board.Board.column_len * board.Board.row_len


    def test_is_fully_expanded(self):
        pass

    #@unittest.skip("")
    def test_is_available(self):
        data = test.testdata.gen_data3()
        for d in data:
            n = d.node()
            actual = n.available_actions()
            self.assertEqual(d.expected,actual)

    #@unittest.skip("")
    def test_expand(self):
        for count in range(100):
            node = self.dataset["0"]
            while not node.next_status[0] is None:
                if node.ide == '10100':
                    print('hoge')

                b = board.Board(node.player1_board,node.player2_board,node.current_player)
                s = state.State(b)
                n = treenode.Node(s,None)
                child = n.expand()

                p1 = child.state.board.boards[1]
                p2 = child.state.board.boards[-1]
                found = False
                d = None
                for next_id in node.next_status:
                    d = self.dataset[next_id]
                    if d.player1_board == p1 and d.player2_board == p2:
                        found = True
                        break

                if node.ide == "1100":
                    break

                print("===expand information===")
                print(str(node.ide))
                print(str(node.actions))
                print(str(node.next_status))
                print("actual   p1 " + bin(p1))
                print("actual   p2 " + bin(p2))
                print("expected p1 " + bin(d.player1_board))
                print("expected p2 " + bin(d.player2_board))
                print("=========================")
                # print(bin(dataset["00"].player1_board))
                # print(bin(dataset["00"].player2_board))
                if not found :
                    self.fail(node.ide)

                print(str(child.depth) + " passed")
                node = d

    def test_expand_and_bp(self):
        d = self.dataset["0"]
        b = board.Board(d.player1_board,d.player2_board,d.current_player)
        s = state.State(b)
        n = treenode.Node(s,None)
        root = n
        i = 0
        while True:
            tmp = n.expand()
            if tmp is None: break
            n = tmp
            self.assertTrue(n.depth,i)
            print("asserted depth " + str(i))
            i += 1

        n.back_propagate(100)

        self.test_node_value(root,True)


    def test_node_value(self,node=None,run=False):
        if not run : return
        if node.children is None:
            self.assertEqual(node.value,100)
            self.assertEqual(node.visits,1)
        self.assertEqual(len(node.children),1)
        for child in node.children:
            self.test_node_value(child)

    def test_select(self):
        treenode.Node.total_visits = 0
        d = self.dataset["0"]
        b = board.Board(d.player1_board,d.player2_board,d.current_player)
        s = state.State(b)
        n = treenode.Node(s,None)

        child = treenode.Node(None,None)
        child.value = 20
        child.visits = 1
        treenode.Node.total_visits += 1
        n.children[1] = child

        child = treenode.Node(None,None)
        child.value = 20
        child.visits = 2
        treenode.Node.total_visits += 2
        n.children[2] = child

        child = treenode.Node(None,None)
        child.value = 20
        child.visits = 10
        treenode.Node.total_visits += 10
        n.children[3] = child

        selected = n.select()
        self.assertEqual(selected.ucb1(),22.264927971243914)
        self.assertEqual(selected.visits,1)



    def test_is_fully_expanded(self):
        d = self.dataset["0"]
        b = board.Board(d.player1_board,d.player2_board,d.current_player)
        s = state.State(b)
        n = treenode.Node(s,None)

        while not n.is_fully_expanded():
            n.expand()

        self.assertEqual(len(n.children),len(d.next_status))


if __name__ == '__main__':
    unittest.main()



