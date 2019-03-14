from networkx import *

class Rw:
    def __init__(self):
        print("init Rw")

    def random_walk(self,G):
        nodes = sorted(G.nodes())
        s = nodes[0]
        print(G.adj[s])
