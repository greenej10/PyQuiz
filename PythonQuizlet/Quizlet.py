from tkinter import *
# keep the question in a separate json file
questions = [
    "Q1: What is the programming language we are using?",
    "Q2: What are the main data structures of Python?",
]

options = [
    ["Java", "Ruby ", "Python", "Chennai"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
]

a = [1, 4]

class Quizlet:
    def __init__(self, master):
        self.opt_selected = IntVar()
        self.qn = 0
        self.correct = 0
        self.ques = self.create_q(master, self.qn)
        self.opts = self.create_options(master, 4)
        self.display_q(self.qn)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def create_q(self, master, qn):
        w = Label(master, text=questions[qn])
        w.pack(side=TOP)
        return w

    def create_options(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.opt_selected, value=b_val+1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def display_q(self, qn):
        b_val = 0
        self.opt_selected.set(0)
        self.ques['text'] = questions[qn]
        for op in options[qn]:
            self.opts[b_val]['text'] = op
            b_val = b_val + 1

    def check_q(self, qn):
        if self.opt_selected.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.correct, "/", len(questions))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.qn):
            print("Correct")
            self.correct += 1
        else:
            print("Wrong")
        self.qn = self.qn + 1
        if self.qn >= len(questions):
            self.print_results()
        else:
            self.display_q(self.qn)


root = Tk()
root.geometry("800x800")
menu= Menu(root)
logo =  PhotoImage(file="python-logo.png")
title = Label(root, image=logo)
title.pack(side=TOP)
root.config(menu=menu)
app = Quizlet(root)
root.mainloop()