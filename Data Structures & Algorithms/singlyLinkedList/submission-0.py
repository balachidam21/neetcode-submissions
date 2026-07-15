class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        temp = self.head.next
        i = 0
        while temp:
            if i == index:
                return temp.value
            i += 1
            temp = temp.next
        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = ListNode(val)
        self.tail.next = newNode
        self.tail = newNode
        
    def remove(self, index: int) -> bool:
        temp = self.head
        i = 0
        while i < index and temp:
            i += 1
            temp = temp.next

        if temp and temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
            return True
        return False        

    def getValues(self) -> List[int]:
        values = []
        tempNode = self.head.next
        while tempNode is not None:
            values.append(tempNode.value)
            tempNode = tempNode.next
        return values
        
