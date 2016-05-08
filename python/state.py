class State:
    def __init__(self,board):
        self.board = board

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return self.board.__hash__()

