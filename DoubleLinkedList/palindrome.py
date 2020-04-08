from DoubleLinkedList import Node,DoublyLinkedList

def palindrome(doublyLinkedList):
    startPointer = doublyLinkedList.head
    endPointer = doublyLinkedList.head
    while endPointer.next is not None:
        endPointer = endPointer.next
    while True:
        if startPointer == endPointer:
            print("List is palindrome")
            return
        if startPointer.data == endPointer.data:
            startPointer = startPointer.next
            endPointer = endPointer.previous
        else:
            print("List is not palindrome")
            return