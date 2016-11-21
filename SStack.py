import sLListClass as SL
    
class SStack:
    def __init__(self):
        '''
        self.nstack = sStack()
        self.nsize = 32
        for i in range(self.nsize):
            self.nstack.push(Node())
        '''
        self.stck = SL.SLink()
        self.size = 0

    def __len__(self):
        return self.size
    
    def push(self,item):
        self.size +=1
        self.stck.insert(item)

    def pop(self):
        self.size -=1 
        if self.stck.head == None:
            return None
        placeholder = self.stck.data
        self.stck.head = self.stck.head.next
        return placeholder
    
    def __topN__(self):
        for i in range(self.size):
            maxval = None
            if self.stck[i] >= maxval:
                maxval = self.stck[i]
        return maxval
            

class Slink:
    def __init__(self):
        self.nstack = SStack()
        self.nsize = 64
        for i in range(self.nsize):
            self.nstack.push(Node())

    def add(self,item):
        newNode = none
        if self.nstack.isEmpty():
            newNode = Node()
        else:
            newNode = self.nstack.pop()
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def remove(self):
        prev = None
        runner = self.head
        while runner.data[0] != item and runner != None:
            prev = runner
            runner = runner.next
        if runner == None:
            self.head = runner.next
            del runner
        else:
            prev.next = runner.next
            del runner
        runner.next = None
        runner.data = None
        self.nstack.push(runner)
