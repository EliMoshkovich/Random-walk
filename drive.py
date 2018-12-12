from tkinter import *
from networkx import *
import matplotlib.pyplot as plt
#roy tesr

def randomGraph():
    draw(gnm_random_graph(10, 20))
    plt.show()


def regularGraph():
    draw(random_regular_graph(4, 10))
    plt.show()


def treeGraph():
    draw(random_tree(10))
    plt.show()


top = Tk()
frame = Frame(top)
label1 = Label(top, text="Choose which Graph you would like:")
randomButton = Button(frame, text="Random Graph", command=randomGraph)
regularButton = Button(frame, text="Regular Graph", command=regularGraph)
treeButton = Button(frame, text="Tree Graph", command=treeGraph)

label1.pack()
randomButton.pack(side=LEFT)
regularButton.pack(side=LEFT)
treeButton.pack(side=LEFT)
frame.pack()
top.mainloop()
