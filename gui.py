from drive import *


# class Gui:
#     D = Drive()

#     label1 = Label(top, text="Choose which Graph you would like:")
#     randomButton = Button(frame, text="Random Graph", command=D.randomGraph())
#     regularButton = Button(frame, text="Regular Graph", command=D.regularGraph())
#     treeButton = Button(frame, text="Tree Graph", command=D.treeGraph)
#
#     label1.pack()
#     randomButton.pack(side=LEFT)
#     regularButton.pack(side=LEFT)
#     treeButton.pack(side=LEFT)
#     frame.pack()
#     top.mainloop()
#
#
# g = Gui()

# from tkinter import Tk, Label, Button
# D = Drive()
#
#
# class MyFirstGUI:
#     def __init__(self, master):
#         self.master = master
#         master.title("A simple GUI")
#         frame = Frame(master)
#         self.label1 = Label(master, text="Choose which Graph you would like:")
#         self.randomButton = Button(frame, text="Random Graph", command=D.randomGraph(self))
#         self.regularButton = Button(frame, text="Regular Graph", command=D.regularGraph())
#         self.treeButton = Button(frame, text="Tree Graph", command=D.treeGraph)
#         self.label1.pack()
#         self.randomButton.pack(side=LEFT)
#         self.regularButton.pack(side=LEFT)
#         self.treeButton.pack(side=LEFT)
#         frame.pack()
#
#
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

from tkinter import Tk, Label, Button



class MyFirstGUI:
    def __init__(self, master, D):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="Choose which Graph you would like:")
        self.label.pack()

        self.randomButton = Button(master, text="Random Graph", command=D.random_graph)
        self.randomButton.pack(side=LEFT)

        self.regularButton = Button(master, text="Regular Graph", command=D.regular_graph)
        self.regularButton.pack(side=LEFT)

        self.treeButton = Button(master, text="Tree Graph", command=D.tree_graph)
        self.treeButton.pack(side=LEFT)


root = Tk()
D = Drive()
my_gui = MyFirstGUI(root, D)
root.mainloop()

