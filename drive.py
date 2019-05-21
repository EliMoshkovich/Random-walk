from networkx import *
import networkx as nx
import matplotlib.pyplot as plt


# This class is responsible for building the graph.
class Drive:

    # Init the drive.
    def __init__(self):
        print("")

    # Draw the regular graph.
    def regular_graph(self):
        G = random_regular_graph(self.e, self.v)
        self.wr(G)
        draw(G)
        plt.show()

    # Draw the tree graph.
    def tree_graph(self):
        G = random_tree(self.v)
        self.wr(G)
        draw(G)
        plt.show()

    # Write to the output file.
    def wr(self, G):
        fh = open("output_graph.txt", 'wb')
        nx.write_edgelist(G, fh)

    # Draw the random graph.
    def random_graph(self):
        G = gnm_random_graph(self.v, self.e)
        self.wr(G)
        draw(G)
        plt.show()

    # Set v.
    def update_v(self, v_input):
        self.v = v_input

    # Set e.
    def update_e(self, e_input):
        self.e = e_input

    # This function shows the graph to the user.
    def show(self, G):
        draw(G)
        plt.show()





