"""
Create a json file for use in Logan's 13CSI Tkinter program.

Data is a dict with nested list.
"""
import tkinter as tk
import json

__author__ = "Logan Simonsen"

"""
General Flow is as follows:

1. Ask the user if they want to add a new difficulty
 - No? Quit
 - Yes? Get the difficulty name.

2. Ask the user for the Nth question.
3. Ask the user for the Nth answer, showing the user their entered question.
4. Ask if they want to repeat from step 2.
- Yes? GoTo 2.
- No? Ask if they want to repeat from step 1.
5. Ask for the filename
6. Get the user to choose the location of the file
"""


def create_file():
    """Run the Main function."""
    X, Y = 400, 300  # Gets omitted if other ran externally
    popup = tk.Tk()
    popup.geometry(f"{X}x{Y}")
    popup.title("Question Creator")
    main = tk.Canvas(popup, width=X, height=Y)
    main.pack()
    data = {}

    def end():
        popup.destroy()

    emergency_exit = tk.Button(popup, text="Quit without saving", command=end)
    emergency_exit.pack(anchor=tk.SE)

    def clear():
        for child in main.winfo_children():
            child.destroy()
        main.update()

    def yesno(question: str, yes: object, no: object):
        lable = tk.Label(main, text=question)
        lable.pack()
        yes_button = tk.Button(main, text="Yes",
                               command=lambda: [clear(), yes()])
        yes_button.pack()
        no_button = tk.Button(main, text="No",
                              command=lambda: [clear(), no()])
        no_button.pack()

    def save_data():
        clear()

        def final():
            with open(f"{entry.get()}.json",
                      "w", encoding="utf8") as json_file:
                json.dump(data, json_file, indent=4)
            end()

        label = tk.Label(
            main, text="Please enter the name for the JSON file. \
(Omit the .json sufix)")
        label.pack()
        entry = tk.Entry(main)
        entry.pack()
        button = tk.Button(main, text="Save & Finalise", command=final)
        button.pack()

    def difficulty():
        def questions():
            questions = []
            diff = entry.get().title()
            if diff.strip() == "":
                return None

            def add_diff():
                nonlocal data
                data[diff] = questions

            def append():
                q = question_entry.get().strip().title()
                a = answer_entry.get().strip().title()
                if q == "" or a == "":
                    print("Null values in Question or Answer")
                    return None
                questions.append([q, a])
                print(f"added {q}, {a}")
                question_entry.delete(0, tk.END)
                answer_entry.delete(0, tk.END)

            clear()
            question_lable = tk.Label(
                main, text=f"Please add a question into {diff}")
            question_lable.pack()
            question_entry = tk.Entry(main)
            question_entry.pack()
            answer_lable = tk.Label(main, text="Please write the answer.")
            answer_lable.pack()
            answer_entry = tk.Entry(main)
            answer_entry.pack()
            button = tk.Button(main, text="Submit", command=append)
            button.pack()
            tk.Button(main, text="Cancel", command=lambda: [
                      add_diff(), start()]).pack()

        lable = tk.Label(
            main, text="What is the name of the difficulty to add?")
        lable.pack()
        entry = tk.Entry(main)
        entry.pack()
        submit = tk.Button(main, text="Submit", command=questions)
        submit.pack()

    def start():
        clear()
        yesno("Do you want to add a difficulty? ", difficulty, save_data)

    start()
    popup.mainloop()


# If ran as a standalone package.
if __name__ == "__main__":
    create_file()
