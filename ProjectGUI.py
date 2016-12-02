from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E, LabelFrame
from TextFilter import *
from tkinter import *

# predict needs an entry point....


class GUI:

    def __init__(self, master):
        self.master = master
        master.title("CSCI-204 Final Project")
        self.file = None
        self.filtL = []
        self.prediction = None
        self.master.minsize(width=350,height=700)

# message Label Text Stuff

        self.workingLabel = Label(master ,text = "File to Edit: ")
        
# Entry box storage section
        vcmd = master.register(self.validate)
        vcmd1 = master.register(self.validateFile)
        vcmd2 = master.register(self.validateGenre)
        vcmd3 = master.register(self.validateYear)
        vcmd4 = master.register(self.validateAuthor)
 #       vcmd5 = master.register(self.trainers)
        self.entry = Entry(master, validate="key",validatecommand=(vcmd, '%P'))
                        
# Buttons and input boxes declaration
        self.add_document = Button(master, text="Add Document", command=lambda: self.update("add"))

        self.fileEntry = Entry(master,validate='key',validatecommand = (vcmd, '%P'),bd=3)
        self.workingEntry = Entry(master,validate='key',validatecommand = (vcmd1,'%P'),bd = 3)

        

        self.filter0 = Button(master, text= "Normalize White Space", command=lambda: self.appFilter("normalize white space"))
        self.filter1 = Button(master, text= "Normalize Case", command=lambda: self.appFilter("normalize case"))
        self.filter2 = Button(master, text= "Strip Null", command=lambda: self.appFilter("strip null characters"))
        self.filter3 = Button(master, text= "Strip Numbers", command=lambda: self.appFilter("strip numbers"))
        self.filter4 = Button(master, text= "Strip Common Words", command=lambda: self.appFilter("strip common words"))
        self.appFilter = Button(master, text= "APPLY FILTERS", command=lambda: self.appFilter("apply filters"))

        self.addInfo = Label(master,text = "-----------Add Info--------------")
        self.addInfo.grid(row=3,column=1,stick=W+E)
        self.GenreButt = Button(master, text = 'Enter Genre', command = lambda: self.addInfo('genre'))
        self.GenreEnt = Entry(master, validate = 'key', validatecommand = (vcmd2,'%P') ,bd=3)       
        self.YearButt = Button(master, text = 'Enter Year', command = lambda: self.addInfo('year'))
        self.YearEnt = Entry(master, validate = 'key', validatecommand = (vcmd3,'%P'),bd=3)
        self.AuthorButt = Button(master, text = 'Enter Author', command = lambda: self.addInfo('author'))
        self.AuthorEnt = Entry(master, validate = 'key', validatecommand = (vcmd4,'%P'),bd=3)

        self.filtlab = Label(master,text="------------Filters------------")
        self.filtlab.grid(row=7,column=1)
                             
        self.trainsection = Label(master,text="--------Training----------")
        self.trainsection.grid(row=14,column=1,stick=W+E)
        self.statmethod1 = Button(master,text = "Stat Method 1",command = lambda: self.chooseStat('1'))
        self.statmethod2 = Button(master,text = "Stat Method 2",command = lambda: self.chooseStat('2'))
        self.statmethod3 = Button(master,text = "Stat Method 3",command = lambda: self.chooseStat('3'))
        self.trainButton = Button(master,text = "TRAIN", command = lambda: self.training())

        self.PredictButton = Button(master,text="Predict",bd=5,command = lambda:self.training())
        self.PredictLabel = Label(master,text="Prediction: " + str(self.prediction))

        self.master.bind('<Return>',lambda event:self.update("enter"))
                           
#Layout and grid

        self.fileEntry.grid(row=1,column = 0, columnspan = 3,stick=W+E)

        self.add_document.grid(row=1,column=3,stick=W+E)
        self.filter0.grid(row=8,column=1,stick=W+E)
        self.filter1.grid(row=9,column=1,stick=W+E)
        self.filter2.grid(row=10,column=1,stick=W+E)
        self.filter3.grid(row=11,column=1,stick=W+E)
        self.filter4.grid(row=12,column=1,stick=W+E)
        self.appFilter.grid(row=13,column=1,stick=W+E)

        self.GenreButt.grid(row = 4,column=1,stick=W+E)
        self.GenreEnt.grid(row=4, column =2,stick = W+E)
        self.YearButt.grid(row = 5,column=1,stick=W+E)
        self.YearEnt.grid(row=5, column =2,stick = W+E)
        self.AuthorButt.grid(row = 6,column=1,stick=W+E)
        self.AuthorEnt.grid(row=6, column =2,stick = W+E)

        self.statmethod1.grid(row=15,column =1, stick = W+E)
        self.statmethod2.grid(row=16,column =1, stick = W+E)
        self.statmethod3.grid(row=17,column =1, stick = W+E)
        self.trainButton.grid(row=18,column=2,stick=W+E)

        self.PredictButton.grid(row=19,column=1,stick=W+E)
        self.PredictLabel.grid(row=19,column=2)

        self.Documents = Label(master,text="Title                   Genre              Author       Year")
        self.Documents.grid(row=21,column=1)
        
        self.text = Text(master)
        self.text.grid(row=22,column=1)
        
    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_file= 0
            return True

        try:
            self.entered_file = str(new_text)
            return True
        except ValueError:
            return False

    def validateFile(self,newtext):
        if not newtext:
            self.newFile = 0
            return True
        try:
            self.newFile = newtext
            return True
        except ValueError:
            return False

    def validateGenre(self,newtext):
        if not newtext:
            self.genre = None
            return True
        try:
            self.genre = newtext
            return True
        except ValueError:
            return False

    def validateAuthor(self,newtext):
        if not newtext:
            self.author = None
            return True
        try:
            self.author = newtext
            return True
        except ValueError:
            return False

    def validateYear(self,newtext):
        if not newtext:
            self.year = 0
            return True
        try:
            self.year = newtext
            return True
        except ValueError:
            return False

    def addInfo(self,infotype):
        if infotype == 'genre':
            self.newFile.genre = self.genre
        if infotype == 'year':
            self.newFile.year = self.year
        if infotype == 'author':
            self.newFile.author = self.author

    def appFilter(self,method):
        '''apply the filter'''
        if method == "apply filters":
            newtext = TextFilter(self.newFile,self.filtL)
            newtext.applyFilters()
        else:
            if method not in filtL:
                self.filtL.append(str(method))
                
    def chooseStat(self,method):
        '''applies the Stat Method'''
        if method == '1':
            pass
        if method == '2':
            pass
        if method =='3':
            pass

    def training(self,method):
        pass
                    

    def update(self, method):
        if method == "add":
            self.file = str(self.entered_file)
            self.text.insert(INSERT,' '*16 + str(self.entered_file) + '\n')
 #           self.main()
                                                 
        self.fileEntry.delete(0,END)

root = Tk()
my_gui = GUI(root)
root.mainloop()
