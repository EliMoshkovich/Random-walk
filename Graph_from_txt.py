import networkx as nx
import matplotlib.pyplot as plt
from networkx import *
import drive
import Rw
# import pgn2gif as pg

class GraphFromTxt:
    def __init__(self, text): # init from text file
        self.GraphStan = []
        file = open(text, "r")
        for line in file:
            self.GraphStan.append(line)

    def print_list(self):
        print(self.GraphStan)

    def length(self):
        print("num of nodes is: " + str(self.GraphStan.__len__()))

    def print_edges(self, G):
        print(G.edges())

    def parse(self):
        return nx.parse_edgelist(self.GraphStan, nodetype=int)


G_listed = GraphFromTxt("small.txt")
G_listed.length()
G = G_listed.parse()

node_colors = []
for i in range(0, 8):
        if i < 1:
           node_colors.append('b')
        else:
           node_colors.append('r')
"""
add colors to grapg
https://stackoverflow.com/questions/20523327/python-and-networkx-how-to-change-the-color-of-nodes
"""

# print(node_colors)
# nx.draw_circular(G, node_color=node_colors)
# plt.show()
# plt.savefig('visual graphs\\books_read2.png')

"""
add field of stepped node to each node in graph.
https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.classes.function.set_node_attributes.html
"""

nx.set_node_attributes(G, 0 , 'step')
print(sorted(G.nodes))
# print(G.node[2]['step'])
G.node[2]['step'] += 3
G.node[3]['step'] += 2
G.node[4]['step'] += 1
# print(G.node[2]['step'])

"""
tree test 
"""
# tree = nx.bfs_tree(G, 1)
# tree = dict(nx.bfs_predecessors(G, 1))
# print(tree)
# draw(tree)
# plt.show()


def stepped(G, node_index):
    # print("node " + str(node_index) + " has stepped " + str(G.node[node_index]['step']) + " times")
    return G.node[node_index]['step']


"""
param: list of nodes num
return : node with lowest stepped times 
"""


def min_stepped(G, adj):
    if len(adj) > 0:
        min_step = 0
        node_index = 0
        for node in adj:  # init min_step
            min_step = stepped(G, node[0])
            node_index = node[0]
            break

        for node in adj:
            n_stepped = stepped(G, node[0])
            if(n_stepped < min_step):
                min_step = n_stepped
                node_index = node[0]
    return node_index


"""
random walk algoritm
"""


def random_walk(G):
    print("random walk function")
    nodes = sorted(G.nodes())
    s = nodes[0]
    adj_n = G.adj[s].items()
    # print(adj_n)
    print(min_stepped(G, adj_n))



random_walk(G)


# random_walk(G)

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


