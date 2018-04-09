# from tkinter import*
# from Question import Question
#
# class newClass:
#
#     def __init__ (self, master):
#         frame = Frame(master)
#         run_quiz(questions)
#         frame.pack()
#
#         score = 0
#         prompts = [["Q1: What Programming Language Did We Use?"]]
#         options = [["Python", "Java", "Ruby", "Perl"]]
#         answers = ["Python"]
#         questions = []
#
#         i = 0
#
#         while i < len(prompts) - 1:
#             questions.append(Question(prompts[i], options[i], answers[i]))
#             i + 1
#
#
#
#         #
#         # answer1="Python"
#         # answer2= "Java"
#         # answer3="Ruby"
#         # answer4="Perl"
#         # self.printButton = Button(frame,text = "A) " + answer1)
#         # self.printButton.pack(side=LEFT)
#         # self.printButton = Button(frame, text="B) " + answer2)
#         # self.printButton.pack(side=LEFT)
#         # self.printButton = Button(frame, text="C) " + answer3)
#         # self.printButton.pack(side=LEFT)
#         # self.quitButton = Button(frame, text="D) " + answer4)
#         # self.quitButton.pack(side=LEFT)
#
#
#     def run_quiz(questions):
#         for question in questions:
#             prompt = Label(text=question.prompt)
#             prompt.pack(side=TOP)
#             answer1 = Button(text="A) " + str(question.options[0]))
#             answer1.pack(side=LEFT)
#             answer2 = Button(text="B) " + str(question.options[1]))
#             answer2.pack(side=LEFT)
#             answer3 = Button(text="C) " + str(question.options[2]))
#             answer3.pack(side=LEFT)
#             answer4 = Button(root, text="D) " + str(question.options[3]))
#             answer4.pack(side=LEFT)
#
#     # def check_answer(choice, answer, info):
#     #     if(choice == answer):
#     #         correctMessage= Message(text="Correct")
#     #     else:
#     #         incorrectMessage = Message(text="Incorrect")
#
#
#
#
# root=Tk()
# menu= Menu(root)
# logo =  PhotoImage(file="python-logo.png")
# title = Label(root, image=logo)
# title.pack(side=TOP)
# quiz = newClass(root)
# root.config(menu=menu)
# subMenu=Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="Option1")
# root.mainloop()