import datetime

import networkx as nx
import matplotlib.pyplot as plt
from networkx import *
import numpy
import csv
import drive
import Rw
# import pgn2gif as pg
from ShowGraph import ShowGraph


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

    def length_int(self):
        return self.GraphStan.__len__()

    def print_edges(self, G):
        print(G.edges())

    def parse(self):
        return nx.parse_edgelist(self.GraphStan, nodetype=int)


G_listed = GraphFromTxt("output_graph.txt")
G_listed.length()
G = G_listed.parse()
# ShowGraph.nodes(G)


"""
add field of stepped node to each node in graph.
https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.classes.function.set_node_attributes.html
"""

nx.set_node_attributes(G, 0 , 'step')
print(sorted(G.nodes))
# print(G.node[2]['step'])
# G.node[2]['step'] += 3
# G.node[3]['step'] += 2
# G.node[4]['step'] += 1
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


def min_stepped_node(G, adj):
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


def is_covered(G):
    nodes = sorted(G.nodes())
    for node in nodes:
        if stepped(G, node) == 0:
            return False
    return True


# nx.draw_circular(G,  node_color=node_colors , node_size=10)
# plt.show()

# show_graph(G, 0)


def get_print_stepped_list(G):
    stepped_list = []
    for node in sorted(G.nodes()):
        stepped_list.append(stepped(G, node))
    # print(sorted(G.nodes()))
    # print('coverage steps of Graph :', stepped_list)
    # converting the list to string of integers
    string_of_int = (', '.join(str(x) for x in stepped_list))

    # write steps to csv file
    # time = str(datetime.datetime.now()).replace('.', '_').replace(':', '_')
    with open('output_walks2.txt', 'a') as out:
        out.write('\n')
        # text = "Coverage steps of Graph:"
        # out.write(text)
        out.write('\n')
        for row in string_of_int:
            for col in row:
                out.write('{0}'.format(col))
    return stepped_list


#def print_edge_coverage(G):
#    edge_list = []
#    for edge in G.):
#        edge_list.append(stepped(G, edge))
#    print(sorted(G.edge()))
#    print('coverage steps of Graph :', edge_list)
#pos = nx.spring_layout(G)

show = ShowGraph(G)
pos = nx.spring_layout(G)  # positions for all nodes
def random_walk(G, s, c1 ):
    # print("random walk function")
    if not is_covered(G):
        adj_n = G.adj[s].items()
        next_node = min_stepped_node(G, adj_n)
        # to_blue(next_node)
        print("next node is: "+str(next_node))
        G.node[next_node]['step'] += 1
        # node_colors[next_node] = 'g'
        show.to_blue(next_node)
        # if(c1%10==0):
        showG = show.show_graph
        showG(G, next_node)
            # showG(G, next_node)
        c1 = c1 + 1
        get_print_stepped_list(G)
 #       print_edge_coverage(G)
        random_walk(G, next_node, c1)
    else:
        get_print_stepped_list(G)


def csv_expo(data):
    a = numpy.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    numpy.savetxt("foo.csv", a, delimiter=",")


nodes = sorted(G.nodes())
s = nodes[0]
G.node[s]['step'] += 1
# ShowGraph.show_graph(G, 0)
random_walk(G, s, 1)

# random_walk(G)

# import networkx as nx
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


