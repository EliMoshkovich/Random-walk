import networkx as nx
import matplotlib.pyplot as plt
from networkx import *

class GraphFromTxt:
    def __init__(self, text): # init from text file
        self.GraphStan = []
        file = open(text, "r")
        for line in file:
            self.GraphStan.append(line)

    def print_list(self):
        print(self.GraphStan)

    def length(self):
        print(self.GraphStan.__len__())

    def print_edges(self, G):
        print(G.edges())

    def parse(self):
        return nx.parse_edgelist(self.GraphStan, nodetype=int)


G_listed = GraphFromTxt("small.txt")
G_listed.length()
G = G_listed.parse()

# draw(G)
# plt.show()

"""
add field of stepped node to each node in graph.
"""

nx.set_node_attributes(G, 0 , 'step')
print(sorted(G.nodes))
print(G.node[2]['step'])
G.node[2]['step'] += 1
print(G.node[2]['step'])





# import networkx as nx
#
#
# class GraphFromTxt:
#     def __init__(self, text, max_e):
#         self.m=max_e
#         self.GraphStan = []
#         file = open(text, "r")
#         for line in file:
#             self.GraphStan.append(line)
#
#     def print_list(self):
#         print(self.GraphStan)
#
#     def length(self):
#         print(self.GraphStan.__len__())
#
#     def print_edges(self, G):
#         print(G.edges())
#
#     def parse(self):
#         integers = [x for x in self.GraphStan if (x, int)]
#         integers = integers[-self.m:]
#         print(integers.__len__())
#         return nx.parse_edgelist(integers, nodetype=int)
#
#
# max_e = 4800000
# for x in range(max_e, 7600595, 3):
#     G = GraphFromTxt("stan.txt", max_e)
#     G.lenth()
#     a = G.parse()


