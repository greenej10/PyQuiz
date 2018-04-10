from tkinter import *
# keep the question in a separate json file
questions = [
    "Q1: What is the programming language we are using?",
    "Q2: What are the main data structures of Python?",
]

options = [
    ["Java", "Ruby ", "Python", "Perl"],
    ["Delhi", "Mumbai", "Chennai", "Kanyakumari"],
]

a = [3, 4]

class Quizlet:
    def __init__(self, master):
        self.answer_choice = IntVar()
        self.question_number = 0
        self.num_correct = 0
        self.question = self.question_maker(master, self.question_number)
        self.options = self.option_maker(master, 4)
        self.show_question(self.question_number)
        self.button = Button(master, text="Back", command=self.back_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def question_maker(self, master, question):
        prompt = Label(master, text=questions[question])
        prompt.pack(side=TOP)
        prompt.config(font=("Courier", 16))
        return prompt

    def option_maker(self, master, n):
        b_val = 0
        b = []
        while b_val < n:
            btn = Radiobutton(master, text="foo", variable=self.answer_choice, value=b_val + 1)
            b.append(btn)
            btn.pack(side=TOP, anchor="w")
            b_val = b_val + 1
        return b

    def show_question(self, question):
        b_val = 0
        self.answer_choice.set(0)
        self.question['text'] = questions[question]
        for option in options[question]:
            self.options[b_val]['text'] = option
            b_val = b_val + 1

    def check_q(self, qn):
        if self.answer_choice.get() == a[qn]:
            return True
        return False

    def print_results(self):
        print("Score: ", self.num_correct, "/", len(questions))

    def back_btn(self):
        print("go back")

    def next_btn(self):
        if self.check_q(self.question_number):
            print("Correct")
            self.num_correct += 1
        else:
            print("Wrong")
        self.question_number = self.question_number + 1
        if self.question_number >= len(questions):
            self.print_results()
        else:
            self.show_question(self.question_number)


root = Tk()
root.geometry("800x800")
menu= Menu(root)
logo =  PhotoImage(file="python-logo.png")
title = Label(root, image=logo)
title.pack(side=TOP)
root.config(menu=menu)
app = Quizlet(root)
root.mainloop()