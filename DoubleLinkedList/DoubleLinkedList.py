class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    
    def insertEnd(self,newNode):
        if self.head is None:
            self.head=newNode
            return
        currentNode=self.head 
        while True:
            if currentNode.next is None:
                break
            currentNode=currentNode.next
        currentNode.next=newNode
        newNode.previous=currentNode

    def printList(self):
        if self.head is None:
            print("A lista esta vazia")
            return
        print('Printando do inicio:')
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

    def listLength(self):
        length=0
        currentNode=self.head
        while currentNode is not None:
            currentNode=currentNode.next
            length+=1

        return length

    def insertHead(self,newNode):
        previousHead=self.head
        self.head=newNode
        self.head.next=previousHead
        previousHead.previous=self.head

    def insertAt(self,newNode,position):
        
        if position<-1  or position>self.listLength():
            print("Posicao invalida")
            return

        if position is self.listLength():
            self.insertEnd(newNode)
            return

        if position is 0:
            self.insertHead(newNode)
            return
        
        currentNode=self.head
        currentPosition=0
        while True:
            if currentPosition==position:
                currentNode.previous.next=newNode
                newNode.previous=currentNode.previous
                newNode.next=currentNode
                currentNode.previous=newNode
                break
            currentNode=currentNode.next
            currentPosition+=1
            
    def deleteHead(self):
        self.head=self.head.next
        self.head.previous.next=None
        self.head.previous=None

    def deleteAt(self,position):
        currentNode=self.head
        currentPosition=0

        while True:
            if currentPosition==position:
                currentNode.previous.next=currentNode.next
                currentNode.next.previous=currentNode.previous
                currentNode.next=None
                currentNode.previous=None
                break
            currentNode=currentNode.next
            currentPosition+=1