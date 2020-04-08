from DoubleLinkedList import Node,DoublyLinkedList

def findGreater(doublyLinkedList):
    length=doublyLinkedList.listLength()
    middlePosition=length//2

    if length>3:

        currentNode=doublyLinkedList.head
        currentPosition=0

        while True:
            if currentPosition==middlePosition:
                if currentNode.previous.data>currentNode.next.data:
                    print("Previous node has a greater value than next node")
                else:
                    print("Next node has a greater value than previous node")
                break
            currentNode=currentNode.next
            currentPosition+=1
    else:
        print("Not enough nodes")

