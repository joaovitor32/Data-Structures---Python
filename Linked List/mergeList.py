from LinkedList import Node, LinkedList


def mergeLists(firstList,secondList,mergedList):
    currentFirst=firstList.head
    currentSecond=secondList.head
    while True:
        if currentFirst is None:
            mergedList.insertEnd(currentSecond)
            break

        if currentSecond is None: 
            mergedList.insertEnd(currentFirst)
            break

        if currentFirst.data<currentSecond.data:
            currentFirstNext=currentFirst.next
            currentFirst.next=None
            mergedList.insertEnd(currentFirst)
            currentFirst=currentFirstNext
        else:
            currentSecondNext=currentSecond.next
            currentSecond.next=None
            mergedList.insertEnd(currentSecond)
            currentSecond=currentSecondNext                       

        

# First List

mergedList = LinkedList(None)

mergeLists(firstList, secondList, mergedList)
del firstList
del secondList

print("Printing Merged List")
mergedList.printList()