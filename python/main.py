import board
import player.mcts_player
import player.random_player
import pickle
import treenode
import copy

result = {"player1": 0, "player2": 0, "draw": 0}
root = None

def setup():
    global root
    root = pickle.load(open("./trainer/data.pickle", "rb"))
    treenode.Node.total_visits = root.total_visits_for_pickling

def play_game():
    player1 = player.mcts_player.MCTSPlayer(root)
    player2 = player.random_player.RandomPlayer()
    b = board.Board()


    a = None
    end = False
    while not end:
        for p in (player1,player2):
            a = p.action(b,a)
            b.put(a)
            #b.show_board()
            if b.is_end():
                end = True
                break

    b.show_board()
    result[b.get_wining_player()] += 1
    print(b.get_wining_player())

def main():
    setup()
    for i in range(30):
        play_game()

    print(result)

if __name__ == '__main__':
    main()