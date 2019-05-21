from networkx import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


# This class is for showing the graph we saved with networkx.
class ShowGraph:
    # This function initializes the graph.
    def __init__(self, G):
        self.node_blue_colors = []
        self.node_red_colors = []
        self.node_green_color = []
        self.pos = nx.spring_layout(G)  # positions for all nodes

        for i in range(0, len(G.nodes())):
            if i < 1:
                self.node_blue_colors.append(i)
            else:
                self.node_red_colors.append(i)

    # This function draws the graph with networkx and reloads every 2 seceonds.
    # Blue - Not yet stepped.
    # Green - Current node.
    # Red - Stepped node.
    def show_graph(self, G, current_node):
        nx.draw(G, self.pos, nodelist=self.node_blue_colors, node_color='r', node_size=250, alpha=0.8, with_labels=True)
        nx.draw(G, self.pos, nodelist=self.node_red_colors, node_color='b', node_size=250, alpha=0.8, with_labels=True)
        nx.draw(G, self.pos, nodelist=[current_node], node_color='g', node_size=250, alpha=0.8, with_labels=True)

        plt.title("Random Walk")
        plt.show(block=False)
        plt.savefig('random_walk_2d.png', dpi=250)
        plt.pause(2)
        plt.close()
        # node_colors[next_node] = 'b'

    # Change the color to red.
    def to_red(self, n):
        if n in self.node_blue_colors:
            self.node_blue_colors.remove(n)
            self.node_red_colors.append(n)

    # Change the color to blue.
    def to_blue(self, n):
        if n in self.node_red_colors:
            self.node_red_colors.remove(n)
            self.node_blue_colors.append(n)

