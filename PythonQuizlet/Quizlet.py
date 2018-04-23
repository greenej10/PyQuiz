from tkinter import *
from tkinter import messagebox

# class Question:
#     def __init__(self,prompt,options,answer,description):
#         self.prompt = prompt
#         self.options = options
#         self.answer_choice = answer
#         self.description=description
#
#     def make_questions(self,questions,options,answers,descriptions):
#         question_num = 0;
#         for question in questions:
#             question_obj[Question(self,questions[question_num],options[question_num],answers[question_num],descriptions[question_num])]
#             question_num=question_num+1


questions = [
    "Q1: Which of the following is NOT a primitive data type in Python?",
    "Q2: Which of these paradigms are supported by Python?",
    "Q3: True or False: Logical lines can be broken up by using the backslash character at the break/end of physical line.",
    "Q4: How are lists defined in Python?",
    "Q5: How do you write a comment in Python?",
    "Q6: Which of these is a structured data type in Python?",
    "Q7: Which of the following is NOT correct?",
    "Q8: True or False: Python does not need to be compiled before it is run.",
    "Q9: True or False: Variable types must be declared in Python",
    "Q10: Which of the following is correct?",
    "Q11: Which of the following is NOT true about dictionaries?",
    "Q12: How are random numbers generated in Python?",
    "Q13: Which of the following is NOT true about decorators?",
    "Q14: True or False: An integer x can be defined as: var x=10",
    "Q15: True or False: Python supports automatic garbage collection.",
    "Q16: How can you convert String s into a list?",
    "Q17: What does the pass statement do in Python?",
    "Q18: How do you capitalize the first letter of a String?",
    "Q19: How do you remove all leading whitespace from a String s?"
]

options = [
    ["Boolean", "List ", "Long", "String"],
    ["Procedure", "Object Oriented", "Functional", "All of the Above"],
    ["True", "False","",""],
    ["In square brackets with elements separated by commas", "In parentheses with elements separated by spaces", "In parentheses with elements separated by dashes", "In parentheses with elements separated by dashes"],
    ["Begin with a hash character and end at the end of the physical line", "Begin with an asterisk and end with an asterisk", "Begin with a hash character and end with a hash character", "Begin with an asterisk and end at the end of the physical line"],
    ["Integer", "Long", "List", "String"],
    ["Python was first conceived in the late 1980’s", "Python is now widely considered to be outdated and is rarely used", "Python was named after Monty Python’s Flying Circus", "Guido van Rossum is Python’s creator"],
    ["True", "False", "", ""],
    ["True", "False", "", ""],
    ["Lists are mutable and Tuples are immutable", "Lists and Tuples are mutable", "Lists and Tuples are immutable", "Lists are immutable and Tuples are mutable"],
    ["Dictionary is a datatype to define one-to-one relationships between keys and values", "Dictionaries are indexed by keys", "A dictionary cannot contain another dictionary", "Dictionaries contain a pair of keys and their corresponding values"],
    ["Random.random()", "Rand()", "Random.rand()", "Rand.rand()"],
    ["Decorators are used to modify or inject code into functions/classes", "Decorators allow you to delete code in other functions/classes", "Decorators allow you to wrap a class or function method call", "Decorators can be used to check for permissions or modify/track arguments passed to a method"],
    ["True", "False", "", ""],
    ["True", "False", "", ""],
    [" s.list()", " list(s)", "s(list)", "list.s()"],
    ["It must be used before passing arguments to a method.", "It is used when a statement is required syntactically but you do not want any command or code to execute.", "It has no function.", "It is used to pass a method into another method. "],
    ["s.cap()", "s.capitalize()", "cap()", "cap(s)"],
    ["s.whtspc()", "s.lstrip()", "lstrip(s)", "whtspc(s)"]
]

answers = [2, 4, 1, 1, 1, 3, 2, 1, 2, 1, 3, 1, 2, 1, 1, 2, 2, 2, 2]

descriptions = [
                "List is a structured data type.",
                "Procedure, Object and Functional programming is supported by Python.",
                "Long logical lines can be physically broken up for readability with the character “\”",
                "Lists are defined like so: sea_creatures = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']",
                "Comments begin with a hash character and end with the physical line. #For Example this would be commented",
                "Integer, Long and String are all Primitive data types.",
                "Python is widely used today by companies including Google, NASA and Yahoo",
                "Python has a built in compiler that compiles to byte code to be used by a virtual machine.",
                "Variable types are set when the user declares a value for the variable.  For example, “var x” has no data type until the user writes a statement like x = 10, so that x will become an Integer.",
                "Lists can be edited, and once declared, tuples cannot.",
                "Dictionaries can use other dictionaries as keys",
                "Use #include random as a header to include the Random class and call random()",
                "Decorators allow you to inject code into, but not delete from another class/function",
                "Variable types do not need to be explicitly declared in Python.",
                "Usually, the user does not need to worry about memory management when the objects are no longer needed - Python automatically reclaims the memory from them.",
                "Pass in the String as a parameter to the list() function.",
                "The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.",
                "The capitalize() function takes no arguments and is called by the String.",
                "The lstrip() function can take char parameters to specify a range of removing whitespace."
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
        self.description= Message(master, text="", width=400)
        self.description.pack()
        self.button = Button(master, text="Next Question", command=self.next_btn)
        self.button.pack(side=BOTTOM)
        self.button = Button(master, text="Check Answer", command=self.check_btn)
        self.button.pack(side=BOTTOM)


    def question_maker(self, master, question):
        prompt = Label(master, text=questions[question], width=600)
        prompt.pack(side=TOP)
        prompt.config(font=("Courier", 16), width=600)
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
        prompt.pack(side=TOP, width=700)
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
# root.geometry("800x600")
menu= Menu(root)
logo =  PhotoImage(file="python-logo.png")
title = Label(root, image=logo)
title.pack(side=TOP)
root.config(menu=menu)
app = Quizlet(root)
root.mainloop()