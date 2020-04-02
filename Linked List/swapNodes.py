from LinkedList import Node,LinkedList

def swapNodes(linkedList,dataOne,dataTwo):
    currentNode=linkedList.head
    previousFirst=None
    previousSecond=None

    while True:
        if currentNode.data==dataOne:
            firstNode=currentNode
            break
        else:
            previousFirst=currentNode
            currentNode=currentNode.next

    currentNode=linkedList.head
    while True:
        if currentNode.data==dataTwo:
            secondNode=currentNode
            break
        previousSecond=currentNode
        currentNode=currentNode.next

    previousFirst.next=secondNode
    nextSecond=secondNode.next
    secondNode.next=firstNode.next
    previousSecond.next=firstNode
    firstNode.next=nextSecond


