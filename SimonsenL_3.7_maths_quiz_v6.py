"""
Game made to support year 9s in learning maths.
Made for 13CSI_2024

Use the command line arg -O when running
"""
# Created 27/03/24

from os import getcwd
import tkinter as tk
from tkinter import messagebox
import json

"""
COMPANY, LOGO, AND CWD are all constant.
CWD represents the current working directory,
allows the program to run on Windows, GNU/Unix & macOS
"""
__version__ = "0.6"
__author__ = "Logan Simonsen"
COMPANY: str = "13CSI_2024"
LOGO: str = "icon.gif"
CWD = getcwd()
JSON_DATA_FILE = "data.json"

current_question: int = 0
username: str = ""
data, difficulties = [],[]

def gather_data(source=JSON_DATA_FILE):
    global data, difficulties
    # Get the data for the questions
    with open(source, "r") as file:
        data = json.load(file)
    if __debug__:
        print(data)

    difficulties = []
    for i in data:
        difficulties.append(i)

gather_data()
if __debug__:
    print()
    print(difficulties)


def main():
    """Control the main canvas."""
    root = tk.Tk()
    x_canvas, y_canvas = root.winfo_width(), root.winfo_height()
    if __debug__:
        print(x_canvas, y_canvas)
    root.title(f"Math game for {COMPANY}")
    # Sets the app icon to be the tawa college emblem
    root.iconphoto(False, tk.PhotoImage(
        file=fr"{CWD}/{LOGO}"))
    root.geometry(f"{x_canvas}x{y_canvas}")
    div = tk.Canvas(root, width=x_canvas, height=y_canvas)  # Used exclusively by the level select
    div.pack()

    def copyright():
        messagebox.showinfo("Info", f"© {__author__} 2024. \n Made on behalf of {COMPANY}")

    def about():
        messagebox.showinfo("Info", f"Version: {__version__} \n See latest patchnotes via readme.md as either raw text or in your favourite markdown viewer")

    def tutorial():
        messagebox.showerror("Help", "Uhhh, you caught me, this hasnt been updated")
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Copyright", command=copyright)
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="Tutorial", command=tutorial)
    menubar.add_cascade(label="Help", menu=helpmenu)

    def clear_div():
        for child in div.winfo_children():
            child.destroy()
        div.update()

    def leave():
        """Kill the window."""
        root.destroy()


    def level(hardness, index):
        clear_div()
        question_set = data[hardness]  # Hardness bc data is a dict

        def show_results():
            clear_div()
            lable = tk.Label(div, text=f"Excellent Job, {username}! \n You've completed the quiz!")
            lable.pack()
            incorrect_answers = 0
            for i, questions in enumerate(question_set):  #question_set[i]
                try:
                    lable = tk.Label(div, text=f"Question: {question_set[i][0]} Correct answer was: {question_set[i][1]} (You entered: {question_set[i][2]})").pack()
                    incorrect_answers += 1
                except IndexError:
                    lable = tk.Label(div, text=f"Question: {question_set[i][0]} Correct answer was: {question_set[i][1]}").pack()
            total_answers, correct_answers = len(question_set), len(question_set) - incorrect_answers
            lable = tk.Label(div, text=f"You got {correct_answers} right of {total_answers}. This means you got a score of {int((correct_answers/total_answers) * 100)}%").pack()
            button = tk.Button(div, text="Start Again?", command=lambda: [leave(), main()])
            button.pack()
            button = tk.Button(root, text="Quit", command=leave)
            button.pack()

        def compair_answers():
            global current_question
            answer = entry.get().strip()
            correct_answer = question_set[current_question][1]
            if __debug__:
                print(f"User: {answer}, Correct: {correct_answer}")
            clear_div()
            result = str(answer) == str(correct_answer)
            if result == 0:
                question_set[current_question].append(answer)
                if __debug__:
                    print(question_set)
            # Do something with results
            lable = tk.Label(div, text=result)
            lable.pack()
            button = tk.Button(div, text="Next?", command=lambda: level(hardness, index))
            button.pack()
            current_question += 1  # Increment after setting answers


        if __debug__:
            print(index)
            print(question_set)
            # iterate throught all questions for debuging
            for questions in question_set:  # Numeric index bc nested list
                print(f"Question: {questions[0]}, Answer: {questions[1]}")
        # will need to add a try: except for index error, go to result screen
        try:
            lable = tk.Label(div, text=question_set[current_question][0])
            lable.pack()
            entry = tk.Entry(div)
            entry.pack()
            sumbit = tk.Button(div, text="Submit Answer", command=compair_answers)
            sumbit.pack()
            div.update()
        except IndexError:
            assert "Slightly intented, easiest way to find end of list"
            show_results()



    def level_select():
        for i, options in enumerate(difficulties):  # i refers to the index
            options = tk.Button(div, text=options.title(),  command=lambda i=i, hardness=options: level(hardness, i))
            if __debug__:
                print(f"options:{options}, i:{i}")
            options.pack()

    def getusername():

        def check_name():
            global username  # Use the global scope else incorrect assignment
            current_question: int = 0  # Placed out of the way
            value = box.get().strip().title().replace("-", "")
            if value.isalpha() and 2 < len(value) < 15:
                username = value
                if __debug__:
                    print(box.get())
                    print(f"{username =}")
            else:
                messagebox.showerror("Non-fatal Error!", "Please make sure your name is bewteen 2 and 15 chars and only includes latin charaters")
            if username != "":
                label.destroy()
                box.destroy()
                submit.destroy()
                level_select()

        label = tk.Label(root, text="Please enter your name")
        label.place(relx=0.45, rely=0.25, relwidth=0.1)
        # User input handling
        box = tk.Entry(root)
        box.place(relx=0.45, rely=0.3, relwidth=0.1)

        submit = tk.Button(root, text="Submit Name", command=lambda: check_name())
        submit.place(relx=0.45, rely=0.5, relwidth=0.1)

    clear_div()
    root.state("zoomed")
    end = tk.Button(root, text="Quit", command=leave)
    end.place(relx=0.95, rely=0.95)
    getusername()
    root.mainloop()


if __name__ == "__main__":
    main()
