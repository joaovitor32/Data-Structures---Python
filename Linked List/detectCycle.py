from LinkedList import Node, LinkedList

class NewNode(Node):
    def __init__(self,data):
        super().__init__(data)
        self.isVisited=False

def detectCycle(linkedList):
    currentNode=linkedList.head
    currentNode.isVisited=True
    while True:
        if currentNode.next.isVisited is True:
            currentNode.next=None
            break
        currentNode=currentNode.next
        currentNode.isVisited=True
