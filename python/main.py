import board
import player.mcts_player
import player.random_player
import player.minmax_player
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
    #player1 = player.mcts_player.MCTSPlayer(root)
    player1 = player.random_player.RandomPlayer()
    player2 = player.minmax_player.MinMaxPlayer(1)
    b = board.Board()


    a = None
    end = False
    passed = False
    while not end:
        for p in (player1,player2):
            if end: break
            a2 = p.action(b,a)

            if a2 == -1:
                if passed:
                    end = True
                    print("passed2")
                    break
                else:
                    passed = True
                    print("passed")
                    continue
            b.put(a2)
            #b.show_board()
            a = a2
            if b.is_end(): end = True



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