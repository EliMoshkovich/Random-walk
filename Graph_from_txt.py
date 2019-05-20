import ctypes
import math
import threading
import xlrd as xlrd
from networkx import *
import random
from ShowGraph import ShowGraph
import sys
from xlutils.copy import copy


# This class is for the random walk on the given graph.
class GraphFromTxt:
    # This function initializes the graph we saved before.
    def __init__(self):
        self.GraphStan = []
        file = open("output_graph.txt", "r")
        for line in file:
            self.GraphStan.append(line)
        self.G = GraphFromTxt.parse(self)
        self.show = ShowGraph(self.G)
        self.G_edges = sorted(self.G.edges())
        self.stepped_edges = [0] * len(self.G_edges)
        self.stepped_edges_remember = []

    # How much are stepped.
    def stepped(self, G, node_index):
        return G.node[node_index]['step']

    # Print the edges.
    def print_edges(self, G):
        print(G.edges())

    # Parse the graph.
    def parse(self):
        return nx.parse_edgelist(self.GraphStan, nodetype=int)

    # Get the index out of the graph.
    def get_index_of_edge(self, node1, node2):
        for i in range(len(self.G_edges)):
            edge = self.G_edges[i]
            if edge[0] == node1 and edge[1] == node2:
                return i

            elif edge[1] == node1 and edge[0] == node2:
                return i

        return -1

    # Get the list stepped.
    def get_steeped_node_list(self):
        stepped_node_list = []
        nodes = sorted(self.G.nodes)

        for node in nodes:
            stepped_node_list.append(self.G.node[node]['step'])

        return stepped_node_list

    # Check if the graph is already covered.
    def is_covered(self, G):
        nodes = sorted(G.nodes())
        for node in nodes:
            if self.stepped(G, node) == 0:
                return False
        return True

    # This is the main function of the random walk, runs recursively.
    def random_walk(self, G, s, count_steps, show_graph):
        if not self.is_covered(G):
            mod = int(math.sqrt(len(G.nodes())))
            # print(int(mod))
            adj_n = G.adj[s].items()
            next_node = self.min_stepped_node(G, adj_n)
            G.node[next_node]['step'] += 1
            self.show.to_blue(next_node)
            # show the graph
            if show_graph == 1:
                if count_steps % mod == 1:
                    try:
                        showG = self.show.show_graph
                        showG(G, next_node)
                    except:
                        print(" ")
            count_steps = count_steps + 1
            #self.get_print_stepped_list(G)  # write steppes nodes to csv
            index = self.get_index_of_edge(s, next_node)
            self.stepped_edges[index] += 1
            self.stepped_edges_remember.append(self.stepped_edges)
            self.edges_to_csv2(self.stepped_edges)
            self.random_walk(G, next_node, count_steps, show_graph)
        else:
            global counter
            counter = count_steps
            #self.get_print_stepped_list(G)  # write steppes nodes to csv

    # This function prints to a csv the number of steps for each edge.
    def edges_to_csv(self):
        # print((self.stepped_edges_remember))
        self.G_edges
        with open('csvfile2.txt', 'w') as file:
            #file.write("aaaaa")
            print("edges_to_csv")
            print(self.stepped_edges_remember)
            for line in self.stepped_edges_remember:
                file.write(line)
                file.write('\n')

    # This function prints to a csv the number of steps for each edge.
    def edges_to_csv2(self, row):
        # print((self.stepped_edges_remember))
        self.G_edges
        with open('csvfile2.txt', 'a') as file:
                file.write(str(row))
                file.write('\n')

    # This is the function to control the random walk with a new thread.
    def run_random(self, show_graph):
        nx.set_node_attributes(self.G, 0, 'step')
        nodes = sorted(self.G.nodes())
        s = nodes[0]
        # print(self.G.node[s])
        self.G.node[s]['step'] += 1
        sys.setrecursionlimit(10000) # https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object
        t = threading.Thread(target=self.random_walk, args=(self.G, 0, 1, show_graph))
        t.start()
        t.join()
        self.Mbox('Done!', "Number of steps: " + str(counter) + "\nNumber of nodes: " + str(len(nodes)) + "\nThe density of the graph: " + str(density(self.G)), 1)
        return counter
        # write_to_csv()

    # The pop up function.
    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    # Check the next node from a given node randomly.
    def min_stepped_node(self, G, adj):
        if len(adj) > 0:
            arr = []
            for node in adj:
                arr.append(node[0])
            node_index = arr[random.randint(0, len(adj) - 1)]
        return node_index

    # This function prints to a csv how many steps it made according to number of nodes.
    def get_steps_to_nodes(self, G):
        global counter
        rb = xlrd.open_workbook('steps_to_nodes.xls', formatting_info=True)
        sheet = rb.sheet_by_index(0)
        wb = copy(rb)
        sh = wb.get_sheet(0)
        sh.write(sheet.nrows, 0, len(G.nodes))
        sh.write(sheet.nrows, 1, counter)
        wb.save('steps_to_nodes.xls')

    # Not needed function for now.
    #def get_print_stepped_list(self, G):
    #    stepped_list = []
    #    for node in sorted(G.nodes()):
    #        stepped_list.append(self.stepped(G, node))
    #    # converting the list to string of integers
    #    string_of_int = (', '.join(str(x) for x in stepped_list))

        # write steps to csv file
    #    with open('output_walks2.txt', 'a') as out:
    #        out.write('\n')
            # text = "Coverage steps of Graph:"
            # out.write(text)
    #        out.write('\n')
    #        for row in string_of_int:
    #            for col in row:
    #                out.write('{0}'.format(col))
    #    return stepped_list
