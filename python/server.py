from flask import Flask
from flask import request
import os
import ast
import json
import player.mcts_player
import board
import traceback
import pickle
import treenode

app = Flask(__name__)

from flask import render_template

ai_player = None


@app.route('/start', methods=['GET'])
def start():
    try:
       global ai_player
       root = pickle.load(open("./trainer/data.pickle", "rb"))
       treenode.Node.total_visits = root.total_visits_for_pickling
       ai_player = player.mcts_player.MCTSPlayer(root)
       return ""
    except Exception as e:
       traceback.print_exc()


def convert_to_board(data):
    try:
       p1 = data["p1"]
       p2 = data["p2"]
       p1 = board.BoardUtil.string_to_bit(p1)
       p2 = board.BoardUtil.string_to_bit(p2)
       return board.Board(p1,p2,-1)
    except Exception as e:
       traceback.print_exc()


@app.route('/ai', methods=['POST'])
def next_action():
    if request.method == 'POST':
      try:
          print("ai")
          print(hoge)
          print(request.data);
          data = ast.literal_eval(request.data.decode("utf-8"))
          print(data)
          b = convert_to_board(data)
          action = data["action"]
          next_action = ai_player.action(b,action)
          print(next_action)
          rv = json.dumps({"next":next_action})
          rv = json.JSONEncoder().encode({"next":next_action})
          return rv
      except Exception as ex:
          traceback.print_exc()
          return(str(ex));
      except Error as er:
          traceback.print_exc()
          return(str(er));


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

