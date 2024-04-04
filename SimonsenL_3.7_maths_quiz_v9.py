"""
Game made to support year 9s in learning maths.

Made for 13CSI_2024
Use the command line arg -0 when running
"""
# Created 3/04/24

from os import getcwd
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import json_maker

"""
COMPANY, LOGO, AND CWD are all constant.
CWD represents the current working directory,
allows the program to run on Windows, GNU/Unix & macOS
"""
__version__ = "0.9"
__author__ = "Logan Simonsen"
COMPANY: str = "13CSI_2024"
LOGO: str = "icon.gif"
CWD = getcwd()
DEFAULT_JSON_FILE = "data.json"

source_file = DEFAULT_JSON_FILE
username: str = ""
data, difficulties = [], []
font = ("Arial", 16)

tutorial_text = """
You need to enter a valid username, choose a difficulty, and then answer each
 question.\n\n\
You will then be shown a results screen with your provided answers if
 incorrect.\n\n\
You will then have the option to quit or start again from the begining.
"""


def gather_data(source):
    """Get data from specificed JSON file."""
    global data, difficulties
    # Get the data for the questions
    with open(source, "r") as file:
        data = json.load(file)
    if __debug__ == False:
        print(data)

    difficulties = []
    for i in data:
        difficulties.append(i)


def main():
    """Control the main canvas."""
    root = tk.Tk()
    # ttk.Label.configure(font=font)
    x_canvas, y_canvas = root.winfo_width(), root.winfo_height()
    if __debug__ == False:
        print(x_canvas, y_canvas)
    root.title(f"Math game for {COMPANY}")
    # Sets the app icon to be the tawa college emblem
    root.iconphoto(False, tk.PhotoImage(
        file=fr"{CWD}/{LOGO}"))
    root.geometry(f"{x_canvas}x{y_canvas}")
    # Used exclusively by the level select
    div = tk.Canvas(root, width=x_canvas, height=y_canvas)
    div.pack()

    def copyright():
        messagebox.showinfo(
            "Info", f"© {__author__} 2024. \n Made on behalf of {COMPANY}")

    def about():
        messagebox.showinfo(
            "Info", f"Version: {__version__} \n See latest patchnotes via \
readme.md as either raw text or in your favourite markdown viewer")

    def tutorial():
        messagebox.showerror(
            "Help", tutorial_text)

    def alt_questions():
        filename = filedialog.askopenfilename(
            title="Select JSON file", initialdir="/",
            filetypes=[("Json", '*.json')])
        try:
            gather_data(filename)
            global source_file
            messagebox.showinfo(
                "Success",
                "Worked perfectly, changed may be buggy unless restarted")
            if __debug__ == False:
                print("New files loaded successfully")
            source_file = filename
            pass
        except IndexError:
            gather_data(DEFAULT_JSON_FILE)
            if __debug__ == False:
                print("Failed")
                messagebox.showerror(
                    "Error with custom file",
                    "Your file apears to be an incompatible format, \
Please check and try again.")
            pass

    menubar = tk.Menu(root)
    root.config(menu=menubar)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Create Custom Questions",
                         command=json_maker.create_file)
    filemenu.add_command(label="Select Custom Level set",
                         command=alt_questions)
    menubar.add_cascade(label="File", menu=filemenu)
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
        incorrect_answers = 0

        def show_results():
            clear_div()
            nonlocal incorrect_answers
            lable = ttk.Label(
                div, text=f"Excellent Job, {username}! \n\
You've completed the quiz!")
            lable.pack()
            for i, questions in enumerate(question_set):  # question_set[i]
                try:
                    lable = ttk.Label(
                        div, text=f"Question: {question_set[i][0]} \
Correct answer was: {question_set[i][1]} \
(You entered: {question_set[i][2]})").pack()
                    incorrect_answers += 1
                except IndexError:
                    lable = ttk.Label(
                        div, text=f"Question: {question_set[i][0]} \
Correct answer was: {question_set[i][1]}").pack()
            total_answers, correct_answers = len(
                question_set), len(question_set) - incorrect_answers
            lable = ttk.Label(
                div, text=f"You got {correct_answers} right of {total_answers}\
. This means you got a score of {int((correct_answers/total_answers) * 100)}%"
                                        ).pack()
            button = ttk.Button(div, text="Start Again?",
                                command=lambda: [leave(), main()])
            button.pack()
            button = ttk.Button(root, text="Quit", command=leave)
            button.pack()

        def compare_answers():
            nonlocal current_question
            answer = entry.get().strip()
            correct_answer = question_set[current_question][1]
            if __debug__ == False:
                print(f"User: {answer}, Correct: {correct_answer}")
            clear_div()
            result = str(answer) == str(correct_answer)
            if result == 0:
                question_set[current_question].append(answer)
                if __debug__ == False:
                    print(question_set)
            if result == 1:
                lable = ttk.Label(div, text="Good Job! You got it right!")
                lable.pack()
            else:
                lable = ttk.Label(div, text="Unlucky! You got it wrong")
                lable.pack()
            button = ttk.Button(div, text="Next?",
                                command=lambda: level(hardness, index))
            button.pack()
            current_question += 1  # Increment after setting answers

        if __debug__ == False:
            print(index)
            print(question_set)
            # iterate throught all questions for debuging
            for questions in question_set:  # Numeric index bc nested list
                print(f"Question: {questions[0]}, Answer: {questions[1]}")
        # will need to add a try: except for index error, go to result screen
        try:
            lable = ttk.Label(div, text=question_set[current_question][0])
            lable.pack()
            entry = ttk.Entry(div)
            entry.pack()
            sumbit = ttk.Button(div, text="Submit Answer",
                                command=compare_answers)
            sumbit.pack()
            div.update()
        except IndexError:
            print("Slightly intented, easiest way to find end of list")
            show_results()
            pass

    def level_select():
        for i, options in enumerate(difficulties):  # i refers to the index
            options = ttk.Button(div, text=options.title(
            ),  command=lambda i=i, hardness=options: level(hardness, i))
            if __debug__ == False:
                print(f"options:{options}, i:{i}")
            options.pack()

    def getusername():

        def check_name():
            global username  # Use the global scope else incorrect assignment
            value = box.get().strip().title().replace("-", "")
            if value.isalpha() and 2 < len(value) < 15:
                username = value
                if __debug__ == False:
                    print(box.get())
                    print(f"{username =}")
            else:
                username = ""
                messagebox.showerror(
                    "Non-fatal Error!",
                    "Your name needs to be bewteen 2 and 15 chars, \
and only including latin chars")
            if username != "":
                label.destroy()
                box.destroy()
                submit.destroy()
                welcoming.destroy()
                level_select()

        welcoming = ttk.Label(root,
                              text=f"Welcome to {__author__.split()[0]}\
's Math game!")
        welcoming.place(relx=0.43, rely=0.2)
        label = ttk.Label(root, text="Please enter your name")
        label.place(relx=0.45, rely=0.25, relwidth=0.1)
        # User input handling
        box = ttk.Entry(root)
        box.place(relx=0.45, rely=0.3, relwidth=0.1)

        submit = ttk.Button(root, text="Submit Name",
                            command=lambda: check_name())
        submit.place(relx=0.45, rely=0.5, relwidth=0.1)

    clear_div()
    gather_data(source_file)
    current_question: int = 0
    root.state("zoomed")
    end = ttk.Button(root, text="Quit", command=leave)
    end.place(relx=0.95, rely=0.95)
    getusername()
    root.mainloop()


if __name__ == "__main__":
    main()
