from LinkedList import Node, LinkedList

def removeDuplicate(linkedList):
    currentNode = linkedList.head
    while True:
        if currentNode.data == currentNode.next.data:
            duplicateNode = currentNode.next
            currentNode.next = duplicateNode.next
            duplicateNode.next = None
            break
        currentNode = currentNode.next                          


nodeOne = Node(1)
nodeTwo = Node(2)
nodeThree = Node(3)
nodeFour = Node(3)
nodeFive = Node(5)
linkedList = LinkedList(None)
linkedList.insertEnd(nodeOne)
linkedList.insertEnd(nodeTwo)
linkedList.insertEnd(nodeThree)
linkedList.insertEnd(nodeFour)
linkedList.insertEnd(nodeFive)
removeDuplicate(linkedList)
linkedList.printList()