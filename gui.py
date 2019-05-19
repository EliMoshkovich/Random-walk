from Graph_from_txt import GraphFromTxt
from drive import *
from tkinter import *
import ctypes

# This is the gui class. Here we init all the gui and start the project.
class GUI:
    def __init__(self, root, D):
        self.root = root
        root.title("Random Walk")
        root.resizable(width=False, height=False)
        menu = Menu(root)
        root.config(menu=menu)
        root.geometry("400x250+600+300")
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label='Open...', command=self.build_from_text)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        menu.add_cascade(label='File', menu=filemenu)
        helpmenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.about)

        label = Label(root, text="Choose which Graph you would like:")
        label.config(font=("Courier", 14))
        label.pack()

        l1 = Label(root, text="Nodes")
        l2 = Label(root, text="Edges")
        self.e1 = Entry(root)
        self.e2 = Entry(root)
        l1.pack(fill=X)
        self.e1.pack()
        l2.pack(fill=X)
        self.e2.pack()
        global show_graph
        show_graph = IntVar()
        c = Checkbutton(root, text="Show Graph", variable=show_graph, onvalue=1, offvalue=0)
        c.pack()
        Button(root, text='Regular Graph', command=self.build_regular).pack(fill="none", expand=True)
        Button(root, text='Random Graph', command=self.build_random).pack(fill="none", expand=True)
        Button(root, text='Tree Graph', command=self.build_tree).pack(fill="none", expand=True)

    # Here we init the random walk from our most recent graph.
    def build_from_text(self):
        parse = GraphFromTxt()
        steps = parse.run_random(show_graph.get())
        #self.Mbox('Done!', "Number of steps: " + str(steps) + "\nNumber of nodes: " + self.e1.get() + "\nThe density of the graph: " + density(parse), 1)


    # This is the about pop up.
    def about(self):
        self.Mbox('About', 'Hi and welcome to our Project!\n'
                           'In here you will find our Random Walk project and can choose in which graph you would like to run.\n'
                           'You can build a tree, a regular graph and a random graph.\n'
                            'After that just choose File-->Open and it will open your last built Graph and run random walk on it.', 1)

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def build_tree(self):
        try:
            D.update_v(int(self.e1.get()))
            D.tree_graph()
        except ValueError:
            self.Mbox('Error!', 'Please insert two integers!', 1)

    def build_regular(self):
        try:
            D.update_v(int(self.e1.get()))
            D.update_e(int(self.e2.get()))
            if D.e * D.v % 2 == 0 and D.v > D.e:
                D.regular_graph()
            elif D.e * D.v % 2 != 0:
                self.Mbox('Error!', 'In Regular Graph v * d must be even!', 1)
            elif D.v <= D.e:
                self.Mbox('Error!', 'Should be more degrees than nodes!', 1)
        except ValueError:
            self.Mbox('Error!', 'Please insert two integers!', 1)

    def build_random(self):
        try:
            D.update_v(int(self.e1.get()))
            D.update_e(int(self.e2.get()))
            D.random_graph()

        except ValueError:
            self.Mbox('Error!', 'Please insert two integers!', 1)


root = Tk()
D = Drive()
my_gui = GUI(root, D)
root.mainloop()

