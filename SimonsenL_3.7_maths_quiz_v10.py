"""
Game made to support year 9s in learning maths.

Made for 13CSI_2024
Use the command line arg -O when running

https://github.com/AltraMage/3.7_maths_quiz
"""
# Created 4/05/24

from os import getcwd
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import json_maker_ux

"""
COMPANY, LOGO, AND CWD are all constant.
CWD represents the current working directory,
allows the program to run on Windows, GNU/Unix & macOS
"""
__version__ = "1.0.3"  # Submition version
__author__ = "Logan Simonsen"
COMPANY: str = "13CSI_2024"
LOGO: str = "icon.gif"
CWD = getcwd()
DEFAULT_JSON_FILE = "year_9_questions.json"

source_file = DEFAULT_JSON_FILE
username: str = ""
data, difficulties = [], []
font = ("Arial", 16)
current_theme = "dark"


TUTORIAL_TEXT = """
You need to enter a valid username, choose a difficulty, and then answer each \
question.

You will then be shown a results screen with your provided answers if \
incorrect.

You will then have the option to quit or start again from the begining.
You can create or choose new question sets via the menu bar.
"""


def gather_data(source):
    """Get data from specificed JSON file."""
    global data, difficulties
    # Get the data for the questions
    try:
        with open(source, "r") as file:
            data = json.load(file)
    except FileNotFoundError as no_file_error:
        messagebox.showerror("You may need to reinstall the program",
                             f"{source} could not be located. \
Please go to the file drop down menu to manually select a question file \n\n\
{no_file_error}")
    if __debug__ is not False:
        print(data)

    # Create list of all the difficulties
    difficulties = []
    for i in data:
        difficulties.append(i)


def main():
    """Control the main canvas."""
    root = tk.Tk()
    styling = ttk.Style()
    # Theme used under MIT licence, thanks to rdbende.
    root.call("source", "azure.tcl")
    root.call("set_theme", current_theme)
    if __debug__ is not False:
        print(styling.theme_use())
    # Sets variables to the screen max size
    x_canvas, y_canvas = root.winfo_width(), root.winfo_height()
    if __debug__ is not False:
        print(x_canvas, y_canvas)
    root.title(f"Math game for {COMPANY}")
    # Sets the app icon to be the tawa college emblem
    root.iconphoto(False, tk.PhotoImage(
        file=fr"{CWD}/{LOGO}"))
    # Set the window size to max possible
    root.geometry(f"{x_canvas}x{y_canvas}")
    div = tk.Canvas(root, width=x_canvas, height=y_canvas)
    div.pack()

    def swap_theme():
        """
        Swap theme color pallet

        Could be implemented using switch, at the cost of readabilty
        """
        global current_theme
        if current_theme == "dark":
            current_theme = "light"
        else:
            current_theme = "dark"
        root.call("set_theme", current_theme)  # Update

    def copyright():
        messagebox.showinfo(
            "Info", f"© {__author__} 2024. \n Made on behalf of {COMPANY}")

    def about():
        messagebox.showinfo(
            "Info", f"Version: {__version__} \n See latest patchnotes via \
readme.md as either raw text or in your favourite markdown viewer")

    def tutorial():
        messagebox.showerror(
            "Help", TUTORIAL_TEXT)

    def alt_questions():
        # Get the user to choose a file to use
        filename = filedialog.askopenfilename(
            title="Select JSON file", initialdir="/",
            filetypes=[("Json", '*.json')])
        try:
            gather_data(filename)
            global source_file
            messagebox.showinfo(
                "Success",
                "Worked perfectly, reseting now!")
            if __debug__ is not False:
                print("New files loaded successfully")
            source_file = filename
            # Quit and then re-run program with new questions
            leave(), main()
            pass
        except IndexError:  # Revert to default JSON file
            gather_data(DEFAULT_JSON_FILE)
            if __debug__ is not False:
                print("Failed")
                messagebox.showerror(
                    "Error with custom file",
                    "Your file apears to be an incompatible format, \
Please check and try again.")
            pass

    # Menu bar items, could be refactored
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Create Custom Questions",
                         command=json_maker_ux.create_file)
    filemenu.add_command(label="Select Custom Level set",
                         command=alt_questions)
    menubar.add_cascade(label="File", menu=filemenu)
    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Copyright", command=copyright)
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="Tutorial", command=tutorial)
    menubar.add_cascade(label="Help", menu=helpmenu)

    def clear_div():
        # Delete all items in the window
        for child in div.winfo_children():
            child.destroy()
        div.update()

    def leave():
        """Kill the window."""
        root.destroy()

    def level(hardness, index):
        # Starts each level with the difficulty and the index of the difficulty
        clear_div()

        question_set = data[hardness]  # Hardness bc data is a dict
        incorrect_answers = 0

        def show_results():
            """
            Show the user the quiz results

            question_set format:
            question_set[i] is the difficulty
            question_set[i][0] is the question
            question_set[i][1] is the answer
            question_set[i][2] is the user given answer
            The index at [2] only exists is the user got the question wrong
            because of this we can presume the user go the question wrong and
            except the error if they didn't (they got it right)

            Two quit buttons because it is better to have the one always
            in the bottom right and then a new more obvious one.
            """
            clear_div()
            nonlocal incorrect_answers
            lable = ttk.Label(
                div, text=f"Excellent Job, {username}! \n\
You've completed the quiz!")
            lable.pack()
            # questions is unused, but needed due to enumerate
            for i, questions in enumerate(question_set):  # question_set[i]
                try:
                    # Display results from nested list
                    lable = ttk.Label(
                        div, text=f"Question: {question_set[i][0]} \
Correct answer was: {question_set[i][1]} \
(You entered: {question_set[i][2]})").pack()
                    incorrect_answers += 1
                except IndexError:  # Error to see if question is correct
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
            # Post answer comparison feedback
            nonlocal current_question
            answer = entry.get().strip()
            correct_answer = question_set[current_question][1]
            if __debug__ is not False:
                print(f"User: {answer}, Correct: {correct_answer}")
            clear_div()
            result = str(answer).lower() == str(correct_answer).lower()
            if result == 0:
                question_set[current_question].append(answer)
                if __debug__ is not False:
                    print(question_set)
            if result == 1:  # if result is true
                lable = ttk.Label(div, text="Good Job! You got it right!")
                lable.pack()
            else:
                lable = ttk.Label(div, text="Unlucky! You got it wrong")
                lable.pack()
            button = ttk.Button(div, text="Next?",
                                command=lambda: level(hardness, index))
            button.pack()
            current_question += 1  # Increment after setting answers

        if __debug__ is not False:
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
            entry.focus()
            sumbit = ttk.Button(div, text="Submit Answer",
                                command=compare_answers)
            sumbit.pack()
            div.update()
        except IndexError:
            # Error to console, wont effect end user.
            print("Slightly intented, easiest way to find end of list")
            show_results()
            pass

    def level_select():
        # Create a button for each difficulty
        for i, options in enumerate(difficulties):  # i refers to the index
            options = ttk.Button(div, text=options.title(
            ),  command=lambda i=i, hardness=options: level(hardness, i))
            if __debug__ is not False:
                print(f"options:{options}, i:{i}")
            options.pack()

    def getusername():
        # Code for getting a valid username
        def check_name():
            global username  # Use the global scope else incorrect assignment
            value = username_entry.get().strip().title().replace("-", "")
            if value.isalpha() and 2 <= len(value) <= 15:
                username = value
                if __debug__ is not False:
                    print(username_entry.get())
                    print(f"{username=}")
            else:
                username = ""
                messagebox.showerror(
                    "Non-fatal Error!",
                    "Your name needs to be bewteen 2 and 15 chars, \
and only including latin chars")
            if username != "":
                label.destroy()
                username_entry.destroy()
                submit.destroy()
                welcoming.destroy()
                level_select()

        # Using the auther dunder constant, get the first word
        welcoming = ttk.Label(root,
                              text=f"Welcome to {__author__.split()[0]}\
's Quiz!")
        welcoming.pack()
        label = ttk.Label(root, text="Please enter your name")
        label.pack()
        # User input handling
        username_entry = ttk.Entry(root)
        username_entry.pack()
        username_entry.focus()

        submit = ttk.Button(root, text="Submit Name",
                            command=lambda: check_name())
        submit.place(relx=0.45, rely=0.5, relwidth=0.1)

    clear_div()
    gather_data(source_file)
    current_question: int = 0
    # Make it full screen, note animation time.
    root.state("zoomed")

    # Buttons for user control and freedom
    theme_toggle = ttk.Button(root, text="Light / Dark", command=swap_theme)
    theme_toggle.place(relx=0.93, rely=0.9)
    end = ttk.Button(root, text="Quit", command=leave)
    end.place(relx=0.93, rely=0.95)

    getusername()
    root.mainloop()


if __name__ == "__main__":
    main()
