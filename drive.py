# from gui import *

from networkx import *
import matplotlib.pyplot as plt


class Drive:
    v = 10
    e = 10

    def __init__(self):
        print("init")

    def regular_graph(self):
        draw(random_regular_graph(self.e, self.v))
        plt.show()

    def tree_graph(self):
        draw(random_tree(self.v))
        plt.show()

    def random_graph(self):
        draw(gnm_random_graph(self.v, self.e))
        plt.show()

    def update_v(self, v_input):
        self.v = v_input

    def update_e(self, e_input):
        self.e = e_input


# a = Drive()
# print(a.v)
# a.update_v(14)
# print(a.v)



