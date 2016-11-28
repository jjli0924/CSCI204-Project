import sys
from tkinter import *

def doNothing():
    pass

def bs():
    pass

Gui1 = Tk()
Gui1.geometry('1000x500')
Gui1.title("CSCI 204 Final Project")

menu = Menu(Gui1)
Gui1.config(menu=menu)

docMenu = Menu(menu)
menu.add_cascade(label=" Documents'", menu = docMenu)
docMenu.add_command(label = "Documents Window", command=doNothing)


trainMenu = Menu(menu)
menu.add_cascade(label="Train", menu=trainMenu)
trainMenu.add_command(label="Train", command = doNothing)

predictMenu = Menu(menu)
menu.add_cascade(label="Predict", menu=predictMenu)
predictMenu.add_command(label="Predit", command = doNothing)

authorLabel = Label(Gui1,text='Jonathan Li and Katie Lunceford',fg='white',bg='black')
authorLabel.pack()

DescriptionLabel = Label(Gui1,text='This program implements machine learning techniques for the purpose of authorship attribution',fg='white',bg='black')
DescriptionLabel.pack()

labelFrame = LabelFrame(Gui1,text = "Title                                   Genre            Year            Author ")
labelFrame.pack(fill= "both", expand = "yes")

#The different documents will be inserted into the document as followed.
left = Label(labelFrame,text = "fadsfksad")
left.pack()

docName = StringVar()
docEntry = Entry(Gui1, textvariable= docName)
docEntry.grid(sticky=W)
docEntry.pack()

AddDocumentButton = Button(Gui1,text='Add Document',command=bs)
AddDocumentButton.grid(sticky=E)
AddDocumentButton.pack()

trainFrame = LabelFrame(Gui1,text = "TRAIN")
trainFrame.pack(fill= "both", expand = "yes")

