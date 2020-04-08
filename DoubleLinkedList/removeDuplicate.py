from DoubleLinkedList import Node, DoublyLinkedList

def removeDuplicate(doublyLinkedList):
    nodeCount={}
    currentNode=doublyLinkedList.head
    while True:
        if currentNode.data not in nodeCount.keys():
            nodeCount[currentNode.data]=1
        else:
            nodeCount[currentNode.data] +=1
        if currentNode.next is None:
            while True:
                if currentNode.previous is None:
                    break
                previousNode=currentNode.previous
                if nodeCount[currentNode.data]>1:
                    currentNode.previous.next=currentNode.next
                    if currentNode.next is not None:
                        currentNode.next.previous=currentNode.previous
                    currentNode.next=None
                    currentNode.previous=None
                    nodeCount[currentNode.data]-=1
                currentNode=previousNode
            break
        currentNode=currentNode.next


