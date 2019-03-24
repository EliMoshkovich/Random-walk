from drive import *
from tkinter import *
import ctypes


class GUI:
    def __init__(self, root, D):

        self.root = root
        root.title("Random Walk")

        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        menu.add_cascade(label='File', menu=filemenu)
        helpmenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')

        self.label = Label(root, text="Choose which Graph you would like:")
        self.label.config(font=("Courier", 14))
        self.label.grid(row=0, column=0)

        v = IntVar()
        Radiobutton(root, text='Regular Graph', command=self.build_regular, variable=v, value=1).grid(row=1)#.pack(anchor=W)
        Radiobutton(root, text="Random Graph", command=self.build_random, variable=v, value=2).grid(row=2)#.pack(anchor=W)
        Radiobutton(root, text="Tree Graph", command=self.build_tree, variable=v, value=3).grid(row=3)#.pack(anchor=W)

        #self.randomButton = Button(root, text="Random Graph", command=self.build_random)
        #self.randomButton.pack(side=LEFT)

        #self.regularButton = Button(root, text="Regular Graph", command=self.build_regular)
        #self.regularButton.pack(side=LEFT)

        #self.treeButton = Button(root, text="Tree Graph", command=self.build_tree)
        #self.treeButton.pack(side=LEFT)

        Label(root, text="Vertices").grid(row=4)
        Label(root, text="Edges / Degrees").grid(row=5)

        self.e1 = Entry(root)
        self.e2 = Entry(root)

        self.e1.grid(row=4, column=1)
        self.e2.grid(row=5, column=1)

        #self.textBox_msg = Text(root, height=2, width=22)
        #self.textBox_msg.grid(row=6, column=0)#.pack(side=LEFT)
        #self.textBox_msg.insert('1.0', "msg to user if needed", "edges")


    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def p(self):
            print(self.textBox.get(1))

    def build_tree(self):
        try:
            D.update_v(int(self.e1.get())) #self.textBox_v.get("1.0", "end-1c")))
            D.tree_graph()
        except ValueError:
            self.Mbox('Error!', 'Please insert two integers!', 1)
            #self.textBox_msg.delete('1.0', END)
            #self.textBox_msg.insert('1.0', "pls insert 2 integers", "edges")

    def build_regular(self):
        try:
            D.update_v(int(self.e1.get())) #self.textBox_v.get("1.0", "end-1c")))
            D.update_e(int(self.e2.get())) #self.textBox_e.get("1.0", "end-1c")))
            if D.e * D.v % 2 == 0 and D.v > D.e:
                D.regular_graph()
            elif D.e * D.v % 2 != 0:
                self.Mbox('Error!', 'In Regular Graph v * d must be even!', 1)
                #self.textBox_msg.delete('1.0', END)
                #self.textBox_msg.insert('1.0', "in regular Graph v * d must be even", "edges")
            elif D.v <= D.e:
                self.Mbox('Error!', 'Should be more degrees than nodes!', 1)
                #self.textBox_msg.delete('1.0', END)
                #self.textBox_msg.insert('1.0', "should be more degrees than nodes", "edges")
        except ValueError:
            self.Mbox('Error!', 'Please insert two integers!', 1)
            #self.textBox_msg.delete('1.0', END)
            #self.textBox_msg.insert('1.0', "pls insert 2 integers", "edges")

    def build_random(self):
        try:
            D.update_v(int(self.e1.get())) #self.textBox_v.get("1.0", "end-1c")))
            D.update_e(int(self.e2.get())) #self.textBox_e.get("1.0", "end-1c")))
            D.random_graph()

        except ValueError:
            self.Mbox('Error!', 'Please insert two integers!', 1)
            #self.textBox_msg.delete('1.0', END)
            #self.textBox_msg.insert('1.0', "pls insert 2 integers", "edges")


root = Tk()
D = Drive()
my_gui = GUI(root, D)
root.mainloop()

