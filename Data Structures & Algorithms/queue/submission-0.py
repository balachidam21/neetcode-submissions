class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)

        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def isEmpty(self) -> bool:
        if self.size == 0:
            return True
        return False

    def append(self, value: int) -> None:
        #append will be InsertAtTail

        newNode = ListNode(value)

        predecessor, successor = self.right.prev, self.right

        newNode.next = successor
        newNode.prev = predecessor

        predecessor.next = newNode
        successor.prev = newNode
        self.size += 1

    def appendleft(self, value: int) -> None:
        #appendleft will be InsertAtHead

        newNode = ListNode(value)

        predecessor, successor = self.left, self.left.next

        newNode.next = successor
        newNode.prev = predecessor

        predecessor.next = newNode
        successor.prev = newNode
        self.size += 1

    def pop(self) -> int:
        #pop will be deleteAtTail
        if self.isEmpty():
            return -1
        lastNode = self.right.prev

        newLastNode = lastNode.prev
        newLastNode.next = self.right
        self.right.prev = newLastNode
        self.size -= 1
        return lastNode.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        headNode = self.left.next
        newHeadNode = headNode.next
        newHeadNode.prev = self.left
        self.left.next = newHeadNode
        self.size -= 1
        return headNode.val
        
