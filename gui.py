from drive import *
from tkinter import *
from tkinter import ttk
import ctypes


class GUI:
    def __init__(self, root, D):

        self.root = root
        root.title("Random Walk")

        menu = Menu(root)
        root.config(menu=menu)
        root.geometry("400x150+30+30")
        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label='Open...')
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        menu.add_cascade(label='File', menu=filemenu)
        helpmenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.about)

        label = Label(root, text="Choose which Graph you would like:")
        label.config(font=("Courier", 14))
        label.pack()

        l1 = Label(root, text="Vertices")
        l2 = Label(root, text="Edges / Degrees")
        self.e1 = Entry(root)
        self.e2 = Entry(root)
        l1.pack(fill=X)
        self.e1.pack()
        l2.pack(fill=X)
        self.e2.pack()

        v = IntVar(0)
        Radiobutton(root, text='Regular Graph', command=self.build_regular, variable=v, value=1, indicatoron=False).pack(side=LEFT, padx=20)
        Radiobutton(root, text="Random Graph", command=self.build_random, variable=v, value=2, indicatoron=False).pack(side=LEFT, padx=20)
        Radiobutton(root, text="Tree Graph", command=self.build_tree, variable=v, value=3, indicatoron=False).pack(side=LEFT, padx=20)




        #ttk.Button(root, text="Submit", command=self.build_regular, ).pack()#grid(row=6)

    def about(self):
        self.Mbox('About', 'Need to write something here', 1)

    def Mbox(self, title, text, style):
        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

    def p(self):
            print(self.textBox.get(1))

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

