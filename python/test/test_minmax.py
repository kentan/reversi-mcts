import unittest
from player.minmax_player import MinMaxTree
from state import State
from board import Board


class TestMinMaxTree(MinMaxTree):
    suquential_number = 0

    def dfs_evaluate(self, depth):
        if depth == 0:
            self.value()
            return
        self.expand()
        for action,child in self.children.items():
            child.dfs_evaluate(depth - 1)

        self.best_action, self.best_child = self.pick_best()
        self.update()

    def expand(self):
        self.children = {}
        self.children[0] = TestMinMaxTree(State(Board()),self.depth + 1,self)
        self.children[1] = TestMinMaxTree(State(Board()),self.depth + 1,self)
        self.children[2] = TestMinMaxTree(State(Board()),self.depth + 1,self)

    def value(self):
        self.v = TestMinMaxTree.suquential_number
        TestMinMaxTree.suquential_number += 1


    def show_tree_structure(self,indent):

        print(indent + str(self.v))
        for action,child in self.children.items():
            child.show_tree_structure(indent + " ")

class TestMinMax(unittest.TestCase):
    def test_minmax(self):

        tree = TestMinMaxTree(State(Board()),0,None)
        tree.dfs_evaluate(2)
        self.assertEqual(tree.v,6)

        TestMinMaxTree.suquential_number = 0
        tree = TestMinMaxTree(State(Board()), 0, None)
        tree.dfs_evaluate(3)
        self.assertEqual(tree.v, 20)



        # tree.show_tree_structure("")


