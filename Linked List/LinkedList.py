class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,data):
        self.head=None

    def listLength(self):
        currentNode=self.head
        length=0

        while currentNode is not None:
            length+=1
            currentNode=currentNode.next
        
        return length

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    lastNode.next=newNode
                    break
                lastNode=lastNode.next
    
    def insertHead(self,newNode):

        temporaryNode=self.head
        self.head=newNode
        self.head.next=temporaryNode
        del temporaryNode

    def insertAt(self,newNode,position):
        currentNode=self.head
        currentPosition=0

        if position>self.listLength():
            print("Nao e possivel efetuar essa operação")
            return

        if position<0:
            print("Nao e possivel efetuar essa operação")
            return

        if position==0:
            self.insertHead(newNode)
            return

        while True:
            if currentPosition==position:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            previousNode=currentNode
            currentNode=currentNode.next
            currentPosition+=1

    def deleteHead(self):
        
        if self.isListEmpty():
            print("A lista esta vazia")
            return

        previousHead=self.head
        self.head=self.head.next
        previousHead.next=None

    def deleteAt(self,position):
        if position>=self.listLength():
            print("Nao e possivel efetuar essa operação")
            return

        if position<0:
            print("Nao e possivel efetuar essa operação")
            return

        if self.listLength() is False:
            if position ==0:
                self.deleteHead()
                return
                
            currentNode=self.head
            currentPosition=0
            while True:
                if currentPosition==position:
                    previousNode.next=currentNode.next
                    currentNode.next=None
                    break
                else:
                    previousNode=currentNode
                    currentNode=currentNode.next
                    currentPosition+=1

    def deleteEnd(self):
        if(self.head.next is Noe):
            self.deleteHead()
            return 

        lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next=None

    def printList(self):
        if self.head is None:
            print("Linked list não possui nenhum elemento")
            return 
            
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next



