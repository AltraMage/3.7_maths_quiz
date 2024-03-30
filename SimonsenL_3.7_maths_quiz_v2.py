"""
Game made to support year 9s in learning maths.
Made for 13CSI_2024
Use the command line arg -O when running
"""
# Created 26/03/24

from os import getcwd
import tkinter as tk
from tkinter import messagebox

"""
COMPANY, LOGO, AND CWD are all constant.
CWD represents the current working directory,
allows the program to run on Windows, GNU/Unix & macOS
"""
__version__ = "0.2"
# Basic questions
__author__ = "Logan Simonsen"
COMPANY: str = "13CSI_2024"
LOGO: str = "icon.gif"
CWD = getcwd()


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

    def getusername():
        username: str = ""
        def check():
            nonlocal username
            value = box.get().strip().title().replace("-", "")
            if value.isalpha() and 2 < len(value) < 15:
                if __debug__:
                    print(box.get())
                username = value
            if username != "":
                label.destroy()
                box.destroy()
                submit.destroy()
                
        label = tk.Label(root, text="Please enter your name")
        label.place(relx=0.45, rely=0.25)
        # User input handling
        box = tk.Entry(root, width=16)
        box.place(relx=0.45, rely=0.3)

        submit = tk.Button(root, text="Submit Name", command=lambda: check())
        submit.place(relx=0.45, rely=0.5)





    end = tk.Button(root, text="Quit", command=leave)
    end.place(x=x_canvas-60, y=y_canvas-30)
    getusername()
    root.mainloop()


if __name__ == "__main__":
    main()
