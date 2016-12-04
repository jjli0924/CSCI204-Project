""" pair programming with katie lundeford

Summary:
Overview of GUI with TK. Learned how to pack buttons and event-driven. With that,
we can make things look a lot more user friendly. The calculator was a simple
example of how to implement Tkinter for graphical use.
"""

'''didnt work however because the imports didn't work right and crash couldn't be figured
out. However idea is to have command= plotting the function'''

from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
from graphicplot import *

class UserGUI:

    def __init__(self, master):
        self.master = master
        master.title("Word Count Graph")

        self.total = 0
        self.entered_number = 0

        self.label = Label(master, text="Enter a valid text file to analyze: ")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.graphallbutton = Button(master, text="Graph", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.graphallbutton.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
my_gui = UserGUI(root)
root.mainloop()
