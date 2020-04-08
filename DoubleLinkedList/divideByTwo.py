from DoubleLinkedList import Node,DoublyLinkedList

def divideByTwo(doublyLinkedList):
    currentNode=doublyLinkedList.head.next
    while currentNode is not None:
        if currentNode.previous.data %2 is not 0:
            currentNode.data=currentNode.data//2
        currentNode=currentNode.next

