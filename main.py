from PyBasic import run_basic
from threading import Thread
from tkinter import *
import os

# An IDE for PyBasic

def run():
    command = text.get('1.0', 'end-1c')
    save = open('tmp.bas', 'w')
    save.write(command)
    save.close()
    clear_term()
    run_basic.compile('tmp.bas')

def clear():
    text.delete('1.0', END)

def clear_term():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print('\n' * 100)

def about():
    about = Toplevel(root)
    Label(about, text="Python Basic IDE by Jeremy823").pack()
    Label(about, text="PyBasic Author: https://github.com/richpl/PyBasic").pack()
    Button(about, text="Ok", command=about.destroy).pack()

root = Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title("PyBasic IDE by Jeremy823")

text = Text(root, undo=True)
text.grid(sticky=NSEW)

menu = Menu(root)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear", command=clear)

run_menu = Menu(menu, tearoff=0)
menu.add_cascade(menu=run_menu, label="Run")
run_menu.add_command(label="Run", command=run)
run_menu.add_separator()
run_menu.add_command(label="Clear TERM", command=clear_term)

help_menu = Menu(menu, tearoff=0)
menu.add_cascade(menu=help_menu, label="Help")
help_menu.add_command(label="About", command=about)

root.config(menu=menu)
root.mainloop()
