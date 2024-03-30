"""
Game made to support year 9s in learning maths.
Made for 13CSI_2024
Use the command line arg -O when running
"""
# Created 26/03/24

from os import getcwd
import tkinter as tk
from tkinter import messagebox
import json

"""
COMPANY, LOGO, AND CWD are all constant.
CWD represents the current working directory,
allows the program to run on Windows, GNU/Unix & macOS
"""
__version__ = "0.4"
__author__ = "Logan Simonsen"
COMPANY: str = "13CSI_2024"
LOGO: str = "icon.gif"
CWD = getcwd()
JSON_DATA_FILE = "data.json"

# Get the data for the questions
with open(JSON_DATA_FILE, "r") as file:
    data = json.load(file)
if __debug__:
    print(data)

difficulties = []
for i in data:
    difficulties.append(i)
if __debug__:
    print()
    print(difficulties)

def main():
    """Control the main canvas"""
    root = tk.Tk()
    root.state("zoomed")
    # Update root's variables (x,y return 1 otherwise)
    root.update_idletasks()
    x_canvas, y_canvas = root.winfo_width(), root.winfo_height()
    if __debug__:
        print(x_canvas, y_canvas)
    root.title(f"Math game for {COMPANY}")
    # Sets the app icon to be the tawa college emblem
    root.iconphoto(False, tk.PhotoImage(
        file=fr"{CWD}/{LOGO}"))
    root.geometry(f"{x_canvas}x{y_canvas}")
    div = tk.Canvas(root, width=x_canvas, height=y_canvas) # Used exclusively by the level select
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

    def leave():
        """Kill the window"""
        root.destroy()

    def level(hardness, index):
        global data
        for child in div.winfo_children():
            child.destroy()
        if __debug__:
            print(index)
        question_set = data[hardness]

    def level_select():
        for i, options in enumerate(difficulties):  # i refers to the index
            options = tk.Button(div, text=options.title(),  command=lambda i=i, hardness=options: level(hardness, i))
            if __debug__:
                print(f"options:{options}, i:{i}")
            options.pack()

    def getusername():
        username: str = ""
        def check():
            nonlocal username
            value = box.get().strip().title().replace("-", "")
            if value.isalpha() and 2 < len(value) < 15:
                if __debug__:
                    print(box.get())
                username = value
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

        submit = tk.Button(root, text="Submit Name", command=lambda: check())
        submit.place(relx=0.45, rely=0.5, relwidth=0.1)





    end = tk.Button(root, text="Quit", command=leave)
    end.place(x=x_canvas-60, y=y_canvas-30)
    getusername()
    root.mainloop()


if __name__ == "__main__":
    main()
