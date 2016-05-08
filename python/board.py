


class Board:
    row_len = 8
    column_len = 8
    index_len = row_len * column_len

    def __init__(self,mine=None,yours=None,player=1):
        self.player1 = 1
        self.player2 = -1
        self.current_player = player

        mine = 0b1000000001000000000000000000000000000 if mine is None else mine
        yours = 0b100000010000000000000000000000000000 if yours is None else yours

        self.boards = {self.player1:mine,self.player2:yours}
        self.pos_to_flip = 0


    def is_tile(self,pos):
        for b in self.boards.values():
            if (b >> pos) & 0b1 == 1 : return True
        return False

    def is_my_tile(self,pos):
        if (self.boards[self.current_player] >> pos ) & 0b1 == 1: return True
        return False

    def is_your_tile(self,pos):
        if (self.boards[self.current_player * -1] >> pos ) & 0b1 == 1: return True
        return False

    def is_beyond_upper(self,pos):
        return pos >= Board.index_len

    def is_beyond_lower(self,pos):
        return pos < 0

    def is_beyond_right(self,pos):
        return (pos + 1) % Board.column_len == 0

    def is_beyond_left(self,pos):
        return pos % Board.column_len == 0

    def is_overstepping(self,pos,horizontal,vertical):
        if vertical == "up":
            if self.is_beyond_upper(pos) : return True
        elif vertical == "down":
            if self.is_beyond_lower(pos) : return True

        if horizontal == "right":
            if self.is_beyond_right(pos): return True
        elif horizontal == "left":
            if self.is_beyond_left(pos): return True

        return False

    def is_puttable_direction(self,pos,horizontal,vertical):
        if self.is_tile(pos): return False

        if vertical == "up":
            v_move = Board.column_len
        elif vertical == "down":
            v_move = -1 * Board.column_len
        elif vertical == "none":
            v_move = 0
        else:
            print("err in vertical value " + vertical)

        if horizontal == "right":
            h_move = -1
        elif horizontal == "left":
            h_move = 1
        elif horizontal == "none":
            h_move = 0
        else:
            print("err in horizontal value " + horizontal)


        pos += (v_move + h_move)
        if pos < 0 or pos > Board.index_len: return False
        if self.is_my_tile(pos) : return False
        if self.is_overstepping(pos,horizontal,vertical): return False

        pos_to_flip_tmp = 0
        while self.is_your_tile(pos):
            pos_to_flip_tmp |= (1 << pos)
            pos += v_move
            pos += h_move
            if self.is_overstepping(pos,horizontal,vertical): return False

        if not self.is_my_tile(pos):
            return False

        self.pos_to_flip |= pos_to_flip_tmp
        return True

    def is_puttable(self,pos):
        self.pos_to_flip = 0
        b = self.is_puttable_direction(pos,"right","none")
        b |= self.is_puttable_direction(pos,"left","none")
        b |= self.is_puttable_direction(pos,"none","up")
        b |= self.is_puttable_direction(pos,"none","down")
        b |= self.is_puttable_direction(pos,"right","up")
        b |= self.is_puttable_direction(pos,"left","up")
        b |= self.is_puttable_direction(pos,"right","down")
        b |= self.is_puttable_direction(pos,"left","down")

        return b

    def puttable_tiles(self):
        return [pos for pos in range(Board.index_len) if self.is_puttable(pos)]

    def change_player(self):
        self.current_player *= -1

    def flip_tiles(self):
#        print(bin(self.pos_to_flip))
#        print(bin(self.boards[self.current_player]))
#        print(bin(self.boards[self.current_player * -1]))
        self.boards[self.current_player] |= self.pos_to_flip
        self.boards[self.current_player * -1] ^= self.pos_to_flip
#        print(bin(self.boards[self.current_player]))
#        print(bin(self.boards[self.current_player * -1]))

    def put(self,pos):
        if self.is_puttable(pos):
            self.boards[self.current_player] |= (1 << pos)

            self.flip_tiles()
            self.change_player()


    def is_end(self):
        return len(self.puttable_tiles()) == 0

    def check(self):
        b = 2**63-1
        for key,value in self.boards.items():
            b &= value
        assert b == 0

    def get_wining_player(self):
        b1 = bin(self.boards[self.player1]).count("1")
        b2 = bin(self.boards[self.player2]).count("1")
        if b1 > b2:
            return "player1"
        elif b1 == b2:
            return "draw"
        else:
            return "player2"

    def __eq__(self, other):
        result = True
        for player in (self.player1, self.player2):
            result &= self.boards[player] == other.boards[player]

        return result

    def __hash__(self):
        result = self.boards[self.player1]
        result |= self.boards[self.player2] << Board.index_len


    def show_board(self):
        print(bin(self.boards[self.player1]))
        print(bin(self.boards[self.player2]))
        for index in reversed(range(Board.index_len)):
            found = False
#            counter += 1
            if index != Board.index_len - 1 and index != 0 and (index + 1) % Board.column_len == 0 :
                print(' ')
            for key, value in self.boards.items():
                #print(bin(value))

                if (value >> index) & 0b1 == 0b1:
                    if key == 1:
                        print('o',end=' ')
                    else:
                        print('x',end=' ')
                    found = True
            if not found:
                print('-',end=' ')


        print("")
        print('=============')
mine = "00000000" +\
        "00000000" +\
        "00000000" +\
        "00010000" +\
        "00001000" +\
        "00000000" +\
        "00000000" +\
        "00000000"

yours = "00000000" +\
        "00000000" +\
        "00000000" +\
        "00001000" +\
        "00010000" +\
        "00000000" +\
        "00000000" +\
        "00000000"



    # mine = string_to_bit(mine)
    # yours = string_to_bit(yours)
    #
    #


class BoardUtil:
    @staticmethod
    def string_to_bit(s):
        b = 0b0
        for i in range(len(s)):
            if s[i] == '1':
                b |= (1 << (len(s) - 1  - i))

        return b

