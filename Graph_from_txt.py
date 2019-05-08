import ctypes
import math
import threading
import xlrd as xlrd
from networkx import *
import numpy
import random
from ShowGraph import ShowGraph
import sys
from xlutils.copy import copy


class GraphFromTxt:

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

    def stepped(self, G, node_index):
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
            if edge[0] == node1 and edge[1] == node2:
                return i

            elif edge[1] == node1 and edge[0] == node2:
                return i

        return -1

    def get_steeped_node_list(self):
        stepped_node_list = []
        nodes = sorted(self.G.nodes)

        for node in nodes:
            stepped_node_list.append(self.G.node[node]['step'])

        return stepped_node_list

    def is_covered(self, G):
        nodes = sorted(G.nodes())
        for node in nodes:
            if self.stepped(G, node) == 0:
                return False
        return True

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
                # showG(G, next_node)
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

    def edges_to_csv2(self, row):
        # print((self.stepped_edges_remember))
        self.G_edges
        with open('csvfile2.txt', 'a') as file:
                file.write(str(row))
                file.write('\n')

    def run_random(self, show_graph):
        """
        add field of stepped node to each node in graph.
        https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.classes.function.set_node_attributes.html
        """
        nx.set_node_attributes(self.G, 0, 'step')
        # print(sorted(self.G.nodes))
        nodes = sorted(self.G.nodes())
        s = nodes[0]
        # print(self.G.node[s])
        self.G.node[s]['step'] += 1
        #print(self.G_edges)
        self.edges_to_csv()
        # ShowGraph.show_graph(G, 0)
        sys.setrecursionlimit(10000) # https://stackoverflow.com/questions/6809402/python-maximum-recursion-depth-exceeded-while-calling-a-python-object
        #thread.start_new_thread(self.random_walk, (self.G, 0, 1, ))
        t = threading.Thread(target=self.random_walk, args=(self.G, 0, 1, show_graph))
        t.start()
        t.join()
        self.get_steps_to_nodes(self.G)
        print("the end")
        #self.Mbox('Conclusion', 'The number of steps is:' + str(counter), 1)
        # self.random_walk(self.G, 0, 1)
        # write_to_csv()
        # pos = nx.spring_layout(self.G)  # positions for all nodes

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def min_stepped_node(self, G, adj):
        if len(adj) > 0:
            arr = []
            for node in adj:
                arr.append(node[0])
            node_index = arr[random.randint(0, len(adj) - 1)]
        return node_index

    def get_steps_to_nodes(self, G):
        #book = xlwt.Workbook()
        #sh = book.add_sheet("Sheet 1")
        global counter
        rb = xlrd.open_workbook('steps_to_nodes.xls', formatting_info=True)
        sheet = rb.sheet_by_index(0)
        wb = copy(rb)
        sh = wb.get_sheet(0)
        sh.write(sheet.nrows, 0, len(G.nodes))
        sh.write(sheet.nrows, 1, counter)
        #book.save("steps_to_nodes.xls")
        wb.save('steps_to_nodes.xls')
        #with open('steps_to_nodes.txt', 'a') as out:
        #    #out.write('\n')
        #   out.write('{0},{1}'.format(len(G.nodes), counter))
        #    out.write('\n')

    def get_print_stepped_list(self, G):
        stepped_list = []
        for node in sorted(G.nodes()):
            stepped_list.append(self.stepped(G, node))
        # converting the list to string of integers
        string_of_int = (', '.join(str(x) for x in stepped_list))

        # write steps to csv file
        with open('output_walks2.txt', 'a') as out:
            out.write('\n')
            # text = "Coverage steps of Graph:"
            # out.write(text)
            out.write('\n')
            for row in string_of_int:
                for col in row:
                    out.write('{0}'.format(col))
        return stepped_list


## https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.classes.function.density.html