import datetime
import math
import networkx as nx
import matplotlib.pyplot as plt
from networkx import *
import numpy
import csv
import drive
import Rw
# import pgn2gif as pg
import random
from ShowGraph import ShowGraph


class GraphFromTxt:


    def __init__(self): # init from text file
        print("GraphFromTxt __init__")
        self.GraphStan = []
        file = open("output_graph.txt", "r")
        for line in file:
            self.GraphStan.append(line)


        # self.G_listed = GraphFromTxt("output_graph.txt")
        self.G = GraphFromTxt.parse(self)
        self.show = ShowGraph(self.G)
        print("parse class")
        self.G_edges = sorted(self.G.edges())
        # print(self.G_edges)
        self.stepped_edges = [0] * len(self.G_edges)
        self.stepped_edges_remember = []


    def stepped(self, G, node_index):
    # print("node " + str(node_index) + " has stepped " + str(G.node[node_index]['step']) + " times")
        return G.node[node_index]['step']

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

    def get_index_of_edge(self, node1, node2):
        for i in range(len(self.G_edges)):
            edge = self.G_edges[i]
            # print(edge[0], node1 , " " , edge[1] , node2)
            if edge[0] == node1 and edge[1] == node2:
                return i

            elif edge[1] == node1 and edge[0] == node2:
                return i

        return -1


    def is_covered(self, G):
        nodes = sorted(G.nodes())
        for node in nodes:
            if self.stepped(G, node) == 0:
                return False
        return True

    def random_walk(self, G, s, c1):
        print("random walk function")
        print(len(G.nodes()))

        if not self.is_covered(G):
            mod = int(math.sqrt(len(G.nodes())))
            # print(int(mod))
            adj_n = G.adj[s].items()
            next_node = self.min_stepped_node(G, adj_n)
            # to_blue(next_node)
            print("next node is: " + str(next_node))
            G.node[next_node]['step'] += 1
            # node_colors[next_node] = 'g'
            self.show.to_blue(next_node)
            #if (c1 % mod == 1): #freddy
            showG = self.show.show_graph
            showG(G, next_node)
                # showG(G, next_node)
            c1 = c1 + 1
            print("c")
            print(c1)
            self.get_print_stepped_list(G)
            #       print_edge_coverage(G)
            index = self.get_index_of_edge(s, next_node)
            print("index ", index)
            self.stepped_edges[index] += 1
            print(self.stepped_edges)
            self.stepped_edges_remember.append(self.stepped_edges)
            self.edges_to_csv2(self.stepped_edges)
            print("len of mem is ", len(self.stepped_edges_remember))
            self.random_walk(G, next_node, c1)
        # else:
        #     get_print_stepped_list(G)

    def edges_to_csv(self):
        # print((self.stepped_edges_remember))
        self.G_edges
        with open('csvfile2.txt', 'w') as file:
            file.write("aaaaa")
            print("edges_to_csv")
            print(self.stepped_edges_remember)
            for line in self.stepped_edges_remember:
                file.write(line)
                file.write('\n')

    def edges_to_csv2(self, row):
        # print((self.stepped_edges_remember))
        self.G_edges
        with open('csvfile2.txt', 'a') as file:
                file.write(str(row))
                file.write('\n')


    def run_random(self):

        """
        add field of stepped node to each node in graph.
        https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.classes.function.set_node_attributes.html
        """
        nx.set_node_attributes(self.G, 0 , 'step')
        # print(sorted(self.G.nodes))
        nodes = sorted(self.G.nodes())
        s = nodes[0]
        # print(self.G.node[s])
        self.G.node[s]['step'] += 1
        print(self.G_edges)
        self.edges_to_csv()

        # ShowGraph.show_graph(G, 0)
        self.random_walk(self.G, 0, 1)
        # write_to_csv()
        # pos = nx.spring_layout(self.G)  # positions for all nodes

# print(G.node[2]['step'])
# G.node[2]['step'] += 3
# G.node[3]['step'] += 2
# G.node[4]['step'] += 1
# print(G.node[2]['step'])

        """
tree test 



    
    
    
    param: list of nodes num
    return : node with lowest stepped times 
    """


    def min_stepped_node(self, G, adj):
        if len(adj) > 0:
            arr = []
            for node in adj:
                arr.append(node[0])
            node_index = arr[random.randint(0, len(adj) - 1)]
            """min_step = 0
            node_index = 0
            for node in adj:  # init min_step
                min_step = self.stepped(G, node[0])
                node_index = node[0]
                break

            for node in adj:
                n_stepped = self.stepped(G, node[0])
                if(n_stepped < min_step):
                    min_step = n_stepped
                    node_index = node[0]"""
        return node_index





    # nx.draw_circular(G,  node_color=node_colors , node_size=10)
    # plt.show()

    # show_graph(G, 0)

    # steps_memory = []  # save all configurations of steps

    def get_print_stepped_list(self, G):
        stepped_list = []
        for node in sorted(G.nodes()):
            stepped_list.append(self.stepped(G, node))
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



    # def get_print_stepped_list(G):
    #     stepped_list = []
    #     for node in sorted(G.nodes()):
    #         stepped_list.append(stepped(G, node))
    #     # print(sorted(G.nodes()))
    #     # print('coverage steps of Graph :', stepped_list)
    #     # converting the list to string of integers
    #     string_of_int = (', '.join(str(x) for x in stepped_list))
    #     steps_memory.append(string_of_int)
    #     # write steps to csv file
    #     # time = str(datetime.datetime.now()).replace('.', '_').replace(':', '_')
    #     return stepped_list
    #
    #
    # def write_to_csv():
    #     with open('output_walks3.txt', 'a') as out:
    #         out.write("Coverage steps of Graph:")
    #         out.write('\n')
    #         for string_of_int in steps_memory:
    #             for row in string_of_int:
    #                 for col in row:
    #                     out.write('{0}'.format(col))


    #def print_edge_coverage(G):
    #    edge_list = []
    #    for edge in G.):
    #        edge_list.append(stepped(G, edge))
    #    print(sorted(G.edge()))
    #    print('coverage steps of Graph :', edge_list)
    #pos = nx.spring_layout(G)






    def csv_expo(data):
        a = numpy.asarray([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        numpy.savetxt("foo.csv", a, delimiter=",")






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


