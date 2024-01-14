# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyBasic import run_basic
from threading import Thread
from tkinter import *
import wget
import os

# An IDE for PyBasic

if os.path.exists('tmp') == False:
    os.mkdir('tmp')

try:
    if os.path.exists('tmp/LICENSE') == True:
        le = open('tmp/LICENSE', 'r')
        License_ide = le.read()
        le.close()
    else:
        wget.download('https://raw.githubusercontent.com/Jeremy823/PyBasic-IDE/main/LICENSE', 'tmp/LICENSE')
        le = open('tmp/LICENSE', 'r')
        License_ide = le.read()
        le.close()
except: print("Failed to download the 'LICENSE' file!")

def run():
    command = text.get('1.0', 'end-1c')
    save = open('tmp/tmp.bas', 'w')
    save.write(command)
    save.close()
    clear_term()
    run_basic.compile('tmp/tmp.bas')

def clear():
    text.delete('1.0', END)

def clear_term():
    if os.name == "posix":
        os.system('clear')
    elif os.name in ("nt", "dos", "ce"):
        os.system('CLS')
    else:
        print('\n' * 100)

def about(License_ide=License_ide):
    about = Toplevel(root)
    about.title("About")
    Label(about, text="Python Basic IDE by Jeremy823").pack()
    Label(about, text="PyBasic Author: https://github.com/richpl/PyBasic").pack()
    Label(about, text="License").pack
    about_scrollbar = Scrollbar(about)
    about_scrollbar.pack(side = RIGHT, fill = Y) 
    license_ide = Text(about, yscrollcommand = about_scrollbar.set)
    license_ide.pack()
    license_ide.insert('1.0', License_ide)
    about_scrollbar.config(command=license_ide.yview)
    Button(about, text="Ok", command=about.destroy).pack()

root = Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title("PyBasic IDE by Jeremy823")

scrollbar = Scrollbar(root)
scrollbar.grid(column=1, row=0, sticky=NS)

text = Text(root, undo=True, yscrollcommand = scrollbar.set)
text.grid(column=0, row=0, sticky=NSEW)
scrollbar.config( command = text.yview ) 

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
