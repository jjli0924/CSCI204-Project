class minHeap:
    def __init__(self):
        self.root = None
        self.heapL = []

    def parent(self, index):
        if len(self.heapL) < index or index == 1:
            return
        elif self.heapL[0] == None:
            return self.heapL[index//2]
        else:
            return self.heapL[(index-1)//2]

    def rightChild(self,index):
        if len(self.heapL) < index:
            return
        elif self.heapL[0] == None:
            return self.heapL[2*index]
        else:
            return self.heap[2*index + 2]

    def leftChild(self,index):
        if len(self.heapL) < index:
            return
        elif self.heapL[0] == None:
            return self.heapL[2*index]
        else:
            return self.heap[2*index +1]

    def heapAdd(self,val):
        if self.heapL == []:
            self.heapL += [None]
            self.heapL += [val]
        else:
            self.heapL += val
            self.fixUp(val)

    def fixUp(self,val):
        ind = self.heapL.index(val)
        prnt = self.parent(index)
        if prnt == None:
            pass
        else:
            pInd = self.heapL.index(prnt)
            if prnt > val:
                self.heapL[pInd] = val
                self.heapL[ind] = prnt

    def heapRemove(self,val):
        place = self.heapL[1]
        self.heapL[1] = self.heapL[-1]
        del self.heapL[-1]
        self.fixDown()
        return place

    def fixDown(self,index =1):
        if self.heapL == [] or index > len(self.heapL):
            pass
        left = self.leftChild(index)
        leftIndex = self.heapL.index(left)

        right = self.rightChild(index)
        rightIndex = self.heapL.index(right)

        if left < self.heapL[index]:
            self.heapL[leftIndex] = self.heapL[index]
            self.heapL[index] = left
            self.fixDown(leftIndex)

        if right < self.heapL[index]:
            self.heapL[rightIndex] = self.heapL[index]
            self.heapL[index] = right
            self.fixDown(rightIndex)
    
class HeapNode:
    def __init__(self):
        self.data = val
        self.right = None
        self.left = None 
