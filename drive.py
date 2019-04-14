from networkx import *
import networkx as nx
import matplotlib.pyplot as plt


class Drive:
    v = 10
    e = 10

    def __init__(self):
        print("init drive")

    def regular_graph(self):
        draw(random_regular_graph(self.e, self.v))
        plt.show()

    def tree_graph(self):
        G = random_tree(self.v)
        self.wr(G)
        draw(G)
        plt.show()

    def wr(self, G):
        fh = open("output_graph.txt", 'wb')
        nx.write_edgelist(G, fh)

    def random_graph(self):
        G = gnm_random_graph(self.v, self.e)
        self.wr(G)
        draw(G)
        plt.show()

    def update_v(self, v_input):
        self.v = v_input

    def update_e(self, e_input):
        self.e = e_input

    def show(self,G):
        draw(G)
        plt.show()





