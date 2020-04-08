from DoubleLinkedList import Node,DoublyLinkedList

def reverse(doublyLinkedList):
    currentNode=doublyLinkedList.head
    while currentNode is not None:
        nextNode=currentNode.next
        currentNode.next=currentNode.previous
        currentNode.previous=nextNode
        if currentNode.previous is None:
            doublyLinkedList.head=currentNode
        currentNode=nextNode

