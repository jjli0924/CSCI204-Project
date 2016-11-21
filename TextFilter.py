
class TextFilter:
    def __init__(self,document=None, elist=None):
        self.document = document
        self.elist = elist
        
    def normalizeWhitespace(self):
        '''make all white space, 1 space'''
        #if white space
        #get rid of new lines or multiple spaces
        # switch on if white space and continue...turn that into one white space
        self.document = self.document.replace(' ', '_')
        self.document = self.document.replace('\n','_')
        while '__' in self.document:
            self.document = self.document.replace('__','_')
        return self.document
    def normalizecase(self):
        '''make all letters lower case'''
        self.document.lower()
        
    def stripnullcharacters(self):
        '''remove characters not in standard set of letters and numbers'''
        for i in range(len(self.document)):
            a = self.document[i]
            if self.isitaletter(a) == True or self.isitanumber(a) == True:
                pass
            else:
                if a == (len(self.document)-1):
                    self.document[:a]
                else:
                    self.document = self.document[:a]+self.document[a+1:]
    def isitaletter(self, a):
        if a in 'qwertyuiopasdfghjklzxcvbnm':
            return True
        else:
            return False
    def isitanumber(self, a):
        if a in '0123456789':
            return True
        else:
            return False
        
    def stripnumbers(self):
        '''removes all numbers'''
        numbers = '0123456789'
        for i in range(len(self.document)):
            if self.document[i] in numbers:
                if i == len(self.document)-1:
                    self.document = self.document[:i]
                else:
                    self.document = self.document[:i] + self.document[i+1:]
            else:
                pass

    def stripCommon(self):
        f = open('test.txt', 'r')    #open test.tx
        for line in f:
            for i in range(len(self.document)):
                if self.document[i] == line:
                    self.document[i].remove()
                 
    def apply(self):
        '''apply all the requested filters in the order in which the user provided them'''
        '''walk to string and loops through and selects which one to apply'''
        for method in self.elist:
            if method == 'normalize white space':
                self.normalizeWhitespace()
            elif method == 'normalize case':
                self.normalizecase()
            elif method == 'strip null characters':
                self.stripnullcharacters()
            elif method == 'strip numbers':
                self.stripnumbers()
            elif method == 'strip commonwords':
                self.stripCommon()
            
            
                
    
