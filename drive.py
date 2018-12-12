from tkinter import *
from networkx import *
import matplotlib.pyplot as plt


class Drive:

    def __init__(self):
        print("init")

    @staticmethod
    def regular_graph():
        draw(random_regular_graph(4, 10))
        plt.show()

    @staticmethod
    def tree_graph():
        draw(random_tree(10))
        plt.show()

    @staticmethod
    def random_graph():
        draw(gnm_random_graph(10, 20))
        plt.show()





