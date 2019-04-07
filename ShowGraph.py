# from Graph_from_txt import GraphFromTxt
import networkx as nx
from networkx import *
import matplotlib.pyplot as plt


class ShowGraph():

    def __init__(self, G):
        print("init - show graph")
        self.node_blue_colors = []
        self.node_red_colors = []
        self.node_green_color = []
        self.pos = nx.spring_layout(G)  # positions for all nodes

        for i in range(0, len(G.nodes())):
            if i < 1:
                self.node_blue_colors.append(i)
            else:
                self.node_red_colors.append(i)


    # def get_blue_color(self):
    #     return self.node_blue_colors
    #
    # def get_red_color(self):
    #     return self.node_red_colors
    #
    # def get_pos(self):
    #     return self.pos
    """, blue, red, _pos"""
    def show_graph(self, G, current_node):
        # with_labels=True,
        # fig = plt.figure(figsize=(12, 12))
        # ax = plt.subplot(111)
        # ax.set_title('Graph - Shapes', fontsize=10)
        # print(self.node_blue_colors)
        # print(self.node_red_colors)
        nx.draw(G, self.pos, nodelist=self.node_blue_colors, node_color='r', node_size=250, alpha=0.8, with_labels=True)
        nx.draw(G, self.pos, nodelist=self.node_red_colors, node_color='b', node_size=250, alpha=0.8, with_labels=True)
        nx.draw(G, self.pos, nodelist=[current_node], node_color='g', node_size=250, alpha=0.8, with_labels=True)

        # nx.draw(G, pos, node_color=node_colors, node_size=250, with_labels=True)
        plt.title("Random Walk")
        plt.show()
        plt.savefig('random_walk_2d.png', dpi=250)
        # node_colors[next_node] = 'b'


    def to_red(self, n):
        if n in self.node_blue_colors:
            self.node_blue_colors.remove(n)
            self.node_red_colors.append(n)

    def to_blue(self,n):
        if n in self.node_red_colors:
            self.node_red_colors.remove(n)
            self.node_blue_colors.append(n)

    def printt(self):
        print("test")



"""
add colors to grapg
https://stackoverflow.com/questions/20523327/python-and-networkx-how-to-change-the-color-of-nodes
"""

# print(node_colors)
# nx.draw_circular(G, node_color=node_colors)
# plt.show()
# plt.savefig('visual graphs\\books_read2.png')