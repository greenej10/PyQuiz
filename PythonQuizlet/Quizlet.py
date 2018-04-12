from tkinter import *
from tkinter import messagebox

questions = [
    "Q1: What is the programming language we are using?",
    "Q2: What are the main data structures of Python?",
]

options = [
    ["Java", "Ruby ", "Python", "Perl"],
    ["Delhi", "Mumbai", "Chennai", "List"],
]

answers = [3, 4]

descriptions = [
                "We are using Python for this project.",
                "Lists are a data structure in Python"
                ]



class Quizlet:
    def __init__(self, master):

        self.answer_choice = IntVar()
        self.question_number = 0
        self.num_correct = 0
        self.question = self.question_maker(master, self.question_number)
        self.options = self.option_maker(master, 4)
        self.show_question(self.question_number)
        self.check = Message(master, text="", width=100)
        self.check.pack()
        self.description= Message(master, text="", width=200)
        self.description.pack()
        self.button = Button(master, text="Check Answer", command=self.check_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Next Question", command=self.next_btn)
        self.button.pack(side=BOTTOM)

    def question_maker(self, master, question):
        prompt = Label(master, text=questions[question])
        prompt.pack(side=TOP)
        prompt.config(font=("Courier", 16))
        return prompt

    def option_maker(self, master, n):
        button_value = 0
        button_list = []
        while button_value < n:
            button = Radiobutton(master, text="", variable=self.answer_choice, value=button_value + 1)
            button_list.append(button)
            button.pack(side=TOP, anchor="w")
            button_value = button_value + 1
        return button_list


    def answer_maker(self, master, answer, description):
        prompt = Label(master, text=answers[answer])
        prompt.pack(side=TOP)
        prompt.config(font=("Courier", 16))
        description= Message(master, text= descriptions[description])
        description.pack()
        description.config(font=("Courier",12))
        return prompt

    def description_maker(self, master):
        self.description.config(text = descriptions[self.question_number], font=("Courier",12))


    def show_question(self, question):
        self.question['text'] = questions[question]
        for option in options[question]:
            self.options[button_value]['text'] = option
            button_value = button_value + 1

    def show_question(self, question):
        button_value = 0
        self.answer_choice.set(0)
        self.question['text'] = questions[question]
        for option in options[question]:
            self.options[button_value]['text'] = option
            button_value = button_value + 1

    def answer_check(self, question):
        if self.answer_choice.get() == answers[question]:
            return True
        return False

    def print_results(self):
        messagebox.showinfo("Score: ", "You got : " + str(self.num_correct) + "/" + str(len(questions)))
    def check_btn(self):
        if self.answer_check(self.question_number):
            self.check.config(text="CORRECT!")
        else:
            self.check.config(text="INCORRECT!")
        self.description_maker(root)

    def next_btn(self):
        if self.answer_check(self.question_number):
            print("Correct")
            self.num_correct += 1
            self.description.config(text="")
            self.check.config(text="")
        else:
            self.description.config(text="")
            self.check.config(text="")
            print("Wrong")
        self.question_number = self.question_number + 1
        if self.question_number >= len(questions):
            self.print_results()
            quit()
        else:
            self.show_question(self.question_number)


root = Tk()
root.geometry("800x600")
menu= Menu(root)
logo =  PhotoImage(file="python-logo.png")
title = Label(root, image=logo)
title.pack(side=TOP)
root.config(menu=menu)
app = Quizlet(root)
root.mainloop()