from LinkedList import Node,LinkedList

def swapNext(linkedList,previousNode,largestNode,nextNode):
    largestNode.next=nextNode.next
    nextNode.next=largestNode
    if largestNode is linkedList.head:
        linkedList.head=nextNode
        return
    previousNode.next=nextNode

def sort(linkedList):
    numberOfIterations=linkedList.listLength()-1
    while numberOfIterations!=0:
            largestNode=linkedList.head
            previousNode=None
            numberOfComparisons=numberOfIterations
            while numberOfComparisons!=0:
                if largestNode.data>largestNode.next.data:
                    swapNext(linkedList,previousNode,largestNode,largestNode.next)
                else:
                    previousNode=largestNode
                    largestNode=largestNode.next
                numberOfComparisons-=1
            numberOfIterations-=1


