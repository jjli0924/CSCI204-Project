class Node:
    def __init__(self,data= [],nextNode= None):
        self.data = None
        self.next = next_node

    def __repr__(self):
        return self.data

class SLinkIterator:
    def __init__(self,head):
        self.runner = head

    def __iter__(self):
        return self

    self __next__(self):
        if self.runner == None:
            raise StopIteration

        else:
            nxt = self.runner.data
            self.runner = self.runner.next
            return nxt
        
class SLink:
    def __init__(self):
        '''
        self.nstack = sStack()
        self.nsize = 32
        for i in range(self.nsize):
            self.nstack.push(Node())
        '''
        self.list = None
        self.head = None
        self.size =  0

    def __len__(self):
        runner = self.head
        count = 0
        while runner != None:
            count +=1
            runner = runner.next
        return count
    
    def add(self,item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def remove(self,item):
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
    
    def __topN__(self):
        pass

