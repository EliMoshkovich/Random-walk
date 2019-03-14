from drive import *
from tkinter import *

# if num_of_line < 6594982:
class GUI:
    def __init__(self, root, D):
        self.root = root
        root.title("A simple GUI")

        self.label = Label(root, text="Choose which Graph you would like:")
        self.label.pack()

        self.randomButton = Button(root, text="Random Graph", command=self.build_random)
        self.randomButton.pack(side=LEFT)

        self.regularButton = Button(root, text="Regular Graph", command=self.build_regular)
        self.regularButton.pack(side=LEFT)

        self.treeButton = Button(root, text="Tree Graph", command=self.build_tree)
        self.treeButton.pack(side=LEFT)

        self.textBox_v = Text(root, height=2, width=10)
        self.textBox_v.pack(side=LEFT)
        self.textBox_v.insert('1.0', "vertics", "vertics")

        self.textBox_e = Text(root, height=2, width=15)
        self.textBox_e.pack(side=LEFT)
        self.textBox_e.insert('1.0', "edges \ degree", "edges")

        self.textBox_msg = Text(root, height=2, width=22)
        self.textBox_msg.pack(side=LEFT)
        self.textBox_msg.insert('1.0', "msg to user if needed", "edges")

        print(type(self.label))
        print(type(self.randomButton))
        print(self.root)


    def p(self):
            print(self.textBox.get(1))

    def build_tree(self):
        try:
            D.update_v(int(self.textBox_v.get("1.0", "end-1c")))
            D.tree_graph()
        except ValueError:
            self.textBox_msg.delete('1.0', END)
            self.textBox_msg.insert('1.0', "pls insert 2 integers", "edges")

    def build_regular(self):
        try:
            D.update_v(int(self.textBox_v.get("1.0", "end-1c")))
            D.update_e(int(self.textBox_e.get("1.0", "end-1c")))
            if D.e * D.v % 2 == 0 and D.v > D.e:
                D.regular_graph()
            elif D.e * D.v % 2 != 0:
                print("v * e must be even")
                self.textBox_msg.delete('1.0', END)
                self.textBox_msg.insert('1.0', "in regular Graph v * d must be even", "edges")
            elif D.v <= D.e:
                print("should be more degrees than nodes")
                self.textBox_msg.delete('1.0', END)
                self.textBox_msg.insert('1.0', "should be more degrees than nodes", "edges")
        except ValueError:
            self.textBox_msg.delete('1.0', END)
            self.textBox_msg.insert('1.0', "pls insert 2 integers", "edges")

    def build_random(self):
        try:
            D.update_v(int(self.textBox_v.get("1.0", "end-1c")))
            D.update_e(int(self.textBox_e.get("1.0", "end-1c")))
            D.random_graph()
        except ValueError:
            self.textBox_msg.delete('1.0', END)
            self.textBox_msg.insert('1.0', "pls insert 2 integers", "edges")


root = Tk()
D = Drive()
my_gui = GUI(root, D)
root.mainloop()

